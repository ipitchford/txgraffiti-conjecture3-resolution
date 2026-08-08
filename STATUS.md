# Canonical release status

**Release identifier:** `txgraffiti-c3-resolution/4.0.0-rc1`  
**Status:** `unrefereed-candidate`  
**Date:** 6 August 2026  
**Canonical paper:** `MANUSCRIPT.pdf`  
**Canonical evidence supplement:** `EVIDENCE_SUPPLEMENT.pdf`

## Bounded conclusion

The release establishes a connected cubic graph \(G\) on 50 vertices with

\[
\boxed{\mu^*(G)=15<16=i(G)}.
\]

This is a counterexample to the conjecture that every finite positive-degree regular graph satisfies \(i(G)\leq\mu^*(G)\).

The release also proves an exact formula-graph identity and, conditional on the cited external 20-clause theorem, a sharp order boundary within the subclass of cubic graphs admitting a dominating induced matching.

## Assurance snapshot

- All bundled theorem-critical deterministic checks passed in the recorded environment.
- The same core replay passed from a clean extracted copy.
- Exact-v4 independent rerun: **no**.
- Exact-v4 independent reimplementation: **no**.
- Formal verification: **no**.
- Conventional peer review: **no**.
- Environment definition: **pinned**, with container execution still pending.
- Predecessor independent analysis: **partial**, exact hash recorded.

See `ASSURANCE.md` and `ASSURANCE.json` for the object-scoped record.

## Core object hashes

```text
1753ad874d1b09f101f06e91f7a53cfc27026fb4c1166bf7bd16269dae7fbd0f  counterexample.json
d8b6dc5c5738ac657edfa17193363b48f9416111278e6de07246889668fcb3c6  counterexample.g6
63363b5e9c8bdd119418024fe80da7bba36f71119f6e89778519d3fbd8a916b2  counterexample.edgelist
a14c38f6b2f1ed9c65da3efccb60e8443b033b96f8de9cec90fb5d82d020f988  ids_le15.tree.gz
```

Canonical document hashes:

```text
36d1dbd0f17da59327eac7e96ab108f65d04b8b7aead46419adef6b1d4fcc54e  MANUSCRIPT.pdf
ec0a6c4435272f630ff14f4f0b1ec8f8e09bb4010d5bcd9278ddf09eaf1b0e78  EVIDENCE_SUPPLEMENT.pdf
412227e2f14ae4e5c3ea01fa4b41791be55122fdf01193773fe23f1f08468cf6  EXTERNAL_REVIEW_2026-08-06.md
```

The outer ZIP hash appears in the external `.zip.sha256` sidecar after the deterministic build.

## Claims not made

The release does not establish that:

- order 50 is globally minimal among all cubic or regular counterexamples;
- the order-50 graph is unique;
- the exact identity has secured literature priority;
- the exact release has been independently reproduced;
- the package has been formally verified or conventionally peer reviewed.
