> **Supporting, non-canonical note.** The canonical paper is `MANUSCRIPT.pdf`; exact release status is in `STATUS.md` and `ASSURANCE.md`.

---
title: "Independent verification of a 50-vertex cubic counterexample to a TxGraffiti conjecture"
date: "6 August 2026"
bibliography: references.bib
link-citations: true
---

**Status.** Supporting certificate-backed note for an unrefereed candidate release. The construction was already public. Exact release assurance is stated in `STATUS.md` and `ASSURANCE.md`; this note makes no discovery-priority or independent-reproduction claim [@publicrepo2026].

# Abstract

Caro, Davila and Pepper conjectured that every nonzero regular graph \(G\) satisfies \(i(G)\leq\mu^*(G)\) [@caro2022]. We verify a connected cubic graph on 50 vertices with

\[
\boxed{\mu^*(G)=15<16=i(G)},
\]

which disproves the conjecture. The nontrivial lower bound \(i(G)>15\) has two exact routes: a 256,714-node raw-graph proof tree checked by a separately written standard-library program, and an exhaustive \(3^{15}\)-case bilateral-deficiency calculation. The graph also corrects the natural dominating-induced-matching threshold: the endpoint formula is \((3,2,2)\)-CNF, so published bounded-occurrence SAT results exclude counterexamples in this class below order 50. The graph attains that boundary.

# 1. The conjecture

For a finite simple graph \(G\), an independent dominating set is an independent set whose closed neighbourhood is \(V(G)\). Its minimum cardinality is \(i(G)\). A maximal matching that has minimum cardinality has size \(\mu^*(G)=\gamma_e(G)\).

The conjecture states:

> If \(G\) is \(r\)-regular with \(r>0\), then \(i(G)\leq\mu^*(G)\).

It appears as Conjecture 15 in the published paper and as Conjecture 3 in a later open-problems account [@caro2022; @davila2025].

# 2. Construction

Take variables \(x_1,\ldots,x_{15}\) and clauses

\[
\begin{array}{ll}
C_1=(x_1,x_9,\neg x_{11}), & C_2=(\neg x_4,\neg x_{10},\neg x_{13}),\\
C_3=(x_1,\neg x_9,\neg x_{14}), & C_4=(x_2,x_6,x_{14}),\\
C_5=(\neg x_5,\neg x_6,x_{15}), & C_6=(x_2,\neg x_3,x_{15}),\\
C_7=(x_3,x_5,\neg x_9), & C_8=(\neg x_6,\neg x_{12},\neg x_{15}),\\
C_9=(\neg x_1,x_5,\neg x_{11}), & C_{10}=(x_4,\neg x_7,\neg x_{15}),\\
C_{11}=(\neg x_2,x_8,\neg x_{12}), & C_{12}=(x_3,x_9,x_{11}),\\
C_{13}=(\neg x_4,\neg x_8,x_{10}), & C_{14}=(x_7,\neg x_8,x_{13}),\\
C_{15}=(x_4,x_7,\neg x_{13}), & C_{16}=(\neg x_2,\neg x_7,x_{14}),\\
C_{17}=(\neg x_3,x_{11},\neg x_{14}), & C_{18}=(x_8,x_{10},x_{12}),\\
C_{19}=(\neg x_{10},x_{12},x_{13}), & C_{20}=(\neg x_1,\neg x_5,x_6).
\end{array}
\]

Every signed literal occurs exactly twice.

For each variable create adjacent literal vertices \(v_j^-\) and \(v_j^+\). For each clause create a clause vertex adjacent to its three literal vertices. Add no other edges. With labels

\[
v_j^-=2(j-1),\qquad v_j^+=2(j-1)+1,\qquad c_a=29+a,
\]

the graph has 50 vertices and

\[
15+3\cdot20=75
\]

edges. Every vertex has degree three. Independent parsers confirm simplicity, connectivity and girth five.

# 3. The matching invariant

The 15 literal-pair edges form a matching. The unmatched clause vertices are independent, so the matching is maximal and \(\mu^*(G)\leq15\).

One edge in a cubic graph dominates at most five edges. Every maximal matching is edge-dominating, and this graph has 75 edges. Hence every maximal matching has at least \(75/5=15\) edges. Therefore

\[
\boxed{\mu^*(G)=15}.
\]

# 4. The independent-domination invariant

## 4.1 Explicit upper witness

The assignment

\[
x_1=0,\qquad x_2=x_3=1,\qquad x_4=\cdots=x_{15}=0
\]

satisfies every clause except \(C_{18}\). Selecting its 15 literal vertices and \(c_{18}\) gives

\[
D_0=\{0,3,5,6,8,10,12,14,16,18,20,22,24,26,28,47\}.
\]

Direct checking shows that \(D_0\) is independent and dominating. Thus \(i(G)\leq16\).

## 4.2 Raw-graph lower certificate

`ids_le15.tree.gz` certifies that no independent dominating set has size at most 15. At a node with selected independent set \(S\), the checker reconstructs \(D=N[S]\). For an undominated vertex \(w\), every completion must choose a vertex in \(N[w]\setminus D\), so the tree branches over exactly that set. A branch closes only when the cubic bound

\[
|S|+\left\lceil\frac{|V(G)\setminus D|}{4}\right\rceil>15
\]

holds.

The tree has 256,714 nodes: 116,229 branch nodes and 140,485 bound leaves. The generator is C++; the checker is separately written Python and reads the raw edge list. It recomputes every branch and bound. Deterministic regeneration is byte-identical. Four corrupted trees are rejected.

This proves \(i(G)>15\).

## 4.3 Formula-level lower certificate

For a partial assignment \(\alpha\), let \(U(\alpha)\) be its unassigned variables and \(T(\alpha)\) the clauses not satisfied by an assigned literal. Call \(\alpha\) bilateral when both signs of every variable in \(U(\alpha)\) occur among \(T(\alpha)\).

The exact identity proved in `MANUSCRIPT.md` is

\[
i(G(F))=k+\min_{\alpha\ \mathrm{bilateral}}
\bigl(|T(\alpha)|-|U(\alpha)|\bigr).
\]

The verifier checks all \(3^{15}=14,348,907\) partial assignments. Exactly 939,975 are bilateral, and their minimum difference is one. Hence \(i(G)=15+1=16\).

The raw-graph proof tree and bilateral enumeration are independent exact routes. Together with the witness,

\[
\boxed{i(G)=16}.
\]

# 5. Corrected order-50 threshold

Let a cubic graph have a dominating induced matching \(M\). Orient each matching edge and use a Boolean variable to select one endpoint. Each unmatched vertex gives a domination clause. Each endpoint has exactly two neighbours outside \(M\), so each positive literal and each negative literal occurs at most twice. Non-tautological clauses use three distinct variables. The endpoint formula is therefore \((3,2,2)\)-CNF, not merely \((3,4)\)-CNF.

Zhang, Peitl and Szeider show that an unsatisfiable \((3,2,2)\)-formula needs at least 20 clauses [@zhang2024]. A cubic graph with a dominating induced matching has \(2n/5\) unmatched vertices. If \(n<50\), the endpoint formula has fewer than 20 clauses and is satisfiable. Selecting one endpoint per matching edge then produces an independent dominating set of size \(|M|=\mu^*(G)\).

Thus every cubic graph in this class below order 50 satisfies the conjectured inequality. The displayed graph has order 50 and a dominating induced matching, so the threshold is sharp within this class. Global order-50 minimality is not claimed.

# 6. Antecedents, independent replay and scope

Related SAT-to-independent-domination graph constructions are established in the satgraph literature [@zverovich2006]. Ahadi and Dehghan study the same exact twice-positive/twice-negative formula class for hardness reductions [@ahadi2019]. The full manuscript therefore presents the bilateral-deficiency identity as an apparently new formulation after a bounded search, not as a secured priority claim.

Fable independently authenticated the `v2-theorem` predecessor and re-derived the exact identity, twice-occurrence theorem and order-50 threshold. It also brute-forced the complete formula facts and checked the simple witness. Its receipt applies to archive SHA-256 `106787...a589`, not byte-for-byte to this merged v3 release. The full scope is preserved in `INDEPENDENT_REPLAY_FABLE.md`.

The mathematical verdict is exact:

\[
\boxed{i(G)=16>15=\mu^*(G)}.
\]

# References
