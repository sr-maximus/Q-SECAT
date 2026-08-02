from pathlib import Path

from qsecat.validate import load_assessment, validate_assessment

ROOT = Path(__file__).resolve().parents[1]


def test_example_assessment_is_valid():
    data = load_assessment(ROOT / "examples" / "assessment-example.yaml")
    assert validate_assessment(data, ROOT) == []
