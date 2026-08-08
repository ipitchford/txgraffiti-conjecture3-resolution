#!/usr/bin/env python3
"""Build a deterministic release ZIP with fixed timestamps and sorted entries."""
from __future__ import annotations

import argparse
import os
import stat
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT_NAME = "txgraffiti_conjecture3_resolution_v4"
FIXED_TIME = (2026, 8, 6, 12, 0, 0)
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache", "_renders"}


def included(path: Path) -> bool:
    rel = path.relative_to(BASE)
    if any(part in EXCLUDED_PARTS or part.startswith(".") for part in rel.parts):
        return False
    return path.is_file()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=BASE.parent / f"{ROOT_NAME}.zip",
    )
    args = parser.parse_args()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    paths = sorted(
        (path for path in BASE.rglob("*") if included(path)),
        key=lambda path: path.relative_to(BASE).as_posix(),
    )

    with zipfile.ZipFile(
        output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9, strict_timestamps=True
    ) as archive:
        for path in paths:
            rel = path.relative_to(BASE).as_posix()
            info = zipfile.ZipInfo(f"{ROOT_NAME}/{rel}", FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            mode = 0o755 if os.access(path, os.X_OK) else 0o644
            info.external_attr = (stat.S_IFREG | mode) << 16
            info.flag_bits |= 0x800
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    print(f"ARCHIVE_CREATED path={output} files={len(paths)} bytes={output.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
