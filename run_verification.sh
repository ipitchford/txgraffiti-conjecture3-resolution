#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

./run_core_verification.sh

if [[ "${RUN_OPTIONAL_AUDITS:-0}" == "1" ]]; then
  ./run_optional_audits.sh
else
  printf '%s\n' 'OPTIONAL_AUDIT_NOT_REQUESTED set_RUN_OPTIONAL_AUDITS=1_to_run'
fi
