from qsecat.risk import (
    confidence_score,
    impact_score,
    mitigation_effectiveness,
    score_finding,
    severity_for,
    timeline_urgency,
)


def test_timeline_urgency_bands():
    scenarios = [
        ({"data_shelf_life_years": 2, "migration_lead_years": 2, "threat_horizon_years": 12}, 1),
        ({"data_shelf_life_years": 5, "migration_lead_years": 5, "threat_horizon_years": 10}, 2),
        ({"data_shelf_life_years": 7, "migration_lead_years": 5, "threat_horizon_years": 10}, 3),
        ({"data_shelf_life_years": 10, "migration_lead_years": 6, "threat_horizon_years": 10}, 4),
        ({"data_shelf_life_years": 15, "migration_lead_years": 5, "threat_horizon_years": 10}, 5),
    ]
    for timeline, expected in scenarios:
        assert timeline_urgency(timeline) == expected
    assert timeline_urgency(None) == 3


def test_score_is_bounded_and_confidence_does_not_change_central_risk():
    base = {
        "impact": {
            "confidentiality": 5, "integrity": 4, "availability": 2,
            "safety_mission": 2, "privacy_ip": 4, "regulatory_sovereignty": 3,
        },
        "likelihood": {"exposure": 4, "feasibility": 2, "actor_capability": 3, "stealth_persistence": 4},
        "timeline": {"data_shelf_life_years": 12, "migration_lead_years": 4, "threat_horizon_years": 10},
        "control_effectiveness": {"implementation": 0.45, "assurance": 0.5},
        "evidence_confidence": {
            "maturity": 0.6,
            "source_quality": 0.8,
            "reproducibility": 0.7,
            "applicability": 0.9,
        },
    }
    result = score_finding(base)
    lower_confidence = dict(base)
    lower_confidence["evidence_confidence"] = {
        "maturity": 0.1,
        "source_quality": 0.1,
        "reproducibility": 0.1,
        "applicability": 0.1,
    }
    result_low = score_finding(lower_confidence)
    assert 0 <= result.residual_risk <= 100
    assert result.residual_risk == result_low.residual_risk
    assert result_low.uncertainty_high > result.uncertainty_high
    assert result_low.uncertainty_low < result.uncertainty_low


def test_component_calculations_and_severity():
    dimensions = [
        "confidentiality",
        "integrity",
        "availability",
        "safety_mission",
        "privacy_ip",
        "regulatory_sovereignty",
    ]
    impact = {key: 5 for key in dimensions}
    assert impact_score(impact) == 5
    assert mitigation_effectiveness({"implementation": 1, "assurance": 1}) == 1
    full_confidence = {"maturity": 1, "source_quality": 1, "reproducibility": 1, "applicability": 1}
    assert confidence_score(full_confidence) == 1
    assert severity_for(19.99) == "low"
    assert severity_for(20) == "moderate"
    assert severity_for(40) == "high"
    assert severity_for(60) == "very_high"
    assert severity_for(80) == "critical"
