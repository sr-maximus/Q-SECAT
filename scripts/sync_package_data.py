"""Synchronize canonical catalogs and schema into installable package data."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAIRS = (
    (ROOT / "catalog", ROOT / "src/qsecat/data/catalog", "*.yaml"),
    (ROOT / "schema", ROOT / "src/qsecat/data/schema", "*.json"),
)


def expected_files(source: Path, pattern: str) -> list[Path]:
    return sorted(path for path in source.glob(pattern) if path.is_file())


def sync(check: bool) -> int:
    drift: list[str] = []
    for source, destination, pattern in PAIRS:
        files = expected_files(source, pattern)
        expected_names = {item.name for item in files}
        actual_names = {item.name for item in destination.glob(pattern)} if destination.exists() else set()
        if actual_names != expected_names:
            drift.append(f"{destination.relative_to(ROOT)} file set differs from {source.relative_to(ROOT)}")
        for source_file in files:
            destination_file = destination / source_file.name
            differs = not destination_file.is_file() or not filecmp.cmp(
                source_file, destination_file, shallow=False
            )
            if differs:
                drift.append(str(destination_file.relative_to(ROOT)))
        if not check:
            destination.mkdir(parents=True, exist_ok=True)
            for existing in destination.glob(pattern):
                if existing.name not in expected_names:
                    existing.unlink()
            for source_file in files:
                shutil.copy2(source_file, destination / source_file.name)

    if check and drift:
        print("Package data is out of sync:", file=sys.stderr)
        for item in sorted(set(drift)):
            print(f"- {item}", file=sys.stderr)
        return 1
    if check:
        print("Package data is synchronized.")
    else:
        print("Package data synchronized.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail instead of copying when data differs")
    args = parser.parse_args()
    return sync(args.check)


if __name__ == "__main__":
    raise SystemExit(main())
