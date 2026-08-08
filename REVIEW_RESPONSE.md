# Response to the full v3 review

**Reviewed object:** `v3-merged`  
**Reviewed archive SHA-256:** `94fe632a280d0ca8d6d06ec3cf2309d07973acdac0c43c53e21c3d4191903e8f`  
**Review file:** `EXTERNAL_REVIEW_2026-08-06.md`  
**Review file SHA-256:** `412227e2f14ae4e5c3ea01fa4b41791be55122fdf01193773fe23f1f08468cf6`  
**Review recommendation:** major revisions before Evidence Press release.

The review found no fatal mathematical defect. Its major comments concern assurance scope, prior-art positioning, the external threshold dependency, environment reproducibility and the release interface. Release 4.0.0-rc1 addresses those comments as follows.

## Major comment 1 - exact-object assurance

**Disposition: implemented.**

- Added `ASSURANCE.md` and `ASSURANCE.json` with exact-release booleans.
- Set exact-v4 `independentlyRerun=false`, `independentlyReimplemented=false`, `formallyVerified=false`, `peerReviewed=false`.
- Scoped Fable's receipt to `v2-theorem`, SHA-256 `106787526e7d356d7c0535ab01c43aa7d6a1223a95fe728bba76e287aadea589`.
- Scoped the supplied full review to exact v3, SHA-256 `94fe632a280d0ca8d6d06ec3cf2309d07973acdac0c43c53e21c3d4191903e8f`.
- Replaced generic verification language in canonical documents with “all bundled theorem-critical deterministic checks passed in the recorded environment”.
- Added `STATUS.md`, `VERSION_HISTORY.md` and object-level hashes.

An exact-v4 clean-room reimplementation remains outstanding and is stated as such.

## Major comment 2 - closest prior art

**Disposition: implemented with a bounded residual risk.**

- Added `PRIOR_ART_COMPARISON.md` comparing definitions, graph construction, objective, clause types, reduction direction and exact identity against Zverovich (2006), Ahadi and Dehghan (2019), and Zhang, Peitl and Szeider (2024).
- Cited the clause-literal graph antecedent at the point of construction in the canonical manuscript.
- Defined the exact-occurrence class as prior art.
- Adopted the wording: “We prove the following exact identity; our targeted search did not locate an equivalent published statement.”
- Retained the unresolved full-text satgraph collision risk.

A complete subscription-index and full-text search remains outstanding.

## Major comment 3 - external SAT threshold

**Disposition: implemented.**

- Recast the order-50 theorem explicitly as conditional on `ZPS-2024-20-CLAUSE`.
- Added `THEOREM_DEPENDENCY.md` with the exact source conventions and a definition-transfer lemma.
- Explained tautology deletion, duplicate-clause deletion, exact three-distinct-literal clauses and signed occurrence bounds.
- Added `EXTERNAL_DEPENDENCIES.json` with DOI, URN, version, access date, licence and dependency role.
- Made clear that the external threshold is not needed for the central counterexample.

The official PDF could not be materialised in the build runtime, so a PDF SHA-256 is not recorded. DOI, URN, publication version, page count and access date are pinned, and the official Zenodo computational supplement is pinned by repository-supplied MD5 `a98d3544d736ccf3f23b9922100d468e`; the residual PDF-hash limitation is explicit.

## Major comment 4 - execution environment

**Disposition: substantially implemented; container execution pending.**

- Added `environment/Containerfile` with a digest-pinned Debian 13.3 base and exact package versions.
- Added hash-locked CPython 3.13 Linux x86-64 NumPy/SciPy wheels for the optional audit.
- Recorded compiler flags, locale, timezone, deterministic environment variables and the absence of theorem-critical randomness.
- Split theorem-critical replay from optional mixed-integer corroboration.
- Replayed the core from a clean extracted copy.

Docker/Podman was unavailable in the authoring environment. The container definition was therefore not built here, and `containerReplayCompleted=false` remains the correct assurance field.

## Major comment 5 - canonical interface and terminology

**Disposition: implemented.**

Added:

- `AI_INDEX.md`;
- `STATUS.md`;
- `ASSURANCE.md` and `ASSURANCE.json`;
- `PROVENANCE.md`;
- `SOURCES.md`;
- `CLAIMS.json`;
- `MANIFEST.sha256`;
- `LICENSE.md`;
- `DOCUMENT_MAP.md`.

The canonical outputs are now `MANUSCRIPT.pdf` and `EVIDENCE_SUPPLEMENT.pdf`. Historical PDFs were removed. The manuscript defines “proper 3-CNF”, uses “positive-degree regular graph”, identifies the proof tree as gzip-compressed, qualifies sharpness by subclass and distinguishes indexed duplicate clauses.

## Should-fix items

The canonical manuscript now:

- presents the two lower-bound routes side by side;
- includes a construction schematic;
- includes a compact claim-to-evidence table;
- explains why unsatisfiability alone is insufficient;
- records exact dependency and assurance boundaries.

The evidence supplement records canonical hashes, replay commands, environment, provenance and remaining gaps.

## Remaining work after v4.0.0-rc1

The following upgrades remain open rather than silently treated as complete:

1. exact-v4 independent rerun and clean-room reimplementation;
2. container build and archived continuous-integration receipt;
3. full-text novelty audit of the satgraph literature and specialist database search;
4. specialist graph-theory or SAT review;
5. proof-assistant formalisation;
6. immutable repository release or archival DOI for the exact final archive.

These gaps affect assurance and originality calibration. They do not reopen the certified numerical counterexample unless an independent implementation rejects the raw graph or its parameter values.
