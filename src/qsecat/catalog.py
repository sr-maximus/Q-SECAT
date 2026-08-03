"""Catalog loading and traceability checks."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

from .paths import repo_root

CATALOG_NAMES = (
    "sources",
    "domains",
    "tactics",
    "techniques",
    "top10",
    "controls",
    "tests",
    "assurance-levels",
    "profiles",
    "mappings",
)

ID_PATTERNS = {
    "domains": re.compile(r"^QSD-\d{2}$"),
    "tactics": re.compile(r"^QTA-\d{2}$"),
    "techniques": re.compile(r"^QTE-\d{2}\.\d{3}$"),
    "top10": re.compile(r"^QST-\d{2}$"),
    "controls": re.compile(r"^QSC-\d{2}\.\d{3}$"),
    "tests": re.compile(r"^QSTEST-\d{2}\.\d{3}$"),
    "assurance-levels": re.compile(r"^QAL-[0-5]$"),
    "profiles": re.compile(r"^QSP-[A-Z0-9]+$"),
    "sources": re.compile(r"^SRC-[A-Z0-9-]+$"),
}

EXPECTED_COUNTS = {
    "sources": 27,
    "domains": 12,
    "tactics": 12,
    "techniques": 48,
    "top10": 10,
    "controls": 48,
    "tests": 48,
    "assurance-levels": 6,
    "profiles": 7,
    "mappings": 10,
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise TypeError(f"Invalid catalog envelope: {path}")
    return data


def load_catalog(name: str, root: Path | None = None) -> dict[str, Any]:
    if name not in CATALOG_NAMES:
        raise ValueError(f"Unknown catalog: {name}")
    root = root or repo_root()
    return load_yaml(root / "catalog" / f"{name}.yaml")


def catalog_index(name: str, root: Path | None = None) -> dict[str, dict[str, Any]]:
    items = load_catalog(name, root)["items"]
    result: dict[str, dict[str, Any]] = {}
    pattern = ID_PATTERNS.get(name)
    for item in items:
        item_id = item.get("id")
        if not isinstance(item_id, str):
            raise TypeError(f"Catalog {name} contains an item without a valid id")
        if pattern and not pattern.fullmatch(item_id):
            raise ValueError(f"Invalid identifier format {item_id} in {name}")
        if item_id in result:
            raise ValueError(f"Duplicate identifier {item_id} in {name}")
        result[item_id] = item
    return result


def _require(mapping: dict[str, Any], item_id: str, relation: str) -> None:
    if item_id not in mapping:
        raise ValueError(f"Broken {relation}: {item_id}")


def _require_unique(values: list[str], relation: str) -> None:
    if len(values) != len(set(values)):
        raise ValueError(f"Duplicate identifiers in {relation}")


def _validate_metadata(name: str, catalog: dict[str, Any]) -> None:
    metadata = catalog.get("metadata")
    if not isinstance(metadata, dict):
        raise TypeError(f"Catalog {name} has no metadata object")
    expected = {
        "framework": "Q-SECAT",
        "framework_version": "0.1.0",
        "status": "community-draft",
        "author": "Edwin Javier Peñuela Camacho",
        "license": "Apache-2.0",
    }
    for key, value in expected.items():
        if metadata.get(key) != value:
            raise ValueError(f"Catalog {name} metadata {key!r} must be {value!r}")


def check_traceability(root: Path | None = None) -> dict[str, int]:
    """Validate counts, identifiers and bidirectional catalog relationships."""
    root = root or repo_root()
    catalogs = {name: load_catalog(name, root) for name in CATALOG_NAMES}
    for name, catalog in catalogs.items():
        _validate_metadata(name, catalog)

    indexes = {name: catalog_index(name, root) for name in CATALOG_NAMES if name != "mappings"}
    mappings = catalogs["mappings"]["items"]

    counts = {name: len(indexes[name]) for name in indexes}
    counts["mappings"] = len(mappings)
    for name, expected in EXPECTED_COUNTS.items():
        actual = counts[name]
        if actual != expected:
            raise ValueError(f"{name} expected {expected} items, found {actual}")

    sources = indexes["sources"]
    domains = indexes["domains"]
    tactics = indexes["tactics"]
    techniques = indexes["techniques"]
    top10 = indexes["top10"]
    controls = indexes["controls"]
    tests = indexes["tests"]
    qals = indexes["assurance-levels"]
    profiles = indexes["profiles"]

    for source in sources.values():
        parsed = urlparse(source["url"])
        if parsed.scheme not in {"https", "http"} or not parsed.netloc:
            raise ValueError(f"Invalid source URL in {source['id']}: {source['url']}")

    for domain in domains.values():
        _require_unique(domain["references"], f"references from {domain['id']}")
        for item_id in domain["references"]:
            _require(sources, item_id, f"source link from {domain['id']}")

    for technique in techniques.values():
        _require(domains, technique["domain"], f"domain link from {technique['id']}")
        for field in ("tactics", "top10", "mitigated_by", "tested_by", "references"):
            _require_unique(technique[field], f"{field} from {technique['id']}")
        for item_id in technique["tactics"]:
            _require(tactics, item_id, f"tactic link from {technique['id']}")
        for item_id in technique["top10"]:
            _require(top10, item_id, f"top10 link from {technique['id']}")
            if technique["id"] not in top10[item_id]["techniques"]:
                raise ValueError(f"Non-reciprocal top10 link: {technique['id']} -> {item_id}")
        for item_id in technique["mitigated_by"]:
            _require(controls, item_id, f"control link from {technique['id']}")
            if technique["id"] not in controls[item_id]["mitigates"]:
                raise ValueError(f"Non-reciprocal mitigation link: {technique['id']} -> {item_id}")
        for item_id in technique["tested_by"]:
            _require(tests, item_id, f"test link from {technique['id']}")
            if tests[item_id]["technique"] != technique["id"]:
                raise ValueError(f"Non-reciprocal test link: {technique['id']} -> {item_id}")
        for item_id in technique["references"]:
            _require(sources, item_id, f"source link from {technique['id']}")

    for control in controls.values():
        _require(domains, control["domain"], f"domain link from {control['id']}")
        _require(qals, control["minimum_recommended_qal"], f"QAL link from {control['id']}")
        for field in ("mitigates", "verified_by", "references"):
            _require_unique(control[field], f"{field} from {control['id']}")
        for item_id in control["mitigates"]:
            _require(techniques, item_id, f"technique link from {control['id']}")
            if control["id"] not in techniques[item_id]["mitigated_by"]:
                raise ValueError(f"Non-reciprocal mitigation link: {control['id']} -> {item_id}")
            if techniques[item_id]["domain"] != control["domain"]:
                raise ValueError(f"Domain mismatch between {control['id']} and {item_id}")
        for item_id in control["verified_by"]:
            _require(tests, item_id, f"test link from {control['id']}")
            if tests[item_id]["control"] != control["id"]:
                raise ValueError(f"Non-reciprocal verification link: {control['id']} -> {item_id}")
        for item_id in control["references"]:
            _require(sources, item_id, f"source link from {control['id']}")

    for test in tests.values():
        _require(domains, test["domain"], f"domain link from {test['id']}")
        _require(techniques, test["technique"], f"technique link from {test['id']}")
        _require(controls, test["control"], f"control link from {test['id']}")
        _require(qals, test["minimum_qal"], f"QAL link from {test['id']}")
        if techniques[test["technique"]]["domain"] != test["domain"]:
            raise ValueError(f"Domain mismatch between {test['id']} and {test['technique']}")
        if controls[test["control"]]["domain"] != test["domain"]:
            raise ValueError(f"Domain mismatch between {test['id']} and {test['control']}")
        _require_unique(test["references"], f"references from {test['id']}")
        for item_id in test["references"]:
            _require(sources, item_id, f"source link from {test['id']}")

    for risk in top10.values():
        for field in ("domains", "techniques", "controls"):
            _require_unique(risk[field], f"{field} from {risk['id']}")
        for item_id in risk["domains"]:
            _require(domains, item_id, f"domain link from {risk['id']}")
        for item_id in risk["techniques"]:
            _require(techniques, item_id, f"technique link from {risk['id']}")
            if risk["id"] not in techniques[item_id]["top10"]:
                raise ValueError(f"Non-reciprocal technique link: {risk['id']} -> {item_id}")
        for item_id in risk["controls"]:
            _require(controls, item_id, f"control link from {risk['id']}")

    for profile in profiles.values():
        required = profile["required_domains"]
        optional = profile["optional_domains"]
        _require_unique(required, f"required domains from {profile['id']}")
        _require_unique(optional, f"optional domains from {profile['id']}")
        overlap = set(required) & set(optional)
        if overlap:
            raise ValueError(f"Profile {profile['id']} has required/optional overlap: {sorted(overlap)}")
        for item_id in [*required, *optional]:
            _require(domains, item_id, f"domain link from {profile['id']}")

    all_qsecat_ids: set[str] = set().union(*(set(index) for index in indexes.values()))
    allowed_relationships = {
        "related_to",
        "specializes",
        "implements",
        "evidences",
        "mitigates",
        "detects",
        "depends_on",
    }
    seen_mapping_keys: set[tuple[str, str, str]] = set()
    for mapping in mappings:
        qsecat_id = mapping.get("qsecat")
        external = mapping.get("external")
        relationship = mapping.get("relationship")
        if qsecat_id not in all_qsecat_ids:
            raise ValueError(f"Mapping references unknown Q-SECAT ID: {qsecat_id}")
        if not isinstance(external, str) or not external.strip():
            raise ValueError(f"Mapping {qsecat_id} has no external reference")
        if relationship not in allowed_relationships:
            raise ValueError(f"Mapping {qsecat_id} has invalid relationship: {relationship}")
        key = (qsecat_id, external, relationship)
        if key in seen_mapping_keys:
            raise ValueError(f"Duplicate mapping: {key}")
        seen_mapping_keys.add(key)

    return {name: counts[name] for name in EXPECTED_COUNTS}
