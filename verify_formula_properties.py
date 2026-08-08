#!/usr/bin/env python3
"""Exact truth-table checks for the 15-variable counterexample formula."""
from __future__ import annotations

import json
from pathlib import Path


def assignment_from_code(code: int, variables: int) -> list[bool]:
    return [bool((code >> j) & 1) for j in range(variables)]


def clause_satisfied(clause: list[int], assignment: list[bool]) -> bool:
    for literal in clause:
        value = assignment[abs(literal) - 1]
        if (literal > 0 and value) or (literal < 0 and not value):
            return True
    return False


def missed_clauses(formula: list[list[int]], assignment: list[bool]) -> list[int]:
    return [i for i, clause in enumerate(formula) if not clause_satisfied(clause, assignment)]


def main() -> int:
    base = Path(__file__).resolve().parent
    data = json.loads((base / 'counterexample.json').read_text(encoding='utf-8'))
    variables = int(data['variables'])
    formula = [[int(lit) for lit in clause] for clause in data['formula_signed_integers']]
    if variables != 15 or len(formula) != 20:
        raise ValueError('unexpected formula dimensions')

    satisfying = 0
    minimum_missed = len(formula) + 1
    attaining = 0
    all_assignments: list[list[bool]] = []
    all_missed: list[list[int]] = []
    for code in range(1 << variables):
        assignment = assignment_from_code(code, variables)
        missed = missed_clauses(formula, assignment)
        all_assignments.append(assignment)
        all_missed.append(missed)
        if not missed:
            satisfying += 1
        if len(missed) < minimum_missed:
            minimum_missed = len(missed)
            attaining = 1
        elif len(missed) == minimum_missed:
            attaining += 1

    deletion_witnesses: list[int] = []
    for deleted in range(len(formula)):
        witness_code = None
        for code, missed in enumerate(all_missed):
            if all(index == deleted for index in missed):
                witness_code = code
                break
        if witness_code is None:
            raise AssertionError(f'formula without clause C{deleted + 1} remained unsatisfiable')
        deletion_witnesses.append(witness_code)

    simple_assignment = [False, True, True] + [False] * 12
    simple_missed = missed_clauses(formula, simple_assignment)
    if simple_missed != [17]:
        raise AssertionError(f'simple assignment misses {simple_missed}, expected only C18')

    if satisfying != 0 or minimum_missed != 1 or attaining != 3318:
        raise AssertionError(
            f'unexpected truth-table result: sat={satisfying}, min={minimum_missed}, count={attaining}'
        )

    print('FORMULA_PROPERTIES_VERIFIED')
    print(f'complete_assignments={1 << variables}')
    print(f'satisfying_assignments={satisfying}')
    print(f'minimum_unsatisfied_clauses={minimum_missed}')
    print(f'assignments_attaining_minimum={attaining}')
    print(f'minimally_unsatisfiable=true deletion_witnesses={len(deletion_witnesses)}')
    print('simple_assignment_misses_only=C18')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
