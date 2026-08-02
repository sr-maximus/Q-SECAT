# Assurance and Evidence

## Q-SECAT Assurance Levels

| ID | Name | Minimum evidence |
|---|---|---|
| QAL-0 | Unsubstantiated | Claim, assumption or marketing statement only |
| QAL-1 | Documented | Named owner, scope, policy/design and versioned record |
| QAL-2 | Reviewed | Architecture/static review with traceable artifacts |
| QAL-3 | Reproducibly Tested | Repeatable simulation or software/integration test with acceptance criteria |
| QAL-4 | Controlled Laboratory | Hardware/physical validation under controlled, recorded conditions |
| QAL-5 | Independently Assured | Competent independent reproduction, accredited evaluation or recognized certification |

QAL describes evidence depth for a claim; it does not certify the whole system. A control can have different QAL values across assets.

## Evidence maturity

| Value | Label | Description |
|---:|---|---|
| 0.00 | none | No artifact |
| 0.20 | asserted | Unverified statement |
| 0.40 | documented | Versioned document or configuration |
| 0.60 | internally tested | Repeatable internal test evidence |
| 0.80 | independently reproduced | Separate competent reviewer reproduced result |
| 1.00 | formally evaluated | Evidence from an applicable accredited/formal scheme |

## Source quality

Prefer, in order:

1. published standards and official validation records;
2. peer-reviewed research and reproducible public artifacts;
3. authoritative technical guidance and protection profiles;
4. vendor documentation with test evidence;
5. expert judgment with explicit assumptions;
6. unsupported claims.

A source can be authoritative for its own product while still being insufficient for an independent security claim.

## Evidence object

Each evidence record should include:

```yaml
id: EVID-001
title: Cryptographic inventory export
type: cbom
uri: evidence://protected/assessment-2026/cbom.json
sha256: "..."
created_at: 2026-08-01T12:00:00Z
collected_by: assessor@example.org
scope: production-api
source_quality: 0.8
reproducibility: 0.7
applicability: 0.9
qal: QAL-2
classification: confidential
retention: 3y
```

## Claim-evidence matrix

Every material report claim should be one of:

- **verified:** acceptance criteria met with sufficient evidence;
- **partially verified:** limited scope or mixed results;
- **not verified:** evidence absent or inadequate;
- **refuted:** evidence contradicts the claim;
- **not applicable:** justified exclusion.

Marketing terms such as “quantum-safe,” “unhackable,” “information-theoretically secure” or “certified” require precise scope, assumptions and supporting evidence.
