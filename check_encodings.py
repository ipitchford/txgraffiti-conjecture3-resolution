#!/usr/bin/env python3
"""Verify that JSON, edge-list and graph6 encodings describe the same graph."""
from __future__ import annotations

import json
from pathlib import Path


def normalise(edges):
    return {tuple(sorted(map(int, edge))) for edge in edges}


def parse_graph6(path: Path):
    text = path.read_text(encoding="ascii").strip()
    if not text:
        raise ValueError("empty graph6 file")
    n = ord(text[0]) - 63
    if not (0 <= n <= 62):
        raise ValueError("only one-byte graph6 orders are supported")
    bits = []
    for char in text[1:]:
        value = ord(char) - 63
        if not (0 <= value < 64):
            raise ValueError("invalid graph6 character")
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    required = n * (n - 1) // 2
    if len(bits) < required:
        raise ValueError("truncated graph6 payload")
    edges = set()
    offset = 0
    for j in range(1, n):
        for i in range(j):
            if bits[offset]:
                edges.add((i, j))
            offset += 1
    if any(bits[required:]):
        raise ValueError("non-zero graph6 padding")
    return n, edges


def parse_edgelist(path: Path):
    edges = set()
    for lineno, raw in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        if not raw.strip():
            continue
        fields = raw.split()
        if len(fields) != 2:
            raise ValueError(f"bad edge-list line {lineno}")
        u, v = map(int, fields)
        edge = tuple(sorted((u, v)))
        if u == v or edge in edges:
            raise ValueError(f"invalid or duplicate edge-list edge {edge}")
        edges.add(edge)
    return edges



def verify_independent_dominating_witness(n, edges, witness, label):
    vertices = [int(v) for v in witness]
    if len(vertices) != 16 or len(set(vertices)) != 16 or any(v < 0 or v >= n for v in vertices):
        raise ValueError(f"{label} is not a 16-vertex subset")
    selected = set(vertices)
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    for u, v in edges:
        if u in selected and v in selected:
            raise ValueError(f"{label} is not independent: edge {u}-{v}")
    for vertex in range(n):
        if vertex not in selected and not (adjacency[vertex] & selected):
            raise ValueError(f"{label} does not dominate vertex {vertex}")

def main() -> int:
    base = Path(__file__).resolve().parent
    data = json.loads((base / "counterexample.json").read_text(encoding="utf-8"))
    json_edges = normalise(data["edges"])
    variables = int(data["variables"])
    clauses = data["formula_signed_integers"]
    formula_edges = {(2 * j, 2 * j + 1) for j in range(variables)}
    positive = [0] * variables
    negative = [0] * variables
    for clause_index, clause in enumerate(clauses):
        if len(clause) != 3 or len({abs(int(lit)) for lit in clause}) != 3:
            raise ValueError(f"clause {clause_index + 1} is not a 3-clause on distinct variables")
        clause_vertex = 2 * variables + clause_index
        for raw_literal in clause:
            literal = int(raw_literal)
            variable = abs(literal) - 1
            if not (0 <= variable < variables):
                raise ValueError(f"invalid literal {literal}")
            literal_vertex = 2 * variable + (1 if literal > 0 else 0)
            formula_edges.add(tuple(sorted((literal_vertex, clause_vertex))))
            if literal > 0:
                positive[variable] += 1
            else:
                negative[variable] += 1
    if any(count != 2 for count in positive + negative):
        raise ValueError("signed literal occurrences are not all exactly two")

    n_g6, g6_edges = parse_graph6(base / "counterexample.g6")
    list_edges = parse_edgelist(base / "counterexample.edgelist")
    n_json = int(data["order"])
    if n_g6 != n_json:
        raise ValueError(f"order mismatch: graph6={n_g6}, json={n_json}")
    if not (json_edges == formula_edges == g6_edges == list_edges):
        raise ValueError("formula or graph encodings disagree")
    verify_independent_dominating_witness(
        n_json, json_edges, data["independent_dominating_witness"], "primary witness"
    )
    verify_independent_dominating_witness(
        n_json, json_edges, data["alternate_public_witness"], "alternate public witness"
    )
    print(
        f"ENCODINGS_VERIFIED n={n_json} m={len(json_edges)} "
        "formats=formula,json,edgelist,graph6 literal_occurrences=2+2 witnesses=2"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"ENCODING CHECK FAILED: {exc}", file=__import__("sys").stderr)
        raise SystemExit(1)
