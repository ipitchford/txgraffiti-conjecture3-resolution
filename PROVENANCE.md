# Provenance and contribution record

## Mathematical object

The canonical graph is the 50-vertex, 75-edge object encoded in:

- `counterexample.json`;
- `counterexample.edgelist`;
- `counterexample.g6`.

Those files have been cross-checked to represent the same labelled graph. The same graph was publicly committed on 23 July 2026 in the repository at

https://github.com/djma/TxGraffiti-conjecture3-counterexample

under commit `7810f30c5e9da0af9ece566bdffa5844d6b34f1b`.

This release does not claim first discovery of the graph or unconditional priority for the exact formula-graph identity.

## Release lineage

- `v1-initial`: SHA-256 `53290a6908febcb7c6225ece8345bff5d4f3a9a5b6c43b6b55680fe4d0703555`.
- `v2-theorem`: SHA-256 `106787526e7d356d7c0535ab01c43aa7d6a1223a95fe728bba76e287aadea589`.
- `v2-proof-tree`: SHA-256 `e4d2d0b8fdc6322ccf80932c8495931aa8f36e07862877f4a2867f2d841efd0c`.
- `v3-merged`: SHA-256 `94fe632a280d0ca8d6d06ec3cf2309d07973acdac0c43c53e21c3d4191903e8f`.
- `v4.0.0-rc1`: identified by the external archive sidecar generated with this package.

`VERSION_HISTORY.md` explains the historical reuse of the `v2` label.

## Inputs and transformations

The audited submission is preserved without modification at `source/newproof.zip`, SHA-256

```text
1bb020e35dc99e896faa1215877f1306d6400c6d901b5f8bd59f50fb8df43e96
```

The release reconstructs and verifies the counterexample rather than treating the submitted search log as a proof. It preserves the source for auditability.

## Contribution categories

The package distinguishes:

- **pre-existing public construction:** the canonical graph and predecessor certificate bundle;
- **AI-assisted mathematical synthesis:** the bilateral-deficiency theorem, corrected structural threshold and release integration;
- **programmatic verification:** exact graph checks, proof-tree generation/checking, formula enumeration and optional optimisation;
- **editorial decisions:** claim scope, assurance labels, canonical interface, licensing and release status;
- **external review evidence:** the Fable predecessor receipt and the supplied full v3 review, each scoped to its exact object.

The release remains anonymous and contains no asserted personal authorship or e-mail address. Attribution for reuse may be given to “the release contributors”.

## Integrity

`MANIFEST.sha256` authenticates every regular file in the release other than the manifest itself. The outer ZIP sidecar authenticates the immutable archive. The sidecar and internal manifest are source-supplied integrity records, not independent provenance.
