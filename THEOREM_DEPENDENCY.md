# Definition transfer for the order-50 theorem

The central 50-vertex counterexample is self-contained. This document concerns only the wider theorem for cubic graphs possessing a dominating induced matching.

## External result ZPS-2024-20-CLAUSE

Zhang, Peitl and Szeider define a clause as a finite non-tautological set of literals and a 3-clause as a clause containing exactly three distinct literals. A \((3,p,q)\)-formula bounds each variable to at most \(p\) positive and \(q\) negative occurrences. Their Table 1 reports 20 as the smallest number of clauses in an unsatisfiable \((3,2,2)\)-formula.

## Derived endpoint formula

Let \(G\) be a finite simple cubic graph with a dominating induced matching \(M\). Orient each edge of \(M\) and create one Boolean variable for that edge. Each unmatched vertex \(w\) has three distinct neighbours, all endpoints of matching edges.

1. If \(w\) is adjacent to both endpoints of one matching edge, its endpoint-selection clause contains complementary literals and is a tautology. Removing this clause preserves satisfiability because it is true under every assignment.
2. Otherwise the three neighbours of \(w\) lie on three distinct matching edges. Its clause therefore contains exactly three distinct literals on three distinct variables and contains no complementary pair.
3. If two unmatched vertices yield extensionally equal clauses, retaining only one copy preserves satisfiability. The external source treats formulas as sets of clauses; the reduced formula therefore matches that convention.
4. Each endpoint of a matching edge has one incident matching edge and exactly two remaining incident edges. Hence each positive and each negative literal appears in at most two derived clauses. Deleting tautologies or duplicate clauses cannot increase these occurrence counts.

The reduced endpoint formula is therefore a \((3,2,2)\)-formula in the source's exact sense and has at most \(|W|\) clauses, where \(W\) is the unmatched vertex set.

## Numerical transfer

Writing \(t=|M|\), edge counting gives

\[
4t=3|W|,
\qquad
|V(G)|=2t+|W|,
\qquad
|W|=\frac{2|V(G)|}{5}.
\]

If \(|V(G)|<50\), then \(|W|<20\). The reduced \((3,2,2)\)-formula has fewer than 20 clauses and is satisfiable by ZPS-2024-20-CLAUSE. A satisfying assignment selects one endpoint of each matching edge, producing an independent dominating set of size \(t\).

This transfer is explicit because the boundary depends on the source's exact clause and occurrence conventions. If the external result or this definition match failed, the restricted threshold theorem would be withdrawn; the 50-vertex counterexample and its certified invariant values would remain intact.
