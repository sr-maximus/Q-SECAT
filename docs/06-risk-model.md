# Risk and Uncertainty Model

## 1. Purpose

Q-SECAT uses a transparent ordinal model for prioritization. It deliberately avoids pretending that a precise probability of quantum capability or exploitation is known. Scores are comparable only when assessors use the same profile, scales and evidence rules.

## 2. Impact

Score six impact dimensions from 0 to 5:

- `confidentiality`;
- `integrity`;
- `availability`;
- `safety_mission`;
- `privacy_ip`;
- `regulatory_sovereignty`.

The impact score combines the most severe consequence with a weighted portfolio value:

\[
I = 0.60\max(v_i) + 0.40\sum_i w_i v_i
\]

Default weights, summing to 1.00:

| Dimension | Weight |
|---|---:|
| Confidentiality | 0.16 |
| Integrity | 0.22 |
| Availability | 0.16 |
| Safety/mission | 0.20 |
| Privacy/IP | 0.12 |
| Regulatory/sovereignty | 0.14 |

Profiles may change weights, but must version and disclose them.

## 3. Quantum urgency

For confidentiality dependent on quantum-vulnerable public-key cryptography, Q-SECAT uses a timeline gap derived from the well-known migration relation:

\[
G = X + Y - Z
\]

where:

- `X` = years the information or trust anchor must remain protected;
- `Y` = estimated migration duration;
- `Z` = assessor-selected threat horizon in years.

`Z` is a scenario assumption, not a prediction. Use several scenarios when decision sensitivity is high.

Default urgency score:

| Gap G | Urgency |
|---:|---:|
| `G <= -5` | 1 |
| `-5 < G <= 0` | 2 |
| `0 < G <= 3` | 3 |
| `3 < G <= 7` | 4 |
| `G > 7` | 5 |
| Unknown inputs | 3, with reduced confidence |

For non-cryptographic quantum-system threats, replace timeline urgency with `technology_exposure` on the same 0–5 scale and document the rationale.

## 4. Likelihood

Score each factor 0–5:

- `exposure` — reachability and attack-surface availability;
- `feasibility` — required access, expertise, resources and repeatability;
- `actor_capability` — capability of plausible actors in scope;
- `urgency` — quantum timeline or current technology exposure;
- `stealth_persistence` — ability to evade detection or create durable effects.

\[
L = 0.25E_x + 0.20F + 0.20A + 0.20U + 0.15S
\]

## 5. Control effectiveness

Record:

- `implementation` from 0.00 to 1.00;
- `assurance` from 0.00 to 1.00, derived from evidence and QAL.

\[
M = implementation \times (0.40 + 0.60 \times assurance)
\]

This prevents an undocumented implementation claim from receiving full credit.

## 6. Base and residual risk

\[
R_{base} = 100 \times \frac{I}{5} \times \frac{L}{5}
\]

\[
R_{residual} = R_{base} \times (1-M)
\]

Clamp results to 0–100.

| Score | Severity |
|---:|---|
| 0–19.99 | Low |
| 20–39.99 | Moderate |
| 40–59.99 | High |
| 60–79.99 | Very High |
| 80–100 | Critical |

## 7. Confidence

Evidence confidence is independent of risk:

\[
C = 0.35M_e + 0.25Q_s + 0.25R_p + 0.15T_a
\]

where each term is 0–1:

- `M_e` evidence maturity;
- `Q_s` source quality;
- `R_p` reproducibility;
- `T_a` temporal/context applicability.

The uncertainty interval is:

\[
R_{low} = R(0.65 + 0.35C)
\]

\[
R_{high} = \min(100, R(1.35 - 0.35C))
\]

Confidence narrows the interval but does not lower the central risk. High risk with low confidence means “investigate urgently,” not “ignore.”

## 8. Scenario analysis

For CRQC-dependent confidentiality risk, calculate at least three threat-horizon scenarios when material:

- optimistic/long horizon;
- planning/baseline horizon;
- conservative/short horizon.

Never publish one scenario as a certain “Q-day.” Record source, date and stakeholder responsible for selecting the assumption.

## 9. Limits

- Scales are ordinal, not physical measurements.
- Weights encode policy preference and require governance approval.
- Correlated risks and cascading failures require scenario analysis beyond simple addition.
- Physical safety analysis may require specialized methods such as FMEA, HAZOP or STPA in parallel.
- A score cannot establish algorithmic or information-theoretic security.
