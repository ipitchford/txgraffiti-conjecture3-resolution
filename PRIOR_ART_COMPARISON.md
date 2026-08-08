# Prior-art comparison for the formula-graph results

**Search date:** 6 August 2026.  
**Scope:** targeted web, publisher, arXiv and bibliographic searches. This is not an exhaustive priority search.

The clause-literal graph architecture is established prior art. The bounded claim is that the exact bilateral-deficiency identity below was not located in the inspected sources.

| Feature | Present release | Zverovich (2006) | Ahadi and Dehghan (2019) | Zhang, Peitl and Szeider (2024) |
|---|---|---|---|---|
| Object | Indexed CNF; clauses treated as literal sets | Satgraphs corresponding to SAT instances | (2/2/3)-SAT and domination reductions | CNF formula encoded by a clause-literal graph for symmetry-aware generation |
| Basic graph architecture | Two complementary literal vertices per variable; one vertex per indexed clause; complement and incidence edges | Related satgraph construction; full theorem-by-theorem comparison remains incomplete | Uses larger regularising variable gadgets in the inspected reduction, rather than only a complementary pair | Explicit literal vertices, clause vertices, complement edges and clause-incidence edges |
| Clause convention | Arbitrary indexed clauses for Theorem 1; proper 3-CNF separately defined | Not fully mapped from the accessible abstract-level record | Each variable appears exactly twice positively and twice negatively; clauses may contain at least two distinct variables | A clause is a finite non-tautological literal set; a 3-clause has exactly three distinct literals |
| Objective | Exact independent domination number | Satisfiability/independent-domination equivalence is reported | Hardness/equivalence results for domination problems | Enumeration of small unsatisfiable bounded-occurrence formulas |
| Direction | Equality between a graph optimum and a partial-assignment deficiency minimum | Reduction/equivalence between SAT and independent domination | Formula-to-graph reductions for hardness | Formula-to-graph encoding for SAT Modulo Symmetries |
| Exact additive identity | \(i(G(F))=k+\beta(F)\) | No equivalent statement located in the accessible record; residual full-text collision risk | No equivalent statement located | No equivalent statement located |
| Signed occurrence threshold | Uses exact twice-positive/twice-negative class for cubicity | Not the inspected focus | Same exact signed-occurrence class is central | Defines \((3,p,q)\); Table 1 gives 20 clauses for \((3,2,2)\) |

## Defensible novelty wording

> We prove the following exact identity; our targeted search did not locate an equivalent published statement.

This wording applies to the identity and bilateral-deficiency formulation. It does **not** claim novelty for the literal-pair/clause-incidence graph, bounded-occurrence formula class, or general use of SAT constructions in independent domination.

## Decisive collision test

An earlier result would collide with Theorem 1 if it translated, under the same indexed-clause semantics, into

\[
i(G(F))=k+\min_{\alpha\ \mathrm{bilateral}}
\bigl(|T(\alpha)|-|U(\alpha)|\bigr).
\]

No such statement was located. A complete full-text comparison of the satgraph literature, especially Zverovich (2006) and subsequent parts, remains a stated literature risk rather than an implied absence.
