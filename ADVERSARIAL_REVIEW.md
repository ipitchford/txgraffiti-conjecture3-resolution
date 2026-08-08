> **Supporting internal adversarial record.** This is not independent review of the exact release.

# Adversarial review

## Bottom line

The displayed graph satisfies \(\mu^*(G)=15<16=i(G)\). The counterexample claim survives the independent parsers, explicit witnesses, elementary matching proof, raw-graph certificate, bilateral enumeration, mutation tests and generic optimisation audit. Remaining uncertainties concern priority, theorem novelty and global minimality, not the graph's two invariant values.

## 1. Could the graph fail to be a connected cubic simple graph?

No defect was found. Formula, JSON, edge-list and graph6 parsers reconstruct 50 vertices and 75 distinct non-loop edges, degree sequence \(3^{50}\), one connected component and girth five. The handshake check gives \(50\cdot3/2=75\).

## 2. Could the 15-edge matching be non-maximal or non-minimum?

The 15 complementary-literal edges are disjoint. Their unmatched clause vertices form an independent set, so the matching is maximal. One edge in a cubic graph dominates at most five edges. Since the graph has 75 edges, every maximal matching has at least 15 edges. Thus \(\mu^*(G)=15\) without optimisation software.

## 3. Could the size-16 witnesses fail independence or domination?

Two distinct 16-vertex sets are checked against the raw graph. One comes directly from a complete assignment that misses only \(C_{18}\); the other is the witness in the public repository. Both are independent and dominate all 50 vertices.

## 4. Does formula unsatisfiability alone prove \(i(G)>15\)?

No. An independent dominating set may mix literal and clause vertices. Any proof that considers only one literal per variable is incomplete. The release addresses mixed sets in two exact ways:

- the proof tree searches the raw 50-vertex graph;
- the bilateral-deficiency identity characterises mixed sets and the verifier checks all \(3^{15}\) partial assignments.

## 5. Could the proof-tree generator and checker share the same bug?

They use different languages, state implementations and graph inputs. The C++ generator reconstructs the graph from the clause formula. The Python checker reads the raw edge list and recomputes every selected set, dominated region, branch candidate set and lower bound. It rejects invalid leaves, invalid witnesses, truncation and trailing data. Deterministic regeneration is byte-identical.

This does not prove absolute implementation independence, but it sharply reduces shared-bug risk.

## 6. Is the lower-bound leaf rule valid?

Yes. In a cubic graph, a newly selected vertex has a closed neighbourhood of size at most four. If \(u\) vertices remain undominated, at least \(\lceil u/4\rceil\) further selections are required. A branch closes only when that lower bound pushes the total above 15.

## 7. Is the exact identity valid for arbitrary CNFs?

The proof uses indexed clauses treated as literal sets. It does not require proper 3-CNF. Tautological clauses, one-sided literals, empty clauses, absent variables and \(k=0\) do not break either direction. Fable independently re-derived the proof and probed these edge cases on the authenticated `v2-theorem` predecessor.

## 8. Could the exact identity already be known?

Yes; literature search cannot exclude that. Zverovich's satgraph work closely relates SAT and independent domination, and only title/abstract-level comparison was available in the bounded review. Ahadi and Dehghan use the same exact-occurrence class, but their inspected results concern hardness reductions rather than the additive identity. The release therefore uses bounded novelty language and makes no priority claim.

## 9. Is the order-50 threshold correction justified?

Within the dominating-induced-matching class, yes. Each matching endpoint has exactly two neighbours outside the matching, so each literal occurs at most twice with each polarity. The endpoint formula is \((3,2,2)\), not merely \((3,4)\). Zhang, Peitl and Szeider's published table places the first unsatisfiable formula in that class at 20 clauses. Since a cubic DIM graph has \(2n/5\) unmatched vertices, fewer than 50 vertices give fewer than 20 clauses.

This theorem depends on the cited SAT result, which the package does not re-derive. The counterexample does not depend on that external result.

## 10. Is order 50 globally minimal?

Unknown. The theorem excludes smaller counterexamples only among cubic graphs with a dominating induced matching. A smaller cubic counterexample of another structure, or a smaller regular counterexample of higher degree, remains possible.

## 11. Does Fable's receipt cover v3?

Not byte-for-byte. It authenticates `v2-theorem`, SHA-256 `106787...a589`. The proof-tree predecessor and merged v3 are distinct archives. The release records inherited claims and new artefacts separately rather than treating one receipt as universal.

## 12. What remains load-bearing?

For the disproof:

1. raw graph data;
2. the elementary proof \(\mu^*(G)=15\);
3. one explicit size-16 independent dominating set; and
4. either the checked proof tree or the exact bilateral-deficiency enumeration excluding size at most 15.

The mixed-integer models, formula minimal-unsatisfiability facts, literature search and historical finite sweeps are corroborative.
