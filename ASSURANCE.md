# Assurance record

**Release:** `txgraffiti-c3-resolution/4.0.0-rc1`  
**Status:** `unrefereed-candidate`  
**Scope rule:** every assurance statement applies to the exact release object only unless a different archive hash is named.

## Current assurance matrix

| Dimension | Exact v4 state | Basis |
|---|---|---|
| Peer reviewed | No | No conventional journal or specialist peer review is claimed |
| Internal deterministic replay | Passed | Core replay passed in the recorded environment and from a clean extracted copy |
| Independent rerun of exact v4 | No | No external exact-v4 execution receipt exists |
| Independent reimplementation of exact v4 | No | No clean-room exact-v4 implementation exists |
| Formal verification | No | No proof-assistant artefact exists |
| Environment definition | Pinned | Base-image digest, exact tool versions and hash-locked optional wheels are supplied |
| Container replay | Pending | Docker or Podman was unavailable in the authoring environment |
| Predecessor independent analysis | Partial | Fable analysed `v2-theorem`, SHA-256 `106787...a589`, with an independent harness |
| Predecessor technical review | Completed | The supplied full review inspected exact v3, SHA-256 `94fe632...3e8f`, and recommended release hardening |

The permissible human-facing formulation is:

> All bundled theorem-critical deterministic checks passed in the recorded environment and from a clean extracted copy.

The release must not be described as independently reproduced, formally verified or peer reviewed.

## Assurance layers by claim

### Central disproof

The central claim

\[
\mu^*(G)=15<16=i(G)
\]

has the following support:

1. a canonical 50-vertex raw graph in three mutually checked encodings;
2. an elementary maximal-matching witness and lower bound;
3. an explicit independent dominating set of size 16;
4. two exact lower-bound routes for \(i(G)\):
   - a raw-graph proof tree checked by a separately written standard-library Python checker;
   - exhaustive bilateral-deficiency enumeration over all \(3^{15}\) partial assignments;
5. optional generic mixed-integer formulations as corroboration.

The central disproof does not depend on the external 20-clause SAT threshold.

### General identity

The proof of

\[
i(G(F))=k+\beta(F)
\]

is included in the canonical manuscript. It was also re-derived on the byte-distinct `v2-theorem` predecessor. The theorem's mathematical status and its novelty status are separate: the proof is supported; priority remains bounded by the literature corpus described in `PRIOR_ART_COMPARISON.md`.

### Restricted order-50 theorem

The theorem for cubic graphs with a dominating induced matching depends on the external result `ZPS-2024-20-CLAUSE`. `THEOREM_DEPENDENCY.md` records the exact clause conventions and the definition-transfer lemma. Failure of that external dependency would affect this restricted structural theorem, not the counterexample.

## Trust base

The finite certificate route trusts:

- the raw graph parser;
- `check_ids15_certificate.py`;
- ordinary Python integer semantics and machine execution.

The second exact route trusts the independently implemented C++ exhaustive checker and Theorem 1's proof. Four targeted certificate mutations test specific rejection paths but are not exhaustive checker validation.

## Machine-readable form

See `ASSURANCE.json` and claim-level fields in `CLAIMS.json`.
