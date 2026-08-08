# TxGraffiti Conjecture 15/3 resolution - release candidate 4.0.0-rc1

## Verdict

The conjecture is false. The package establishes a connected cubic graph \(G\) on 50 vertices with

\[
\boxed{\mu^*(G)=15<16=i(G)}.
\]

Here \(i(G)\) is the independent domination number and \(\mu^*(G)\) is the minimum cardinality of a maximal matching.

## Release status

This is an **unrefereed candidate release**. All bundled theorem-critical deterministic checks passed in the recorded environment and from a clean extracted copy. The exact release has **not** been independently rerun, independently reimplemented, formally verified or conventionally peer reviewed.

Fable's independent receipt concerns the byte-distinct `v2-theorem` predecessor. A separate full review concerns exact v3 and recommended major release-hardening revisions. `ASSURANCE.md`, `VERSION_HISTORY.md` and `REVIEW_RESPONSE.md` record those scopes.

## Start here

| Need | File |
|---|---|
| Bounded conclusion and hashes | `STATUS.md` |
| Mathematical argument | `MANUSCRIPT.pdf` |
| Evidence and replay details | `EVIDENCE_SUPPLEMENT.pdf` |
| Agent navigation | `AI_INDEX.md` |
| Claim map | `CLAIMS.json` |
| Assurance booleans | `ASSURANCE.json` |
| Provenance | `PROVENANCE.md` |
| Sources and dependency boundary | `SOURCES.md` |

## Principal results

1. **Counterexample:** \(\mu^*(G)=15<16=i(G)\).
2. **Exact identity:** for an indexed CNF \(F\) on \(k\) variables,
   \[
   i(G(F))=k+\beta(F),
   \]
   where \(\beta(F)\) is minimum bilateral deficiency.
3. **Exact twice-occurrence case:** if every indexed clause contains exactly three distinct literals on three distinct variables, no complementary pair, and each signed literal occurs exactly twice, then \(G(F)\) is cubic and \(\mu^*(G(F))=k\).
4. **Restricted threshold:** conditional on the cited 20-clause SAT theorem, every cubic graph with a dominating induced matching and order below 50 satisfies the conjectured inequality. The order-50 example is sharp within this subclass.

The literal-pair/clause-incidence graph architecture and twice-positive/twice-negative formula class have clear prior antecedents. The release claims only that its targeted search did not locate the exact bilateral-deficiency identity.

## Proof architecture

The matching value is elementary. The independent-domination upper bound is an explicit 16-vertex witness. Two exact lower-bound routes exclude size at most 15:

- a 21,803-byte gzip-compressed proof-tree certificate checked from the raw graph;
- exhaustive enumeration of all \(3^{15}=14,348,907\) partial assignments through the exact identity.

Ordinary formula unsatisfiability is not enough: an independent dominating set may mix literal and clause vertices. Bilaterality is the additional condition that controls those mixed sets.

## Replay

Core proof, with no third-party Python dependency:

```sh
./run_core_verification.sh
```

Optional generic mixed-integer corroboration:

```sh
./run_optional_audits.sh
```

The declarative environment is in `environment/Containerfile`; optional wheels are hash-locked in `environment/requirements-milp.lock`. Container execution remains pending because Docker/Podman was unavailable in the authoring environment.

## Scope limits

The package does not prove global order-50 minimality among all cubic or regular counterexamples, uniqueness of the graph, secured novelty priority for Theorem 1, exact-release independent reproduction, formal verification or peer review.
