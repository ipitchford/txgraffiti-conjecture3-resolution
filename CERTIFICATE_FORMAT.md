# Independent-domination proof-tree certificate

## Claim certified

For the graph in `counterexample.json`, there is no independent dominating set of cardinality at most 15.

The compressed certificate is `ids_le15.tree.gz`. Its uncompressed SHA-256 digest and compressed digest appear in `SHA256SUMS`.

## State invariant

At a proof-tree node, let \(S\) be the independent set selected along the root-to-node path and let

\[
D=N[S]=\bigcup_{v\in S}N[v].
\]

Every vertex outside \(D\) is nonadjacent to every vertex of \(S\), so it can be added without violating independence. The checker reconstructs \(D\) and \(|S|\) from the path; the certificate supplies neither mask nor count.

## Grammar

The first line is

```text
IDS15_TREE_V1
```

A proof node is one of:

- `P w`: `w` is currently undominated. Let \(C=N[w]\setminus D\). The following \(|C|\) subtrees, in increasing vertex order, certify the states obtained by adding each vertex of \(C\).
- `B`: a degree bound closes the branch. If \(u=|V(G)\setminus D|\), each new vertex can dominate at most four currently undominated vertices because the graph is cubic. The checker requires
  \[
  |S|+\left\lceil\frac{u}{4}\right\rceil>15.
  \]
- `C`: the path has already selected more than 15 vertices.
- `X w`: `w` is undominated and \(N[w]\setminus D=\varnothing\), so no independent extension can dominate it.

The canonical certificate happens to use only `P` and `B` nodes.

## Why the branching is exhaustive

Take any independent dominating extension \(S'\supseteq S\). Since `w` is not dominated by \(S\), some future selected vertex must lie in \(N[w]\). Independence forces every future selected vertex to lie outside \(D=N[S]\). Hence \(S'\setminus S\) contains a member of \(C=N[w]\setminus D\), and at least one child contains the extension. Requiring every child subtree to close proves that no extension of size at most 15 exists.

## Independence from the generator

`generate_ids15_certificate.cpp` chooses branch witnesses and emits the tree. `check_ids15_certificate.py` does not trust those choices. It:

1. reads the raw edge list from `counterexample.json`;
2. verifies that the graph has 50 vertices, 75 distinct edges and degree three throughout;
3. reconstructs every state from the root;
4. recomputes each exact branch candidate set;
5. recomputes every lower bound;
6. rejects premature leaves, invalid witnesses, truncation and trailing data.

The canonical tree has 256,714 nodes: 116,229 branch nodes and 140,485 bound leaves, with maximum depth 15. The canonical text tree is 848,888 bytes; deterministic gzip compression reduces it to 21,803 bytes.
