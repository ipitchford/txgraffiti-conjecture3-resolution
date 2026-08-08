#!/usr/bin/env python3
"""Verify MANIFEST.sha256 and reject missing or unlisted release files."""
from __future__ import annotations
import hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parent
MANIFEST = BASE / "MANIFEST.sha256"
EXCLUDED_NAMES = {"MANIFEST.sha256"}
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache", "_renders"}


def included(path: Path) -> bool:
    rel = path.relative_to(BASE)
    if path.name in EXCLUDED_NAMES:
        return False
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return False
    if any(part.startswith(".") for part in rel.parts):
        return False
    return path.is_file()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    expected: dict[str, str] = {}
    for line_number, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            digest, rel = line.split("  ", 1)
        except ValueError as exc:
            raise AssertionError(f"malformed manifest line {line_number}") from exc
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise AssertionError(f"invalid digest on line {line_number}")
        if rel in expected:
            raise AssertionError(f"duplicate manifest entry: {rel}")
        expected[rel] = digest

    actual_paths = {p.relative_to(BASE).as_posix(): p for p in BASE.rglob("*") if included(p)}
    if set(expected) != set(actual_paths):
        missing = sorted(set(expected) - set(actual_paths))
        unlisted = sorted(set(actual_paths) - set(expected))
        raise AssertionError(f"manifest membership mismatch missing={missing} unlisted={unlisted}")

    for rel, path in sorted(actual_paths.items()):
        actual = sha256(path)
        if actual != expected[rel]:
            raise AssertionError(f"digest mismatch for {rel}: {actual} != {expected[rel]}")

    print(f"MANIFEST_PASSED files={len(expected)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
