from pathlib import Path

from qsecat.catalog import check_traceability

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_traceability_and_counts():
    assert check_traceability(ROOT) == {
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
