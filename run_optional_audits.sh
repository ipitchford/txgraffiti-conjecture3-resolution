#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PYTHON="${PYTHON:-python3}"

if ! "$PYTHON" - <<'PYDEP_END' >/dev/null 2>&1
import numpy, scipy
from scipy.optimize import milp
PYDEP_END
then
  printf '%s\n' 'OPTIONAL_AUDIT_SKIPPED reason=numpy_or_scipy_unavailable'
  exit 2
fi

printf '%s\n' '== Optional generic mixed-integer audit =='
"$PYTHON" independent_milp_audit.py counterexample.json
printf '%s\n' 'OPTIONAL_AUDIT_PASSED scope=corroborative_milp'
