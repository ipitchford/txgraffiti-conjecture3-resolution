# Full review

**Manuscript:** *A 50-vertex cubic counterexample to independent domination versus minimum maximal matching*
**Package:** release candidate v3
**Review date:** 6 August 2026
**Editorial recommendation:** **Major revisions before Evidence Press release**
**Confidence:** **0.92**

## 1. Executive assessment

This certificate-backed theoretical and computational manuscript presents a connected cubic graph on 50 vertices for which the independent domination number is (i(G)=16), while the minimum cardinality of a maximal matching is (\mu^*(G)=15). Subject to the definitions stated in the manuscript, this is a valid counterexample to the TxGraffiti conjecture that (i(G)\leq \mu^*(G)) for every positive-degree regular graph. The package also develops an exact correspondence between independent domination in a clause–literal graph and a new partial-assignment deficiency parameter, derives (\mu^*(G)=k) for a balanced twice-positive/twice-negative formula construction, and gives a sharp order threshold within the subclass of cubic graphs possessing a dominating induced matching.

The strongest feature is the unusually strong internal evidentiary architecture. The graph, formula, witnesses, direct proof-tree certificate, exhaustive formula route, independent mixed-integer models, mutation tests and provenance records agree. I found no fatal mathematical defect, and all bundled deterministic checks passed in a fresh execution.

The decisive weaknesses concern release status rather than the core counterexample: the exact v3 package has not been independently reproduced; a predecessor-scoped AI receipt is too easily overread; the execution environment is recorded but not pinned; one theorem depends on an external SAT lower bound; and the novelty discussion does not yet confront the closest SAT-to-independent-domination antecedents in sufficient detail. These are substantial but feasible repairs. **Major revisions** is therefore a release-hardening recommendation, not a demand for conventional journal peer review or a redesign of the mathematical result.

## 2. Scope and evidence limits

### Manuscript type and intended audience

This is a **theoretical graph theory paper with a computer-assisted finite certificate**, supported by a Boolean satisfiability construction and exact optimisation checks. Its primary audience is researchers in graph domination, matching theory and extremal graph theory, with a secondary audience in satisfiability, computational proof and reproducible mathematics.

### Materials inspected

I inspected:

* the seven-page main manuscript;
* the four-page counterexample note and four-page audit/solution document;
* the indexed conjunctive normal form formula and its graph encodings;
* the edge list, JSON representation and graph6 representation;
* the stated maximal matching and independent dominating-set witnesses;
* the direct lower-bound proof tree and checker;
* the exhaustive partial-assignment route;
* the mixed-integer optimisation scripts;
* mutation tests, receipts, provenance documents and version history;
* the supplied Research Excellence Framework calibration image;
* the Evidence Press website and the external literature described in Section 6.

The archive SHA-256 value is

`94fe632a280d0ca8d6d06ec3cf2309d07973acdac0c43c53e21c3d4191903e8f`.

It agrees with the supplied sidecar. All 32 files listed in the internal checksum manifest passed verification. The three PDFs rendered cleanly without visible clipping, overlap or missing glyphs.

### Review standard

No journal-specific criteria were supplied. I therefore applied:

1. mathematical correctness and completeness;
2. consistency between prose, certificates, code and raw graph data;
3. reproducibility and assurance proportional to a computer-assisted theorem;
4. accurate novelty and dependency positioning;
5. Evidence Press’s distinction between internal replay, independent reproduction, formal verification and peer review. Evidence Press presents itself as an evidence layer rather than a substitute for a journal and explicitly distinguishes several assurance states rather than treating verification as a single binary property. ([Evidence Press][1])

The user’s context—that these are release candidates rather than journal-ready papers—has been taken into account. I have not treated the absence of conventional peer review or final typesetting as a defect in itself.

### Evidence classes used in this report

* **Manuscript evidence** means the supplied text, raw graph, code, certificates and receipts.
* **External evidence** means sources opened during the live literature and standards check.
* **Reviewer inference** means my mathematical or editorial judgement based on those materials.

### Material limitations

The following were not available or not established:

* no clean-room rerun or reimplementation of the exact v3 archive by an independent party;
* no formal proof-assistant verification;
* no pinned or containerised execution environment;
* no immutable repository release or archival digital object identifier for this exact package;
* no exhaustive MathSciNet, zbMATH Open, Scopus or Web of Science search;
* no complete full-text comparison with every earlier “satgraph” result;
* no evidence supporting unrestricted minimality among all cubic counterexamples;
* no conventional specialist peer-review report.

These are **not reported or not established**, rather than presumed not to have been done elsewhere.

## 3. Contribution and positioning

### 3.1 Strongest defensible thesis

The strongest defensible central claim is:

> There exists a connected cubic graph (G) of order 50 such that
> [
> \mu^*(G)=15<16=i(G),
> ]
> and therefore the proposed inequality (i(G)\leq\mu^*(G)) for positive-degree regular graphs is false.

The conjecture is stated in the recent TxGraffiti overview as applying to every (r)-regular graph with (r>0). ([arXiv][2])

The manuscript does **not** establish that 50 is the smallest possible order among all cubic counterexamples. It is careful not to claim this, and that restraint should be retained.

### 3.2 Claim-to-evidence map

| Claim                                                                             | Principal manuscript evidence                                          | Assessment                                                                          |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| The supplied graph is simple, connected, cubic and has 50 vertices                | Section 4; JSON, edge list and graph6 encodings; replay output         | Established                                                                         |
| (\mu^*(G)\leq15)                                                                  | Explicit 15-edge maximal matching, Proposition 4                       | Established directly                                                                |
| (\mu^*(G)\geq15)                                                                  | Cubic edge-domination count, Proposition 4                             | Established directly                                                                |
| (i(G)\leq16)                                                                      | Explicit 16-vertex independent dominating set, Proposition 5           | Established directly                                                                |
| (i(G)\geq16)                                                                      | Direct proof-tree certificate and independent formula/deficiency route | Established with strong computational support                                       |
| The graph refutes the conjecture                                                  | Combination of the preceding exact values                              | Established                                                                         |
| (i(G(F))=k+\beta(F)) for the indexed formula construction                         | Theorem 1, Section 2                                                   | Proof appears correct                                                               |
| Balanced exact twice-occurrence proper 3-CNF gives a cubic graph with (\mu^*=k)   | Theorem 2, Section 2                                                   | Proof appears correct; terminology needs definition                                 |
| Cubic dominating-induced-matching graphs of order below 50 satisfy the inequality | Theorem 3, Section 3                                                   | Correct conditional on the cited 20-clause SAT result and exact definition matching |
| The exact identity and synthesis are novel                                        | Section 8 and search receipt                                           | Plausible, but not yet demonstrated adequately                                      |

### 3.3 Originality

The **specific 50-vertex counterexample and its exact certification** appear to be a meaningful contribution. The same graph is already present in the public repository associated with the package, so an Evidence Press release would consolidate and audit the evidence rather than constitute the first public appearance of the construction. ([GitHub][3])

The exact identity
[
i(G(F))=k+\beta(F)
]
is potentially the most conceptually reusable result. However, its novelty requires a stronger comparison with earlier SAT-to-independent-domination work. Zverovich established a linear-time equivalence between satisfiability and independent domination for corresponding satgraphs, while Zhang, Peitl and Szeider explicitly use the same literal-pair/clause-incidence graph architecture to represent conjunctive normal form formulas. ([ScienceDirect][4])

This does not show that the manuscript’s deficiency identity is already known. It does show that the **graph transformation itself cannot be presented as new without qualification**.

### 3.4 Significance

Resolving a concise named conjecture by an explicit small counterexample is significant within its specialised area. The result also has methodological value because it joins:

* a compact graph witness;
* a direct parameter certificate;
* a second lower-bound route through satisfiability;
* mutation-tested checkers;
* explicit provenance.

The conceptual significance would increase if the deficiency identity were shown to yield a wider family of counterexamples, a useful algorithm, or a structural characterisation. At present, the central impact is the refutation itself, not yet a broad new theory.

## 4. Major comments

### 1. Assurance labels do not yet distinguish the exact v3 package from predecessor-scoped checking

**Classification: Major**

**Issue**

The package contains accurate caveats, but the combination of “certificate-backed”, “VERIFIED”, independent-agent language and several overlapping receipts can still be read as saying that the exact v3 release has been independently reproduced. That has not been established.

**Manuscript evidence**

* The Status material states that this is not journal peer review.
* Section 7 describes deterministic local replay and a scoped independent AI-agent analysis.
* The Fable receipt applies to a byte-distinct predecessor labelled `v2-theorem`, identified by a different SHA-256 value beginning `106787` and ending `a589`.
* That receipt reports an independent harness and re-derivation, not execution of the present v3 archive.
* The exact v3 proof tree and complete replay were executed locally in this review, but that remains an internal rerun from the perspective of the proposed release.

**Why it matters**

Evidence Press distinguishes internally replayed work from independent rerun, independent reimplementation, formal verification and peer review. Its machine-readable guidance also treats these as separate booleans or assurance dimensions. ([Evidence Press][1])

A mathematically correct release can still be misleading if a reader cannot tell which exact bytes were independently tested. The problem is one of scope and identity, not evidence quality.

**Required revision or decisive test**

For the exact release object, publish an assurance record along the following lines:

| Field                            | Recommended v3 state                       |
| -------------------------------- | ------------------------------------------ |
| `status`                         | `unrefereed-candidate`                     |
| `peerReviewed`                   | `false`                                    |
| `internallyReplayed`             | `true`                                     |
| `independentlyRerun`             | `false`                                    |
| `independentlyReimplemented`     | `false` for exact v3                       |
| `formallyVerified`               | `false`                                    |
| `predecessorIndependentAnalysis` | `partial`, with predecessor hash and scope |
| `environmentPinned`              | `false` until repaired                     |

Replace unqualified “VERIFIED” with a scoped formulation such as **“all bundled deterministic checks passed in the recorded environment”**. Retain the Fable receipt, but place it under a clearly labelled predecessor-evidence heading.

A decisive upgrade would be a clean-room reimplementation against the exact v3 graph and certificate, performed from the mathematical specification rather than by invoking the bundled checker.

---

### 2. The closest prior art is materially closer than the current novelty discussion conveys

**Classification: Major**

**Issue**

The manuscript’s bounded novelty search did not identify an exact collision, but it does not yet provide the direct theorem-by-theorem comparison needed to support the originality of the clause–literal construction and the identity in Theorem 1.

**Manuscript evidence**

Section 8 reports a scoped search and appropriately avoids an absolute priority claim. The construction in Section 2 uses:

* one vertex for each positive and negative literal;
* an edge joining complementary literals;
* one vertex for each clause;
* incidence edges joining clauses to their literals.

**External evidence**

Zhang, Peitl and Szeider define a “clause-literal graph” with precisely these vertex blocks and edge types. Their paper displays the construction explicitly and uses it for symmetry-aware formula generation. 

Zverovich’s *Satgraphs and independent domination. Part 1* reports that satisfiability is linear-time equivalent to finding the independent domination number in a corresponding satgraph. I verified the publisher/abstract record, but did not complete a line-by-line full-text comparison of every theorem in that paper. ([ScienceDirect][4])

Ahadi and Dehghan study the balanced twice-positive/twice-negative three-clause occurrence class and applications to independent domination. Their ((2/2/3))-SAT definition allows a clause with at least two distinct variables, whereas the present cubic construction appears to require exactly three distinct, non-tautological literals. ([arXiv][5])

**Why it matters**

The central counterexample may remain valid regardless of this literature. The originality rating of the general identity, construction and reduction does not.

The relevant distinction is:

* **apparently new:** the exact deficiency formula, its bilateral partial-assignment interpretation, and its use in this counterexample;
* **not new as presently framed:** the basic literal-pair/clause-incidence graph architecture;
* **not yet determined:** whether an earlier satgraph theorem is equivalent to the claimed identity after a change of notation.

**Required revision or decisive test**

Add a prior-art comparison table containing at least:

| Present result | Zverovich 2006 | Ahadi–Dehghan 2019 | Zhang–Peitl–Szeider 2024 | Claimed difference |
| -------------- | -------------- | ------------------ | ------------------------ | ------------------ |

The comparison must address definitions, graph construction, objective value, allowed clause types, direction of reduction and whether an exact optimisation identity is proved.

Search MathSciNet or zbMATH Open using formula-graph terminology, “satgraph”, “independent domination”, “minimum maximal independent set”, “clause-literal graph” and partial assignments. Until that is complete, replace categorical novelty language with:

> “We prove the following exact identity; our targeted search did not locate an equivalent published statement.”

The decisive test is whether any earlier theorem can be translated into
[
i(G(F))=k+\min_\alpha\bigl(|T(\alpha)|-|U(\alpha)|\bigr)
]
with the same admissibility condition on (\alpha). If so, the manuscript should cite and specialise it rather than claim the identity as new.

---

### 3. The order-threshold theorem relies on an external SAT result whose definitions and assurance are not integrated into the release

**Classification: Major**

**Issue**

Theorem 3 uses the result that an unsatisfiable ((3,2,2))-formula requires at least 20 clauses. The result is cited, but the release does not make the dependency sufficiently explicit in its claim and assurance structure.

**Manuscript evidence**

Section 3 constructs a formula from a cubic graph with a dominating induced matching, simplifies tautological or duplicate occurrences, and invokes the 20-clause threshold to infer satisfiability below order 50.

**External evidence**

Zhang, Peitl and Szeider define a (k)-clause as containing exactly (k) literals and report 20 as the smallest number of clauses for an unsatisfiable ((3,2,2))-formula. Their Table 1 records the value 20 in the (p=2,q=2) entry. 

**Why it matters**

Theorem 3 is not merely supported by a general background citation: its numerical boundary is inherited directly from an externally established computational result. A change in formula convention—for example, repeated variables, tautologies, “at most three” rather than “exactly three”, or signed occurrence bounds—could invalidate the transfer.

This does not threaten the 50-vertex counterexample, which has self-contained parameter certificates. It affects the structural sharpness claim.

**Required revision or decisive test**

State Theorem 3 explicitly as conditional on the cited theorem, including the exact source notation and a short definition-matching lemma. The proof should say why the derived clauses are:

1. non-tautological after simplification;
2. composed of exactly three distinct literals;
3. bounded by two positive and two negative occurrences per variable;
4. unchanged in satisfiability by the specified simplifications.

Add the external result to the machine-readable dependency graph with DOI, version and access date. Where licensing permits, pin the upstream artefact or at least record a content hash for the consulted version.

An independent reconstruction of the 20-clause threshold would strengthen the release but is not necessary for the central disproof. If the definition match cannot be made exact, remove or weaken Theorem 3 rather than weakening the main counterexample.

---

### 4. The execution environment is recorded but not reproducibly pinned

**Classification: Major**

**Issue**

The replay receipt records software versions, but the package does not contain a lockfile, container, declarative environment or continuous-integration recipe sufficient to recreate those versions reliably.

**Manuscript evidence**

The successful environment used:

* Python 3.13.5;
* C++ 14.2.0;
* NumPy 2.3.5;
* SciPy 1.17.0.

The replay was deterministic in this environment. Certificate regeneration was byte-identical.

**Why it matters**

Recording an environment is not the same as reconstructing it. Package-resolution changes, solver changes and compiler defaults could eventually prevent the supplementary optimisation checks or alter their logs.

The theorem-critical distinction also needs to be clearer:

* the direct certificate and its checker are part of the principal proof;
* the exhaustive deficiency route is a second exact proof route;
* the SciPy/HiGHS mixed-integer programmes are corroborative rather than logically necessary.

Evidence Press itself recommends pinned environments and explicit treatment of external dependencies. ([Evidence Press][1])

**Required revision or decisive test**

Provide at least one of:

* an OCI/Docker container;
* a Nix flake;
* a `uv.lock` or equivalent Python lock plus exact compiler image;
* a reproducible workflow on a named long-term-support distribution.

Record compiler flags, solver options, random seeds and locale. Run the complete verification in a fresh environment through continuous integration and archive the resulting receipt.

The decisive test is a successful clean build and complete replay from only the immutable release plus the declared environment definition.

---

### 5. The release needs a clearer canonical interface and tighter mathematical terminology

**Classification: Major for an Evidence Press release; mostly minor for the underlying theorem**

**Issue**

The package is rich but fragmented. Several documents repeat or qualify similar claims, while expected canonical entry points are absent or named differently. A few undefined or ambiguous phrases can also change the apparent mathematical scope.

**Manuscript evidence**

* There are separate manuscript, note, audit, adversarial and receipt documents.
* “Proper 3-CNF” is used but not formally defined.
* The abstract refers to “every nontrivial regular graph”.
* The proof tree is described as 21,803 bytes without immediately saying that this is the compressed size.
* “VERIFIED” and “sharp” appear in contexts where the intended scope must be reconstructed from other files.
* No licence file was identified.

**Why it matters**

A release intended for both humans and automated agents should not require readers to infer the canonical claim or assurance state from several partially overlapping narratives. Ambiguity over “proper” is particularly important because degree three depends on exact clause structure.

The conjecture’s published formulation is for (r)-regular graphs with (r>0), not the potentially ambiguous class “nontrivial regular graphs”. ([arXiv][2])

**Required revision or decisive test**

Create a canonical root-level interface, preferably including:

* `AI_INDEX.md`;
* `STATUS.md`;
* `ASSURANCE.md`;
* `PROVENANCE.md`;
* `SOURCES.md`;
* `CLAIMS.json` or an equivalent claim map;
* `MANIFEST.sha256`;
* `LICENSE`.

Designate one PDF as the canonical paper and one document as the evidence supplement. Other documents should state whether they are historical, explanatory or machine-facing.

Define “proper 3-CNF” explicitly as used here—for example, clauses consisting of exactly three distinct literals on three distinct variables, with no complementary pair—if that is the intended definition.

## 5. Rigour, results and inference

### 5.1 Package integrity and deterministic replay

The complete bundled replay exited successfully. It established internal agreement among the formula, JSON, edge list and graph6 representations. It also regenerated the principal certificate byte-for-byte.

Four deliberately corrupted certificates were rejected:

1. an invalid bound or leaf;
2. a malformed witness;
3. a truncated certificate;
4. a certificate with trailing data.

These tests provide useful evidence that the checker is not merely accepting every input. They are targeted mutation tests, not exhaustive fuzzing or formal verification.

The archive sidecar and internal manifest establish integrity relative to the supplied package. As both were supplied by the same source, they should not by themselves be described as independent provenance.

### 5.2 Direct graph checks

I independently parsed the raw graph rather than relying only on the packaged summary. The following properties held:

* (n=50);
* (m=75);
* every vertex has degree three;
* the graph is simple and connected;
* the reported girth is five;
* the stated 15-edge set is a matching;
* the matching is maximal;
* the stated 16-vertex set is independent;
* the same set dominates every vertex.

The displayed independent dominating set is
[
{0,3,5,6,8,10,12,14,16,18,20,22,24,26,28,47}.
]

The elementary consistency check
[
|E(G)|=\frac{3|V(G)|}{2}=\frac{3\cdot50}{2}=75
]
agrees with the raw encoding.

### 5.3 Exact value of the minimum maximal matching

The upper bound follows from the explicit maximal matching of size 15.

For the lower bound, every maximal matching is an edge-dominating matching: every edge outside it shares an endpoint with a matched edge. In a cubic graph, one matched edge can account for at most:

* itself; and
* four other incident edges, two at each endpoint.

Thus it dominates at most five edges. Since the graph has 75 edges,
[
|M|\geq \left\lceil\frac{75}{5}\right\rceil=15.
]
Together with the witness,
[
\mu^*(G)=15.
]

The equality (15\cdot5=75) also shows that the stated matching meets the counting bound exactly.

This part of the disproof is elementary and does not depend on an optimiser.

### 5.4 Exact value of the independent domination number

#### Upper bound

The explicit 16-vertex set was independently checked to be both independent and dominating, so
[
i(G)\leq16.
]

#### Lower-bound route A: direct proof tree

The direct certificate reports:

* 256,714 nodes;
* 116,229 branch nodes;
* 140,485 bound leaves;
* maximum depth 15.

The node accounting is exact:
[
116{,}229+140{,}485=256{,}714.
]

The checker accepted every node in the original tree and rejected the hostile mutations. The certificate is 21,803 bytes in compressed form and 848,888 bytes as uncompressed text.

This gives strong machine-checkable evidence that no independent dominating set of size at most 15 exists. Its remaining trust base consists of the checker, parser, certificate-generation assumptions and ordinary machine execution.

#### Lower-bound route B: formula identity and exhaustive partial assignments

The graph comes from an indexed formula with 15 variables and 20 clauses. Each positive and negative literal occurs exactly twice.

Theorem 1 claims
[
i(G(F))=k+\beta(F),
]
where (\beta(F)) is the minimum of
[
|T(\alpha)|-|U(\alpha)|
]
over bilateral partial assignments (\alpha).

The manuscript’s proof is sound in outline:

* From a bilateral partial assignment, select the literal corresponding to every assigned variable and select each residual unsatisfied clause vertex. Independence follows because no selected literal occurs in a selected residual clause. Domination of both literal vertices for every unassigned variable follows from the bilateral condition.
* Conversely, the selected literal vertices of an independent dominating set define a partial assignment. Every clause left unsatisfied by those selected literals must itself be selected, while a satisfied clause cannot be selected because it is adjacent to a selected literal. If neither literal of a variable is selected, both literal vertices must be dominated by selected clauses, requiring residual occurrences of both signs.

The cardinality is then
[
(k-|U(\alpha)|)+|T(\alpha)|
=k+\bigl(|T(\alpha)|-|U(\alpha)|\bigr).
]

The bundled enumeration covered all
[
3^{15}=14{,}348{,}907
]
partial assignments. It found 939,975 bilateral assignments, minimum deficiency (\beta=1), and no violation of the claimed correspondence. Therefore
[
i(G)=15+1=16.
]

As an additional reviewer check, I implemented the identity separately and tested:

* 4,369 exhaustive formula sequences for two variables and at most three clauses;
* 4,161 exhaustive formula sequences for three variables and at most two clauses;
* 1,250 random small indexed formulas;
* explicit edge cases including no variables, empty clauses, tautologies, absent variables and one-sided literal occurrence.

All 9,780 checks agreed with the identity. These computations corroborate the proof but do not replace it with a formal derivation.

#### Orthogonal optimisation checks

Two mixed-integer formulations returned:

* independent domination optimum 16;
* minimum maximal matching optimum 15;
* zero reported optimality gap.

These are useful independent model formulations. They are corroborative because they rely on the same input graph and on the solver implementation; the proof does not need them once the direct witnesses and lower-bound certificates are accepted.

### 5.5 Formula-level checks

The complete truth table covered
[
2^{15}=32{,}768
]
total assignments.

It found:

* no satisfying assignment;
* minimum one unsatisfied clause;
* 3,318 assignments attaining that minimum;
* every one-clause deletion satisfiable;
* the named assignment falsifying only clause (C_{18}).

Thus the formula is minimally unsatisfiable as represented. These facts explain the size-16 witness and the one-unit deficiency, although minimal unsatisfiability alone is not the proof of (i(G)=16).

### 5.6 Audit of the general theorems

#### Theorem 1

No logical gap was found. The use of indexed clauses and literal sets should nevertheless be made explicit because duplicate clauses or repeated literal positions can otherwise change the associated graph.

#### Theorem 2

For each variable:

* the positive literal vertex has one complementary-pair edge and two incidence edges;
* the negative literal vertex has the same;
* every clause vertex has three incidence edges.

The graph is therefore cubic under the intended “proper” clause convention.

There are (k) complementary-pair edges and (4k) incidence edges, hence (5k) edges. The complementary-pair matching has size (k) and is maximal. Any maximal matching in a cubic graph dominates at most five edges per member, so it has size at least (5k/5=k). Therefore (\mu^*=k).

This proof is correct. Its presentation should state why “proper” rules out a clause incidence that would reduce the degree or create duplicate edges.

#### Theorem 3

For a cubic graph with a dominating induced matching (M) of size (t), let (W) be the unmatched vertices. Since (W) is independent:

* each edge of (M) has four incident edges leading to (W);
* every vertex of (W) has all three incident edges leading to endpoints of (M).

Thus
[
4t=3|W|,
\qquad
|V(G)|=2t+|W|=\frac{10t}{3},
]
so
[
t=\frac{3|V(G)|}{10},
\qquad
|W|=\frac{2|V(G)|}{5}.
]

Below order 50, the resulting formula has fewer than 20 clause vertices. The remaining step is valid if the formula lies exactly in Zhang et al.’s ((3,2,2)) class. The theorem is therefore credible but externally conditional, as discussed in Major Comment 3.

### 5.7 Internal consistency

No discrepancy was found between the principal representations or numerical summaries:

| Check                              |                    Result |
| ---------------------------------- | ------------------------: |
| (50\cdot3/2)                       |                  75 edges |
| Pair edges plus literal incidences |                (15+60=75) |
| Matching edge capacity             |             (15\cdot5=75) |
| Total assignments                  |           (2^{15}=32,768) |
| Partial assignments                |       (3^{15}=14,348,907) |
| Proof-tree node total              | (116,229+140,485=256,714) |
| Parameter gap                      |                 (16-15=1) |

### 5.8 Results and inference

The evidence directly establishes the existence of the counterexample, conditional only on ordinary trust in the supplied finite proof machinery and the manually checkable bridge theorems.

It does **not** directly establish:

* that the graph is the smallest cubic counterexample;
* that the graph is unique at order 50;
* that the deficiency identity is unprecedented;
* that the exact v3 archive has been independently reproduced;
* that the full package is formally verified.

No statistical multiplicity, (p)-value interpretation or sampling issue applies. Analytic flexibility in the discovery process would matter for claims of priority, smallest order or search completeness, but it does not weaken an exact counterexample once independently checked. The manuscript’s avoidance of an unrestricted minimality or discovery-priority claim is therefore appropriate.

### 5.9 Recommended assurance matrix

| Assurance dimension           | Recommended state         | Basis                                                                   |
| ----------------------------- | ------------------------- | ----------------------------------------------------------------------- |
| Archival availability         | Not assessed              | No immutable final release inspected                                    |
| Internal deterministic replay | Passed                    | Full v3 replay passed                                                   |
| Independent rerun of exact v3 | Not assessed              | No external exact-v3 execution receipt                                  |
| Independent reimplementation  | Partial, predecessor only | Fable receipt concerns a byte-distinct predecessor                      |
| Formal verification           | Not assessed              | No proof-assistant artefact                                             |
| Specialist review             | Not assessed              | This report should not be represented as conventional human peer review |
| Editorial peer review         | Not assessed              | None claimed                                                            |
| Environment reproducibility   | Partial                   | Versions recorded, environment not pinned                               |

## 6. External literature check

### 6.1 Search record

**Review date:** 6 August 2026.

**Resources searched:** general live web search; publisher and DOI landing pages; arXiv; Discrete Mathematics & Theoretical Computer Science; Dagstuhl/LIPIcs; CORE/Rutgers-indexed material; GitHub; Evidence Press; and official Research Excellence Framework pages.

**Representative search strings:**

* `"independent domination" "minimum maximal matching" regular graph`
* `"TxGraffiti Conjecture 3"`
* `"i(G) <= mu*(G)" cubic graph`
* `satgraph independent domination CNF`
* `"clause-literal graph" independent domination`
* `"(3,2,2)" smallest unsatisfiable 20 clauses`
* `"bilateral deficiency" SAT graph`
* `"twice positive" "twice negative" independent domination`

**Inclusion logic:** I prioritised the original or recent formal statement of the conjecture, direct SAT-to-independent-domination antecedents, balanced occurrence SAT results, the external 20-clause threshold, and the public repository containing the present graph. Older papers were retained where they are direct conceptual antecedents.

This was a **targeted, not exhaustive** search. I did not have subscription-index access to every specialist database. The Zverovich comparison was based on publisher metadata and an accessible detailed abstract/search extract rather than a complete theorem-by-theorem reading of the final typeset article.

### 6.2 Pivotal publications and direct comparison

| Source                                  | Decision-relevant content                                                                                                  | Implication                                                                                                           |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Caro, Davila and Pepper (2022)          | Earlier source for the relevant TxGraffiti line of conjectures and matching/independence relations                         | Establishes the conjectural context; should be cited with verified DOI                                                |
| Davila, Brimkov and Pepper (2025)       | States TxGraffiti Conjecture 3 as (i(G)\leq\mu^*(G)) for (r)-regular (G), (r>0)                                            | Confirms that the present graph refutes the stated conjecture ([arXiv][2])                                            |
| Zverovich (2006)                        | Defines satgraphs and reports a linear-time equivalence between SAT and independent domination in the corresponding graph  | Makes a full-text novelty comparison essential for Theorem 1 ([ScienceDirect][4])                                     |
| Ahadi and Dehghan (2019)                | Studies balanced twice-positive/twice-negative three-clause occurrence SAT and independent-domination applications         | Close antecedent for the occurrence-restricted construction, though its clause convention is broader ([arXiv][5])     |
| Zhang, Peitl and Szeider (2024)         | Defines the same clause–literal graph architecture and establishes 20 as the smallest unsatisfiable ((3,2,2))-formula size | Requires direct citation at the construction and underpins Theorem 3                                                  |
| Public counterexample repository (2026) | Contains the same graph and describes it as computationally rigorous but not peer reviewed                                 | The Evidence Press object is an audited release of an already public construction, not first disclosure ([GitHub][3]) |

### 6.3 Important omissions and contradictions

1. **The clause–literal graph construction has a clear prior antecedent.** The manuscript should cite Zhang et al. where it defines the graph, not only where it uses the 20-clause threshold.

2. **The exact identity may still be original.** I found no source in the targeted search stating the bilateral-deficiency formula. That negative search result is not proof of priority.

3. **The occurrence terminology differs across sources.** Ahadi and Dehghan’s ((2/2/3))-SAT permits clauses containing at least two distinct variables, whereas Zhang et al.’s (3)-clauses contain exactly three literals. The manuscript should not treat these conventions as interchangeable.

4. **No competing published counterexample was located.** The public repository already contains this graph, but I did not locate a separate peer-reviewed paper independently reporting the same 50-vertex counterexample.

5. **Global minimality remains open on the inspected evidence.** The dominating-induced-matching threshold does not prove that every cubic counterexample has at least 50 vertices.

### 6.4 Implications for credibility and originality

**Credibility:** strengthened. The relevant external SAT threshold and occurrence classes exist and are consistent with the manuscript’s strategy, subject to exact definition matching.

**Originality:** provisionally strong for the concrete counterexample and potentially strong for the exact identity, but weaker for the underlying graph transformation.

**Significance:** unaffected by the construction antecedent. An explicit disproof remains a substantive result even when built from known machinery.

## 7. Minor comments

1. Define (\mu^*(G)) once as the minimum cardinality of a maximal matching and mention “saturation number” as an alternative name only if useful.

2. Replace “every nontrivial regular graph” with “every positive-degree regular graph” or the exact formulation “every (r)-regular graph with (r>0)”.

3. Define “proper 3-CNF” before Theorem 2. Specify distinctness of literals and variables, exclusion of tautologies, and treatment of repeated clauses.

4. Clarify that clauses are indexed. Two extensionally equal clauses may correspond to distinct clause vertices if the construction treats occurrences as distinct.

5. At the first mention of the 21,803-byte proof tree, say **“21,803-byte gzip-compressed certificate”**.

6. In Proposition 4, include the one-sentence explanation that a maximal matching is edge-dominating and a matched edge in a cubic graph can dominate at most five edges.

7. In Theorem 3, distinguish simplification of the derived formula from alteration of the original graph. “Deleting a duplicate literal” and “deleting a clause vertex” are not interchangeable operations.

8. Qualify “sharp” as **“sharp at the order boundary within the dominating-induced-matching subclass”**. It does not establish unrestricted order minimality.

9. Replace generic “verified” badges in human-facing documents with the exact assurance operation and object hash.

10. State explicitly that byte-identical regeneration demonstrates deterministic internal reproducibility, not independence.

11. Describe the four mutation tests as representative targeted mutations. Do not imply complete checker validation.

12. Separate theorem-critical scripts from optional corroborative scripts in the run instructions. The principal replay should not fail merely because SciPy is unavailable unless the optimisation checks are intentionally mandatory.

13. Put the two lower-bound routes side by side in the main paper. Their independence is a major strength and should not be buried in the audit documents.

14. Include a small schematic of the formula-to-graph construction showing one complementary literal pair, clause vertices and incidence edges.

15. Add a concise plain-language explanation of why formula unsatisfiability alone does not automatically give (i(G)=k+1); the bilateral condition is the key extra point.

16. Include the exact hashes of the canonical manuscript, raw graph and principal certificate in the main status document.

17. Use immutable semantic release labels. The repeated use of “v2” for byte-distinct objects is reconstructible from hashes but unnecessarily confusing.

18. Add an explicit licence for prose, code and data. Evidence Press currently presents releases as reusable evidence objects, so uncertainty over reuse terms is avoidable. ([Evidence Press][1])

19. Distinguish source contributions, AI-assisted derivations, human editorial decisions and independently rerun outputs in the contributor/provenance statement.

20. Verify that the Caro–Davila–Pepper journal DOI is recorded as `10.7151/dmgt.2317`.

## 8. Prioritised revision plan

### Must fix before the claims are publishable as an Evidence Press release

1. Publish exact v3 assurance booleans and remove any implication of independent reproduction of the current bytes.

2. Scope the predecessor AI receipt explicitly by version and hash.

3. Add a direct prior-art comparison covering Zverovich, Ahadi–Dehghan and Zhang–Peitl–Szeider.

4. Cite the pre-existing clause–literal graph construction at the point of use.

5. Define “proper 3-CNF” and verify the definition transfer in Theorem 3.

6. Represent the 20-clause result as a pinned external dependency.

7. Supply a reproducible, pinned execution environment.

8. Create a canonical status, assurance, provenance, source and claim-index interface.

9. Add an explicit licence and immutable release identifier.

### Should fix to strengthen the paper

1. Consolidate the mathematical narrative into one canonical manuscript plus one evidence supplement.

2. Present the direct certificate route and the formula route as co-equal lower-bound proofs.

3. Add a diagram of the construction and a short claim-to-evidence table.

4. Explain the matching lower bound and the bilateral condition more explicitly.

5. Run continuous integration from a clean environment and publish its receipt.

6. Conduct one exact-v3 clean-room reimplementation by a party or agent that does not invoke the bundled checker.

7. Have a graph theorist or SAT specialist check the novelty comparison and the definition mapping for Theorem 3.

### Could improve presentation or future work

1. Formalise Theorem 1 and the 50-vertex graph certificate in Lean, Isabelle or another proof assistant.

2. Search systematically for smaller counterexamples outside the dominating-induced-matching subclass.

3. Determine whether the formula construction produces an infinite counterexample family.

4. Analyse uniqueness or multiplicity of order-50 examples without implying that such analysis is required for the present disproof.

5. Develop a smaller formally checkable lower-bound certificate or independently verified checker implementation.

## 9. Editorial recommendation

### Recommendation: **Major revisions**

**Confidence:** **0.92**

No fatal concern was identified. The central graph and its two exact parameter values survived:

* raw-data reconstruction;
* elementary hand checks;
* direct certificate replay;
* exhaustive partial-assignment enumeration;
* independent small-instance testing of the bridge identity;
* two separate optimisation formulations;
* adversarial certificate mutations.

The manuscript is therefore substantially stronger than a bare computational counterexample.

The recommendation is nevertheless **major revisions** because Evidence Press’s principal editorial value lies in trustworthy assurance and provenance. The present package risks conflating an internally replayed exact release with predecessor-scoped independent analysis, and its novelty account does not yet engage sufficiently with the closest graph-construction antecedents. A pinned environment and exact external-dependency map are also needed for a durable evidence object.

This recommendation could move to **minor revisions or release approval** after:

* exact-v3 assurance fields are corrected;
* the environment is pinned and replayed cleanly;
* the literature comparison is completed;
* Theorem 3’s dependency is mapped precisely;
* the canonical release interface is simplified.

Discovery of a prior equivalent to Theorem 1 would require narrowing the originality claim, but would not invalidate the counterexample. Failure of an independently implemented exact-v3 checker, or discovery that the raw graph does not have the certified parameter values, would change the recommendation to **reject**. I found no indication of either problem.

## 10. Provisional REF calibration

### Applicable framework

The most relevant unit is **Unit of Assessment 10: Mathematical Sciences**, with a possible secondary connection to Unit 11 because of the computational certificate. The mathematical theorem, rather than software engineering, is the primary output. The official REF 2029 unit structure includes these separate units. ([REF 2029][6])

Final REF 2029 panel-specific output criteria are not yet a stable basis for a definitive rating; current Contributions to Knowledge and Understanding guidance remains subject to the evolving REF 2029 framework. ([REF 2029][7]) I therefore use the REF 2021 Main Panel B definitions as the closest available calibration proxy. Those definitions assess originality, significance and rigour, with 4* associated with agenda-setting or forefront work and 3* with important contributions at an international standard. 

The numerical 0–12 overlay below is the scale supplied with the review brief. It is **not an official REF scale**.

| Dimension                  |    Provisional rating | Rationale                                                                                                                                                                                                                                                                                                                                                              | Confidence |
| -------------------------- | --------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------: |
| **Originality**            |    **3* high — 9/12** | The explicit disproof and bilateral-deficiency identity appear to make an important contribution. The rating is held below 4* because the graph architecture has clear antecedents, the same graph is already public, and exact priority for Theorem 1 remains incompletely checked.                                                                                   |       0.70 |
| **Significance**           |    **3* high — 9/12** | The paper resolves a named, concise conjecture and provides a reusable certified example. Its reach is currently specialised, and it does not yet establish a general counterexample family or unrestricted minimality.                                                                                                                                                |       0.80 |
| **Rigour**                 | **4* medium — 11/12** | Multiple exact proof routes, explicit witnesses, full raw data, deterministic replay, mutation tests and independent reviewer recalculations provide exceptionally strong rigour. The rating is below 12 because the environment is not pinned, exact-v3 independent reproduction is absent, and one structural theorem relies on an external computational threshold. |       0.91 |
| **Overall output quality** |    **3* high — 9/12** | Holistically, this is an internationally excellent specialised result with unusually strong internal evidence. The unresolved novelty comparison and release-assurance imprecision prevent a secure 4* judgement as submitted.                                                                                                                                         |       0.79 |

A plausible decision-changing path to **4* low — 10/12 overall** would require a convincing full-text novelty audit, exact-v3 independent reimplementation, immutable archival release, and a clearer demonstration that the identity or method materially advances work beyond this single counterexample.

This calibration is **indicative only and is not an official REF panel decision**.

## 11. References

### Graph theory and the TxGraffiti conjecture

Caro, Y., Davila, R., & Pepper, R. (2022). New results relating independence and matchings. *Discussiones Mathematicae Graph Theory, 42*(3), 921–935. [https://doi.org/10.7151/dmgt.2317](https://doi.org/10.7151/dmgt.2317)

Davila, R., Brimkov, B., & Pepper, R. (2025). *In reverie together: Ten years of mathematical discovery with a machine collaborator*. arXiv. [https://doi.org/10.48550/arXiv.2507.17780](https://doi.org/10.48550/arXiv.2507.17780) ([arXiv][2])

djma. (2026). *TxGraffiti-conjecture3-counterexample* [GitHub repository]. [https://github.com/djma/TxGraffiti-conjecture3-counterexample](https://github.com/djma/TxGraffiti-conjecture3-counterexample) ([GitHub][3])

### SAT, clause–literal graphs and independent domination

Ahadi, A., & Dehghan, A. (2019). ((2/2/3))-SAT problem and its applications in dominating set problems. *Discrete Mathematics & Theoretical Computer Science, 21*(4), Article 9. [https://doi.org/10.23638/DMTCS-21-4-9](https://doi.org/10.23638/DMTCS-21-4-9) ([arXiv][5])

Zhang, T., Peitl, T., & Szeider, S. (2024). Small unsatisfiable (k)-CNFs with bounded literal occurrence. In S. Chakraborty & J.-H. R. Jiang (Eds.), *27th International Conference on Theory and Applications of Satisfiability Testing (SAT 2024)* (LIPIcs Vol. 305, Article 31, pp. 31:1–31:22). Schloss Dagstuhl—Leibniz-Zentrum für Informatik. [https://doi.org/10.4230/LIPIcs.SAT.2024.31](https://doi.org/10.4230/LIPIcs.SAT.2024.31) ([DROPS][8])

Zverovich, I. E. (2006). Satgraphs and independent domination. Part 1. *Theoretical Computer Science, 352*(1–3), 47–56. [https://doi.org/10.1016/j.tcs.2005.08.038](https://doi.org/10.1016/j.tcs.2005.08.038) ([ScienceDirect][4])

### Evidence and assessment guidance

Evidence Press. (n.d.). *About this site*. Retrieved 6 August 2026, from [https://evidence-press.pages.dev/about/](https://evidence-press.pages.dev/about/) ([Evidence Press][1])

Evidence Press. (n.d.). *For AI agents*. Retrieved 6 August 2026, from [https://evidence-press.pages.dev/ai/](https://evidence-press.pages.dev/ai/) ([Evidence Press][9])

Research Excellence Framework. (2019). *Panel criteria and working methods* (REF 2019/02). [https://2021.ref.ac.uk/media/1450/ref-2019_02-panel-criteria-and-working-methods.pdf](https://2021.ref.ac.uk/media/1450/ref-2019_02-panel-criteria-and-working-methods.pdf) 

Research Excellence Framework. (2026). *Section 4: Contributions to Knowledge and Understanding guidance*. [https://2029.ref.ac.uk/guidance/section-4-contributions-to-knowledge-and-understanding-cku-guidance/](https://2029.ref.ac.uk/guidance/section-4-contributions-to-knowledge-and-understanding-cku-guidance/) ([REF 2029][7])

Research Excellence Framework. (n.d.). *Units of assessment*. Retrieved 6 August 2026, from [https://2029.ref.ac.uk/panels/units-of-assessment/](https://2029.ref.ac.uk/panels/units-of-assessment/) ([REF 2029][6])

[END]

[1]: https://evidence-press.pages.dev/about/ "About this site · Evidence Press"
[2]: https://arxiv.org/html/2507.17780v1 "In Reverie Together: Ten Years of Mathematical Discovery with a Machine Collaborator"
[3]: https://github.com/djma/TxGraffiti-conjecture3-counterexample "GitHub - djma/TxGraffiti-conjecture3-counterexample · GitHub"
[4]: https://www.sciencedirect.com/science/article/pii/S0304397505006638?utm_source=chatgpt.com "Satgraphs and independent domination. Part 1"
[5]: https://arxiv.org/abs/1605.01319?utm_source=chatgpt.com "SAT problem and its applications in dominating set problems"
[6]: https://2029.ref.ac.uk/panels/units-of-assessment/ "Units of assessment – REF 2029"
[7]: https://2029.ref.ac.uk/guidance/section-4-contributions-to-knowledge-and-understanding-cku-guidance/ "Section 4 – Contributions to Knowledge and Understanding (CKU) guidance – REF 2029"
[8]: https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-305?utm_source=chatgpt.com "27th International Conference on Theory and Applications of ..."
[9]: https://evidence-press.pages.dev/ai/ "For AI agents and automated research tools · Evidence Press"
