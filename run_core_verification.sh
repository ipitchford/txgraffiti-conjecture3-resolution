#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

CXX="${CXX:-c++}"
PYTHON="${PYTHON:-python3}"
CXXFLAGS=(-std=c++20 -O3 -Wall -Wextra -Wconversion -Wshadow -pedantic)

cleanup() {
  rm -f .verify_counterexample.tmp .generate_ids15_certificate.tmp
  rm -f "${TMP_TREE:-}" "${TMP_GZ:-}"
}
trap cleanup EXIT

printf '%s\n' '== Encoding consistency =='
"$PYTHON" check_encodings.py

printf '%s\n' '== Formula properties =='
"$PYTHON" verify_formula_properties.py

printf '%s\n' '== Dependency-free graph verification =='
"$CXX" "${CXXFLAGS[@]}" verify_counterexample.cpp -o .verify_counterexample.tmp
./.verify_counterexample.tmp

printf '%s\n' '== Proof-tree verification =='
"$PYTHON" check_ids15_certificate.py counterexample.json ids_le15.tree.gz

printf '%s\n' '== Deterministic certificate regeneration =='
"$CXX" "${CXXFLAGS[@]}" generate_ids15_certificate.cpp -o .generate_ids15_certificate.tmp
TMP_TREE="$(mktemp "${TMPDIR:-/tmp}/ids15-tree.XXXXXX")"
TMP_GZ="${TMP_TREE}.gz"
./.generate_ids15_certificate.tmp "$TMP_TREE"
gzip -n -9 -c "$TMP_TREE" > "$TMP_GZ"
cmp -s "$TMP_GZ" ids_le15.tree.gz
printf '%s\n' 'CERTIFICATE_REPRODUCED byte_identical=1'

printf '%s\n' '== Targeted checker mutations =='
"$PYTHON" test_certificate_checker.py

printf '%s\n' '== Release metadata and assurance scope =='
"$PYTHON" check_release_metadata.py

if [[ -f MANIFEST.sha256 ]]; then
  printf '%s\n' '== Release manifest =='
  "$PYTHON" check_manifest.py
else
  printf '%s\n' 'MANIFEST_CHECK skipped=1 reason=manifest_not_yet_generated'
fi

printf '%s\n' 'CORE_REPLAY_PASSED scope=bundled_deterministic_checks environment=recorded'
