"""Repository path discovery for the reference CLI."""

from __future__ import annotations

import os
from pathlib import Path


def repo_root() -> Path:
    candidates: list[Path] = []
    if os.environ.get("QSECAT_HOME"):
        candidates.append(Path(os.environ["QSECAT_HOME"]).expanduser())
    candidates.append(Path.cwd())
    candidates.extend(Path(__file__).resolve().parents)
    candidates.append(Path(__file__).resolve().parent / "data")
    for candidate in candidates:
        if (candidate / "catalog" / "techniques.yaml").is_file() and (
            candidate / "schema" / "assessment.schema.json"
        ).is_file():
            return candidate
    raise FileNotFoundError(
        "Q-SECAT catalog data was not found. Run inside the repository, reinstall the package, "
        "or set QSECAT_HOME."
    )
