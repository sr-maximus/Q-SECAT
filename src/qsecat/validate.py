"""Assessment schema and catalog-reference validation."""

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from .catalog import catalog_index
from .paths import repo_root


def _normalise_yaml_scalars(value: Any) -> Any:
    """Convert YAML-native date objects into JSON Schema-compatible strings."""
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _normalise_yaml_scalars(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_normalise_yaml_scalars(item) for item in value]
    return value


def load_assessment(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        data = _normalise_yaml_scalars(yaml.safe_load(text))
    if not isinstance(data, dict):
        raise TypeError("Assessment must be a YAML or JSON object")
    return data


def validate_assessment(data: dict[str, Any], root: Path | None = None) -> list[str]:
    root = root or repo_root()
    schema = json.loads((root / "schema" / "assessment.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path))
    ]
    if errors:
        return errors

    techniques = catalog_index("techniques", root)
    controls = catalog_index("controls", root)
    tests = catalog_index("tests", root)
    domains = catalog_index("domains", root)
    evidence_ids = {item["id"] for item in data.get("evidence", [])}
    asset_ids = {item["id"] for item in data["scope"]["assets"]}

    seen_domains: set[str] = set()
    for record in data["domain_applicability"]:
        domain_id = record["domain_id"]
        if domain_id not in domains:
            errors.append(f"domain_applicability: unknown domain {domain_id}")
        if domain_id in seen_domains:
            errors.append(f"domain_applicability: duplicate domain {domain_id}")
        seen_domains.add(domain_id)
        for evidence_id in record.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(f"domain_applicability {domain_id}: unknown evidence {evidence_id}")

    finding_ids: set[str] = set()
    for finding in data["findings"]:
        fid = finding["id"]
        if fid in finding_ids:
            errors.append(f"findings: duplicate id {fid}")
        finding_ids.add(fid)
        technique_id = finding["technique_id"]
        control_id = finding["control_id"]
        test_id = finding["test_id"]
        if technique_id not in techniques:
            errors.append(f"{fid}: unknown technique {technique_id}")
        if control_id not in controls:
            errors.append(f"{fid}: unknown control {control_id}")
        if test_id not in tests:
            errors.append(f"{fid}: unknown test {test_id}")
        if technique_id in techniques and control_id not in techniques[technique_id]["mitigated_by"]:
            errors.append(f"{fid}: {control_id} is not linked to {technique_id}")
        if technique_id in techniques and test_id not in techniques[technique_id]["tested_by"]:
            errors.append(f"{fid}: {test_id} is not linked to {technique_id}")
        for asset_id in finding.get("asset_ids", []):
            if asset_id not in asset_ids:
                errors.append(f"{fid}: unknown asset {asset_id}")
        for evidence_id in finding.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(f"{fid}: unknown evidence {evidence_id}")
    return errors
