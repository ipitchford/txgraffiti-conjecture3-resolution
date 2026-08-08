#!/usr/bin/env python3
"""Independent generic MILP audit of the graph in counterexample.json.

Requires NumPy and SciPy with scipy.optimize.milp.  This script does not use the
formula-specific bilateral lemma or the C++ branch-and-bound implementation.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, deque
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def load_graph(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    n = int(data["order"])
    edges = [tuple(map(int, e)) for e in data["edges"]]
    if len(edges) != len(set(tuple(sorted(e)) for e in edges)):
        raise ValueError("duplicate edges")
    adj = [set() for _ in range(n)]
    for u, v in edges:
        if u == v or not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"invalid edge {(u, v)}")
        adj[u].add(v)
        adj[v].add(u)
    return data, n, edges, adj


def connected(adj):
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == len(adj)


def solve_independent_domination(n, edges, adj):
    rows, lower, upper = [], [], []
    for u, v in edges:
        rows.append({u: 1.0, v: 1.0})
        lower.append(-np.inf)
        upper.append(1.0)
    for v in range(n):
        row = {v: 1.0}
        row.update({u: 1.0 for u in adj[v]})
        rows.append(row)
        lower.append(1.0)
        upper.append(np.inf)
    A = lil_matrix((len(rows), n), dtype=float)
    for r, row in enumerate(rows):
        for c, value in row.items():
            A[r, c] = value
    result = milp(
        c=np.ones(n),
        integrality=np.ones(n),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=LinearConstraint(A.tocsr(), np.asarray(lower), np.asarray(upper)),
        options={"mip_rel_gap": 0.0, "time_limit": 300.0},
    )
    if not result.success:
        raise RuntimeError(f"independent-domination MILP failed: {result.message}")
    selected = [i for i, x in enumerate(result.x) if x > 0.5]
    independent = all(not (u in selected and v in selected) for u, v in edges)
    dominating = all(v in selected or any(u in selected for u in adj[v]) for v in range(n))
    return result, selected, independent, dominating


def solve_minimum_maximal_matching(n, edges, adj):
    m = len(edges)
    incidence = [[] for _ in range(n)]
    for e, (u, v) in enumerate(edges):
        incidence[u].append(e)
        incidence[v].append(e)
    rows, lower, upper = [], [], []
    for v in range(n):
        rows.append({e: 1.0 for e in incidence[v]})
        lower.append(-np.inf)
        upper.append(1.0)
    for u, v in edges:
        candidates = set(incidence[u]) | set(incidence[v])
        rows.append({e: 1.0 for e in candidates})
        lower.append(1.0)
        upper.append(np.inf)
    A = lil_matrix((len(rows), m), dtype=float)
    for r, row in enumerate(rows):
        for c, value in row.items():
            A[r, c] = value
    result = milp(
        c=np.ones(m),
        integrality=np.ones(m),
        bounds=Bounds(np.zeros(m), np.ones(m)),
        constraints=LinearConstraint(A.tocsr(), np.asarray(lower), np.asarray(upper)),
        options={"mip_rel_gap": 0.0, "time_limit": 300.0},
    )
    if not result.success:
        raise RuntimeError(f"minimum-maximal-matching MILP failed: {result.message}")
    selected = [edges[e] for e, x in enumerate(result.x) if x > 0.5]
    return result, selected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="counterexample.json")
    args = parser.parse_args()
    data, n, edges, adj = load_graph(Path(args.input))
    print(f"STRUCTURE n={n} m={len(edges)} degrees={dict(Counter(map(len, adj)))} connected={connected(adj)}")
    ids, ids_set, independent, dominating = solve_independent_domination(n, edges, adj)
    print(
        "IDS optimum={} gap={} nodes={} independent={} dominating={} witness={}".format(
            round(float(ids.fun)), getattr(ids, "mip_gap", None),
            getattr(ids, "mip_node_count", None), independent, dominating, ids_set
        )
    )
    mm, mm_set = solve_minimum_maximal_matching(n, edges, adj)
    print(
        "MIN_MAXIMAL_MATCHING optimum={} gap={} nodes={} matching={}".format(
            round(float(mm.fun)), getattr(mm, "mip_gap", None),
            getattr(mm, "mip_node_count", None), mm_set
        )
    )
    if round(float(ids.fun)) != 16 or round(float(mm.fun)) != 15 or not independent or not dominating:
        raise SystemExit("AUDIT FAILED")
    print("MILP_AUDIT_PASSED result=i_16_mu_star_15")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
