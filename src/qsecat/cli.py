"""Q-SECAT command-line interface."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from . import __version__
from .catalog import check_traceability
from .risk import score_finding
from .validate import load_assessment, validate_assessment


def _print_json(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=False))


def command_validate(path: Path) -> int:
    data = load_assessment(path)
    errors = validate_assessment(data)
    if errors:
        _print_json({"valid": False, "path": str(path), "errors": errors})
        return 1
    _print_json({"valid": True, "path": str(path), "findings": len(data.get("findings", []))})
    return 0


def command_score(path: Path) -> int:
    data = load_assessment(path)
    errors = validate_assessment(data)
    if errors:
        _print_json({"valid": False, "errors": errors})
        return 1
    findings = []
    for finding in data["findings"]:
        result = score_finding(finding).to_dict()
        findings.append(
            {
                "id": finding["id"],
                "title": finding["title"],
                "technique_id": finding["technique_id"],
                **result,
            }
        )
    ordered = sorted(findings, key=lambda item: item["residual_risk"], reverse=True)
    summary = {
        "assessment_id": data["assessment_id"],
        "framework_version": data["framework_version"],
        "finding_count": len(ordered),
        "highest_residual_risk": ordered[0]["residual_risk"] if ordered else 0.0,
        "findings": ordered,
    }
    _print_json(summary)
    return 0


def command_coverage() -> int:
    counts = check_traceability()
    _print_json({"valid": True, "framework_version": __version__, "counts": counts})
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="qsecat",
        description="Validate Q-SECAT catalogs and score authorized security assessments.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate an assessment YAML/JSON file")
    validate_parser.add_argument("path", type=Path)

    score_parser = subparsers.add_parser("score", help="Validate and calculate risk for an assessment")
    score_parser.add_argument("path", type=Path)

    subparsers.add_parser("coverage", help="Check catalog counts and relationship integrity")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            return command_validate(args.path)
        if args.command == "score":
            return command_score(args.path)
        if args.command == "coverage":
            return command_coverage()
    except (FileNotFoundError, TypeError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
