> **Supporting bounded search record.** `PRIOR_ART_COMPARISON.md` and `SOURCES.md` contain the canonical v4 positioning.

# Literature, provenance and bounded-novelty audit

**Search date:** 6 August 2026  
**Questions:** whether the regular-graph inequality had already been resolved; whether the 20-clause threshold is supported; and whether the exact bilateral-deficiency identity collides with prior SAT-to-independent-domination work.

## Fixed objects

1. **Original conjecture.** Caro, Davila and Pepper state as Conjecture 15 that every nonzero regular graph satisfies \(i(G)\leq\mu^*(G)\).  
   https://doi.org/10.7151/dmgt.2317
2. **Later open-problem statement.** Davila, Brimkov and Pepper restate the same inequality as TxGraffiti Conjecture 3 in 2025.  
   https://arxiv.org/abs/2507.17780
3. **Bounded-occurrence threshold.** Zhang, Peitl and Szeider report that the smallest unsatisfiable \((3,2,2)\)-formula has 20 clauses.  
   https://doi.org/10.4230/LIPIcs.SAT.2024.31
4. **Public counterexample.** `djma/TxGraffiti-conjecture3-counterexample` contains the same 50-vertex graph and predates this audit.  
   https://github.com/djma/TxGraffiti-conjecture3-counterexample
5. **Exact-occurrence antecedent.** Ahadi and Dehghan define \((2/2/3)\)-SAT as 3-SAT in which each variable occurs exactly twice positively and twice negatively, and prove complexity results with domination applications.  
   https://doi.org/10.23638/DMTCS-21-4-9
6. **Satgraph antecedent.** Zverovich relates satisfiability and independent domination on satgraphs.  
   https://doi.org/10.1016/j.tcs.2005.08.038

## Search boundary

The audit covered exact conjecture wording, invariant combinations, the numerical signature \(15<16\), TxGraffiti identifiers, arXiv, journal landing pages, general web indices and GitHub. For the exact identity, it searched combinations of independent domination, SAT graphs, partial assignments, residual clauses, formula deficiency and additive optimisation identities.

The boundary excludes private correspondence, unindexed theses or talks, closed bibliographic databases, unpublished computation and material not exposed to the search services. Zverovich's paper was inspected at title and abstract level in the bounded novelty review; its full body was not exhaustively compared line by line. Search absence does not establish priority.

## Findings

### Conjecture status and public construction

The search found the public 23 July 2026 repository containing the same graph, formula and invariant values. No earlier independent public resolution was located within the stated corpus. The present release therefore treats the graph as a verified public counterexample and makes no first-discovery claim.

### Clause threshold

Zhang, Peitl and Szeider's Table 1 gives 20 for \((3,2,2)\)-CNF. This supports the theorem that a cubic graph with a dominating induced matching and fewer than 50 vertices satisfies the conjectured inequality. The counterexample itself does not depend on this external threshold.

### Exact-occurrence class

Ahadi and Dehghan's \((2/2/3)\)-SAT is the same exact signed-occurrence class used in the cubic formula construction: each variable occurs twice positively and twice negatively. Their paper establishes satisfiability hardness and domination-related reductions. It does not, in the inspected full text, state the additive identity

\[
i(G(F))=k+\beta(F).
\]

The manuscript cites this work in the body; the formula class is not claimed as new.

### Satgraph collision risk

Zverovich's abstract states that SAT is linear-time equivalent to finding the independent domination number in a corresponding satgraph. This is a close conceptual antecedent. No exact bilateral-deficiency identity was located in the material inspected. Because the full article was not exhaustively compared, residual collision risk remains.

## Bounded novelty conclusion

The graph is not new to this release. The SAT-to-independent-domination reduction idea and exact twice-occurrence formula class are established. The exact identity \(i(G(F))=k+\beta(F)\) appears distinct within the bounded corpus and survived an independent line-by-line re-derivation, but it should be described as an **apparently new formulation after bounded search**, not as a secured priority claim.

## Bibliographic correction

The 2025 paper's reference list prints DOI `10.7151/dmgt.2353` for the Caro-Davila-Pepper article. Journal and bibliographic records give `10.7151/dmgt.2317`; the release uses the latter.
