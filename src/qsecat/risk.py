"""Transparent Q-SECAT risk and uncertainty calculations."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import asdict, dataclass
from typing import Any

IMPACT_WEIGHTS: dict[str, float] = {
    "confidentiality": 0.16,
    "integrity": 0.22,
    "availability": 0.16,
    "safety_mission": 0.20,
    "privacy_ip": 0.12,
    "regulatory_sovereignty": 0.14,
}

LIKELIHOOD_WEIGHTS: dict[str, float] = {
    "exposure": 0.25,
    "feasibility": 0.20,
    "actor_capability": 0.20,
    "urgency": 0.20,
    "stealth_persistence": 0.15,
}

CONFIDENCE_WEIGHTS: dict[str, float] = {
    "maturity": 0.35,
    "source_quality": 0.25,
    "reproducibility": 0.25,
    "applicability": 0.15,
}


@dataclass(frozen=True)
class RiskResult:
    impact: float
    urgency: float
    likelihood: float
    mitigation_effectiveness: float
    base_risk: float
    residual_risk: float
    confidence: float
    uncertainty_low: float
    uncertainty_high: float
    severity: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _number(value: Any, name: str, minimum: float, maximum: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    value = float(value)
    if not minimum <= value <= maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}")
    return value


def _weighted(values: Mapping[str, Any], weights: Mapping[str, float], maximum: float) -> float:
    missing = [key for key in weights if key not in values]
    if missing:
        raise ValueError(f"Missing score fields: {', '.join(missing)}")
    return sum(_number(values[key], key, 0.0, maximum) * weight for key, weight in weights.items())


def impact_score(impact: Mapping[str, Any]) -> float:
    """Return impact on the 0–5 scale."""
    values = {key: _number(impact.get(key), key, 0.0, 5.0) for key in IMPACT_WEIGHTS}
    weighted = sum(values[key] * weight for key, weight in IMPACT_WEIGHTS.items())
    return round(0.60 * max(values.values()) + 0.40 * weighted, 4)


def timeline_urgency(timeline: Mapping[str, Any] | None) -> float:
    """Convert X + Y - Z into an ordinal 1–5 urgency score.

    Unknown timeline inputs intentionally default to 3.0; callers should lower evidence
    confidence to preserve uncertainty rather than interpreting the default as certainty.
    """
    if not timeline:
        return 3.0
    try:
        x = _number(timeline["data_shelf_life_years"], "data_shelf_life_years", 0.0, 100.0)
        y = _number(timeline["migration_lead_years"], "migration_lead_years", 0.0, 50.0)
        z = _number(timeline["threat_horizon_years"], "threat_horizon_years", 0.0, 100.0)
    except (KeyError, TypeError, ValueError):
        return 3.0
    gap = x + y - z
    if gap <= -5:
        return 1.0
    if gap <= 0:
        return 2.0
    if gap <= 3:
        return 3.0
    if gap <= 7:
        return 4.0
    return 5.0


def likelihood_score(likelihood: Mapping[str, Any], urgency: float) -> float:
    """Return likelihood on the 0–5 scale."""
    values = dict(likelihood)
    values["urgency"] = _number(values.get("urgency", urgency), "urgency", 0.0, 5.0)
    return round(_weighted(values, LIKELIHOOD_WEIGHTS, 5.0), 4)


def mitigation_effectiveness(control: Mapping[str, Any]) -> float:
    """Return control effectiveness on the 0–1 scale."""
    implementation = _number(control.get("implementation"), "implementation", 0.0, 1.0)
    assurance = _number(control.get("assurance"), "assurance", 0.0, 1.0)
    return round(implementation * (0.40 + 0.60 * assurance), 4)


def confidence_score(evidence: Mapping[str, Any]) -> float:
    """Return evidence confidence on the 0–1 scale."""
    return round(_weighted(evidence, CONFIDENCE_WEIGHTS, 1.0), 4)


def severity_for(score: float) -> str:
    score = _number(score, "risk", 0.0, 100.0)
    if score < 20:
        return "low"
    if score < 40:
        return "moderate"
    if score < 60:
        return "high"
    if score < 80:
        return "very_high"
    return "critical"


def score_finding(finding: Mapping[str, Any]) -> RiskResult:
    """Calculate all Q-SECAT scores for one finding."""
    impact = impact_score(finding["impact"])
    urgency = timeline_urgency(finding.get("timeline"))
    likelihood = likelihood_score(finding["likelihood"], urgency)
    mitigation = mitigation_effectiveness(finding["control_effectiveness"])
    confidence = confidence_score(finding["evidence_confidence"])

    base = 100.0 * (impact / 5.0) * (likelihood / 5.0)
    residual = max(0.0, min(100.0, base * (1.0 - mitigation)))
    low = max(0.0, residual * (0.65 + 0.35 * confidence))
    high = min(100.0, residual * (1.35 - 0.35 * confidence))

    return RiskResult(
        impact=round(impact, 2),
        urgency=round(urgency, 2),
        likelihood=round(likelihood, 2),
        mitigation_effectiveness=round(mitigation, 4),
        base_risk=round(base, 2),
        residual_risk=round(residual, 2),
        confidence=round(confidence, 4),
        uncertainty_low=round(low, 2),
        uncertainty_high=round(high, 2),
        severity=severity_for(residual),
    )
