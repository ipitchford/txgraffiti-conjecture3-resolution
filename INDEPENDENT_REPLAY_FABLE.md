> **Predecessor-scoped review record.** This receipt applies to `v2-theorem`, SHA-256 `106787526e7d356d7c0535ab01c43aa7d6a1223a95fe728bba76e287aadea589`, not to exact v4.

# Independent agent replay receipt: Fable

**Recorded:** 6 August 2026, Europe/London  
**Reviewed object:** `txgraffiti_conjecture3_resolution_v2.zip` with SHA-256 `106787526e7d356d7c0535ab01c43aa7d6a1223a95fe728bba76e287aadea589`  
**Reviewer type:** independent AI-agent analysis, not human journal peer review  
**Execution scope:** independent harness only; none of the reviewed bundle's scripts were executed

This receipt was supplied after the reviewed archive had been produced. It is preserved below substantively verbatim. It applies to the exact predecessor hash above, not automatically to later byte-distinct releases. `VERSION_HISTORY.md` records the relationship.

## Authentication

- ZIP SHA-256 `106787526e7d356d7c0535ab01c43aa7d6a1223a95fe728bba76e287aadea589` matched its sidecar. All 11 internal `SHA256SUMS` entries verified.
- `counterexample.edgelist` and `counterexample.g6` were byte-identical to v1. The restructured `counterexample.json` decoded to the identical formula, as a canonical clause-set, and the identical 75-edge list; it carried v1's witness as `alternate_public_witness`. The graph was the same mathematical object as public repository commit `7810f30c` at `2026-07-23T03:09:43Z`.
- `ids_le15.cnf`, with 850 variables and 1,695 clauses, had SHA-256 `62f4846e7158241a0ee65e845c032466fad0399b1c8b90c23806d3e09199a107` and was byte-identical to the public repository's file.

## New claims independently verified

1. **Exact identity:** the proof of \(i(G(F))=k+\beta(F)\), where \(\beta\) is bilateral deficiency, was re-derived line by line and probed against tautological clauses, one-sided literals, empty clauses, absent variables and \(k=0\). It holds for arbitrary indexed CNFs under clause-as-literal-set semantics. A toy instance was cross-checked.
2. **Twice-occurrence theorem:** for an exact twice-positive/twice-negative proper 3-CNF, the derivation that \(G(F)\) is cubic and \(\mu^*(G(F))=k\) was independently re-derived; the edge count \(5k\) and cubic domination bound were confirmed.
3. **Dominating-induced-matching threshold:** the theorem excluding cubic DIM counterexamples below order 50, including duplicate-clause deletion and maximality of the DIM matching, was independently re-derived.
4. The simple witness
   \[
   \{0,3,5,6,8,10,12,14,16,18,20,22,24,26,28,47\}
   \]
   was checked to be independent and dominating. It is the set derived from the stated near-satisfying assignment, which falsifies exactly \(C_{18}\).
5. Formula facts were brute-forced: zero satisfying assignments; minimum unsatisfied-clause count one, attained by exactly 3,318 of 32,768 assignments; and minimal unsatisfiability, because every single-clause deletion is satisfiable.
6. Recorded receipts matched independent v1 numbers: 14,348,907 partial assignments checked; 939,975 bilateral; zero violations; direct branch-and-bound optimum 16 with 256,714 nodes; mixed-integer optima \(i=16\) and \(\mu^*=15\) with zero reported gap.
7. The submitted-checker patch adds graph6 character-set and length validation, an explicit \(m\le64\) guard and a corrected safe-domain header.
8. No identifying strings or email addresses were found in the reviewed bundle.

## Bounded novelty position for the exact identity

- Ahadi and Dehghan (2019) study the same exact-occurrence formula class used in the twice-occurrence theorem. Their results concern hardness equivalences and satisfiability-based reductions, not the exact additive identity \(i=k+\beta\). No collision was found.
- Zverovich's 2006 satgraph paper was inspected at title and abstract level only. It relates independent domination to satisfiability, but no statement of the additive identity was located. Full-text collision risk remains.
- No collision for \(i(G(F))=k+\beta(F)\) was found within the bounded search. Search absence does not establish priority.

## Not independently recomputed

The intermediate counts from the \(2^{20}\) clause-subset audit - 163,413, 715 and 38,848 - were not independently recomputed. The method was inspected and found sound. Its headline conclusion, that no independent dominating set has size at most 15, was entailed by three independently replayed routes.
