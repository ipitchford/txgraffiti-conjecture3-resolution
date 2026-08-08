# AI index

## Object

- Release ID: `txgraffiti-c3-resolution/4.0.0-rc1`
- Status: `unrefereed-candidate`
- Central verdict: TxGraffiti Conjecture 15/3 is disproved by a connected cubic graph of order 50 with `mu_star=15` and `i=16`.
- Exact assurance: bundled deterministic checks passed; exact-release independent rerun and formal verification are false.

## Canonical entry points

1. `STATUS.md` - bounded conclusion, exact object status and core hashes.
2. `MANUSCRIPT.pdf` - canonical mathematical paper.
3. `EVIDENCE_SUPPLEMENT.pdf` - canonical evidence, replay and dependency supplement.
4. `CLAIMS.json` - claim-to-evidence map.
5. `ASSURANCE.json` - exact object-scoped assurance fields.
6. `RESULT.json` - machine-readable verdict and theorem summary.
7. `PROVENANCE.md` - graph, input and release lineage.
8. `SOURCES.md` - corpus boundary and primary references.
9. `MANIFEST.sha256` - internal release integrity.

## Theorem-critical files

- `counterexample.json`
- `counterexample.edgelist`
- `counterexample.g6`
- `ids_le15.tree.gz`
- `check_ids15_certificate.py`
- `generate_ids15_certificate.cpp`
- `verify_counterexample.cpp`
- `check_encodings.py`
- `verify_formula_properties.py`
- `run_core_verification.sh`

The optional `independent_milp_audit.py` is corroborative and is not required for the proof.

## Replay

```sh
./run_core_verification.sh
```

Optional corroborative audit:

```sh
./run_optional_audits.sh
```

Combined:

```sh
RUN_OPTIONAL_AUDITS=1 ./run_verification.sh
```

## Dependency boundary

- Central counterexample: self-contained relative to the bundled graph and proof machinery.
- Exact formula-graph identity: proved in the manuscript; no external theorem is load-bearing.
- Restricted order-50 dominating-induced-matching theorem: depends on `ZPS-2024-20-CLAUSE`; see `THEOREM_DEPENDENCY.md` and `EXTERNAL_DEPENDENCIES.json`.

## Assurance interpretation

Do not infer independence from byte-identical regeneration. Fable's independent analysis concerns the byte-distinct `v2-theorem` predecessor. The supplied full review concerns exact v3. Neither record is an exact-v4 independent rerun.
