#!/usr/bin/env python3
"""Adversarial smoke tests for check_ids15_certificate.py.

The tests mutate one valid proof in four ways. The checker must reject an invalid
leaf, an invalid branch witness, a truncated proof, and trailing proof data.
Only the Python standard library is required.
"""
from __future__ import annotations

import argparse
import gzip
import subprocess
import sys
import tempfile
from pathlib import Path


def run_checker(checker: Path, graph: Path, certificate: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(checker), str(graph), str(certificate)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checker", type=Path, default=Path("check_ids15_certificate.py"))
    parser.add_argument("--graph", type=Path, default=Path("counterexample.json"))
    parser.add_argument("--certificate", type=Path, default=Path("ids_le15.tree.gz"))
    args = parser.parse_args()

    valid = run_checker(args.checker, args.graph, args.certificate)
    if valid.returncode != 0:
        raise SystemExit(f"canonical certificate was rejected:\n{valid.stderr}")

    with gzip.open(args.certificate, "rt", encoding="ascii") as handle:
        lines = handle.read().splitlines()
    if not lines or lines[0] != "IDS15_TREE_V1":
        raise SystemExit("unexpected canonical certificate format")

    mutations: dict[str, list[str]] = {}

    bad_leaf = lines.copy()
    first_bound = bad_leaf.index("B")
    bad_leaf[first_bound] = "C"
    mutations["invalid_leaf"] = bad_leaf

    bad_witness = lines.copy()
    if not bad_witness[1].startswith("P "):
        raise SystemExit("unexpected root certificate token")
    bad_witness[1] = "P 50"
    mutations["invalid_witness"] = bad_witness

    mutations["truncated"] = lines[:-1]
    mutations["trailing_data"] = lines + ["B"]

    with tempfile.TemporaryDirectory(prefix="ids15-checker-tests-") as tmp:
        tmpdir = Path(tmp)
        for name, mutated in mutations.items():
            path = tmpdir / f"{name}.tree"
            path.write_text("\n".join(mutated) + "\n", encoding="ascii")
            result = run_checker(args.checker, args.graph, path)
            if result.returncode == 0:
                raise SystemExit(f"checker accepted mutation {name}")
            if "CERTIFICATE REJECTED:" not in result.stderr:
                raise SystemExit(
                    f"checker failed unclearly on mutation {name}:\n{result.stderr}"
                )
            print(f"MUTATION_REJECTED name={name}")

    print(f"ADVERSARIAL_TESTS passed={len(mutations)} failed=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
