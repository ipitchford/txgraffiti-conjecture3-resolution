#!/usr/bin/env python3
"""Check a proof tree that no independent dominating set has size <= 15.

The certificate is deliberately simple. At each proof node:

* ``P w`` branches on every currently addable vertex in the closed
  neighbourhood of an undominated vertex w;
* ``B`` closes a branch by the degree bound: one new vertex can dominate at
  most four currently undominated vertices in a cubic graph;
* ``C`` closes a branch after 16 vertices have already been selected; and
* ``X w`` closes a branch when an undominated w has no addable closed-neighbour.

The checker reconstructs every state from the root and recomputes all branch
candidate sets. It does not trust node counts, masks, lower bounds or choices
supplied by the generator.
"""
from __future__ import annotations

import argparse
import gzip
import json
from dataclasses import dataclass
from pathlib import Path
from typing import IO, Iterator


@dataclass
class Stats:
    nodes: int = 0
    branches: int = 0
    bound_leaves: int = 0
    cardinality_leaves: int = 0
    dead_leaves: int = 0
    max_depth: int = 0


def open_text(path: Path) -> IO[str]:
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="ascii", newline="")
    return path.open("rt", encoding="ascii", newline="")


def nonempty_lines(handle: IO[str]) -> Iterator[str]:
    for raw in handle:
        line = raw.strip()
        if line:
            yield line


def load_graph(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    n = int(data["order"])
    edges = [tuple(sorted(map(int, edge))) for edge in data["edges"]]
    if n != 50:
        raise ValueError(f"expected 50 vertices, found {n}")
    if len(edges) != 75 or len(set(edges)) != 75:
        raise ValueError("expected 75 distinct edges")

    adjacency = [0] * n
    for u, v in edges:
        if not (0 <= u < v < n):
            raise ValueError(f"invalid edge {(u, v)}")
        if adjacency[u] & (1 << v):
            raise ValueError(f"duplicate edge {(u, v)}")
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    degrees = [mask.bit_count() for mask in adjacency]
    if any(degree != 3 for degree in degrees):
        raise ValueError(f"graph is not cubic: degree multiset={sorted(set(degrees))}")
    closed = [adjacency[v] | (1 << v) for v in range(n)]
    return data, adjacency, closed


def verify_upper_witness(data, adjacency) -> None:
    witness = [int(v) for v in data["independent_dominating_witness"]]
    if len(witness) != 16 or len(set(witness)) != 16:
        raise ValueError("invalid size-16 witness declaration")
    chosen = sum(1 << v for v in witness)
    for v in witness:
        if adjacency[v] & (chosen ^ (1 << v)):
            raise ValueError("declared witness is not independent")
    full = (1 << len(adjacency)) - 1
    dominated = 0
    for v in witness:
        dominated |= adjacency[v] | (1 << v)
    if dominated != full:
        raise ValueError("declared witness is not dominating")


def verify_matching_and_lower_bound(data, adjacency) -> None:
    matching = [tuple(map(int, edge)) for edge in data["maximal_matching"]]
    if len(matching) != 15:
        raise ValueError("expected a 15-edge matching witness")
    used = 0
    for u, v in matching:
        if not (adjacency[u] & (1 << v)):
            raise ValueError(f"matching contains non-edge {(u, v)}")
        if used & ((1 << u) | (1 << v)):
            raise ValueError("matching edges are not vertex-disjoint")
        used |= (1 << u) | (1 << v)
    for u in range(len(adjacency)):
        neighbours = adjacency[u]
        while neighbours:
            bit = neighbours & -neighbours
            v = bit.bit_length() - 1
            neighbours ^= bit
            if u < v and not (used & (1 << u)) and not (used & (1 << v)):
                raise ValueError("matching is not maximal")
    # Every edge in a cubic graph dominates at most 2*3-1=5 edges.
    if (len(data["edges"]) + 4) // 5 != 15:
        raise ValueError("edge-domination lower bound does not equal 15")


class TreeChecker:
    def __init__(self, lines: Iterator[str], closed: list[int]):
        self.lines = iter(lines)
        self.closed = closed
        self.n = len(closed)
        self.full = (1 << self.n) - 1
        self.target = 15
        self.cap = 4
        self.stats = Stats()

    def next_token(self) -> str:
        try:
            return next(self.lines)
        except StopIteration as exc:
            raise ValueError("certificate ended before the proof tree was complete") from exc

    def check_node(self, dominated: int, size: int, depth: int) -> None:
        token = self.next_token()
        self.stats.nodes += 1
        self.stats.max_depth = max(self.stats.max_depth, depth)

        if token == "C":
            if size <= self.target:
                raise ValueError(f"invalid cardinality leaf at size {size}")
            self.stats.cardinality_leaves += 1
            return

        if dominated == self.full:
            raise ValueError(f"certificate reaches a dominating independent set of size {size}")

        undominated = self.full & ~dominated
        if token == "B":
            additions_needed = (undominated.bit_count() + self.cap - 1) // self.cap
            if size + additions_needed <= self.target:
                raise ValueError(
                    "invalid bound leaf: size={} remaining={} lower_bound={}".format(
                        size, undominated.bit_count(), additions_needed
                    )
                )
            self.stats.bound_leaves += 1
            return

        fields = token.split()
        if len(fields) != 2 or fields[0] not in {"P", "X"}:
            raise ValueError(f"unknown certificate token: {token!r}")
        try:
            witness = int(fields[1])
        except ValueError as exc:
            raise ValueError(f"invalid witness vertex in token: {token!r}") from exc
        if not (0 <= witness < self.n) or not (undominated & (1 << witness)):
            raise ValueError(f"branch witness {witness} is not currently undominated")

        candidates_mask = self.closed[witness] & ~dominated
        candidates = [v for v in range(self.n) if candidates_mask & (1 << v)]

        if fields[0] == "X":
            if candidates:
                raise ValueError(f"dead leaf has addable candidates {candidates}")
            self.stats.dead_leaves += 1
            return

        if not candidates:
            raise ValueError("branch node has no candidates")
        self.stats.branches += 1
        for vertex in candidates:
            # vertex lies outside the union of closed neighbourhoods of all
            # selected vertices, so adding it preserves independence.
            self.check_node(dominated | self.closed[vertex], size + 1, depth + 1)

    def finish(self) -> None:
        try:
            extra = next(self.lines)
        except StopIteration:
            return
        raise ValueError(f"trailing certificate data after root proof: {extra!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("graph", type=Path)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()

    data, adjacency, closed = load_graph(args.graph)
    verify_upper_witness(data, adjacency)
    verify_matching_and_lower_bound(data, adjacency)

    with open_text(args.certificate) as handle:
        lines = nonempty_lines(handle)
        try:
            header = next(lines)
        except StopIteration as exc:
            raise SystemExit("empty certificate") from exc
        if header != "IDS15_TREE_V1":
            raise SystemExit(f"bad certificate header: {header!r}")
        checker = TreeChecker(lines, closed)
        checker.check_node(0, 0, 0)
        checker.finish()

    s = checker.stats
    print(
        "TREE_VERIFIED nodes={} branches={} bound_leaves={} cardinality_leaves={} "
        "dead_leaves={} max_depth={}".format(
            s.nodes,
            s.branches,
            s.bound_leaves,
            s.cardinality_leaves,
            s.dead_leaves,
            s.max_depth,
        )
    )
    print("TREE_CHECK_PASSED result=no_ids_size_le_15")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"CERTIFICATE REJECTED: {exc}", file=__import__("sys").stderr)
        raise SystemExit(1)
