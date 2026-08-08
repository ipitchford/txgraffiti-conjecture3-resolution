#!/usr/bin/env python3
"""Create the canonical hash manifest without self-reference."""
from __future__ import annotations
import hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "MANIFEST.sha256"
EXCLUDED_NAMES = {"MANIFEST.sha256"}
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache", "_renders"}
EXCLUDED_PREFIXES = (".",)


def included(path: Path) -> bool:
    rel = path.relative_to(BASE)
    if path.name in EXCLUDED_NAMES:
        return False
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return False
    if any(part.startswith(EXCLUDED_PREFIXES) for part in rel.parts):
        return False
    return path.is_file()


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    paths = sorted((p for p in BASE.rglob("*") if included(p)), key=lambda p: p.relative_to(BASE).as_posix())
    text = "".join(f"{digest(path)}  {path.relative_to(BASE).as_posix()}\n" for path in paths)
    OUTPUT.write_text(text, encoding="utf-8")
    print(f"MANIFEST_CREATED files={len(paths)}")


if __name__ == "__main__":
    main()
