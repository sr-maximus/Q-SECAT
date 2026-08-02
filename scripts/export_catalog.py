#!/usr/bin/env python3
"""Export the linked technique-control-test matrix to CSV."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qsecat.catalog import catalog_index

techniques = catalog_index("techniques", ROOT)
controls = catalog_index("controls", ROOT)
tests = catalog_index("tests", ROOT)
domains = catalog_index("domains", ROOT)
out = ROOT / "dist" / "qsecat-matrix.csv"
out.parent.mkdir(exist_ok=True)
fields = [
    "domain_id", "domain", "tactic_ids", "technique_id", "technique", "evidence_status",
    "top10_ids", "control_id", "control", "test_id", "test", "test_class", "minimum_qal", "references"
]
with out.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for technique in techniques.values():
        control = controls[technique["mitigated_by"][0]]
        test = tests[technique["tested_by"][0]]
        writer.writerow({
            "domain_id": technique["domain"],
            "domain": domains[technique["domain"]]["name"],
            "tactic_ids": ";".join(technique["tactics"]),
            "technique_id": technique["id"],
            "technique": technique["title"],
            "evidence_status": technique["evidence_status"],
            "top10_ids": ";".join(technique["top10"]),
            "control_id": control["id"],
            "control": control["title"],
            "test_id": test["id"],
            "test": test["title"],
            "test_class": test["test_class"],
            "minimum_qal": test["minimum_qal"],
            "references": ";".join(technique["references"]),
        })
print(out)
