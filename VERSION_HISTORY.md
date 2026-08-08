# Version history and immutable lineage

Hashes identify release objects; labels are descriptive only. The historical name `v2` was reused for two byte-distinct archives, so this record uses explicit labels.

| Label | ZIP SHA-256 | Contents and assurance scope |
|---|---|---|
| `v1-initial` | `53290a6908febcb7c6225ece8345bff5d4f3a9a5b6c43b6b55680fe4d0703555` | Initial audit and counterexample-resolution bundle. |
| `v2-theorem` | `106787526e7d356d7c0535ab01c43aa7d6a1223a95fe728bba76e287aadea589` | Exact formula-graph identity, corrected order-50 theorem and formula/graph cross-checks. Fable's independent receipt applies to this object. |
| `v2-proof-tree` | `e4d2d0b8fdc6322ccf80932c8495931aa8f36e07862877f4a2867f2d841efd0c` | Added compact raw-graph proof tree, independent checker, deterministic regeneration and targeted mutation tests. |
| `v3-merged` | `94fe632a280d0ca8d6d06ec3cf2309d07973acdac0c43c53e21c3d4191903e8f` | Merged theorem and certificate architectures. The supplied full review applies to this exact object and recommended major release hardening. |
| `4.0.0-rc1` | recorded in the external `.zip.sha256` sidecar | Implements exact-object assurance, prior-art comparison, external-dependency mapping, pinned environment definition, canonical interface, licence and review response. |

## Scope of inherited review evidence

- `INDEPENDENT_REPLAY_FABLE.md` authenticates and independently analyses `v2-theorem`. It does not authenticate later archive bytes.
- `EXTERNAL_REVIEW_2026-08-06.md` reviews exact `v3-merged`. It is not an exact-v4 rerun.
- Release 4.0.0-rc1 has internal deterministic replay and clean-copy replay only. No exact-v4 independent reproduction is claimed.

## Mathematical object identity

Across the listed releases, the canonical graph edge list and graph6 encoding describe the same labelled 50-vertex cubic graph. JSON structure and supporting documents changed, but the 75-edge graph and invariant claim remained stable.
