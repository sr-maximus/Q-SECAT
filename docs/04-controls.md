# Control Model

## Control structure

Each `QSC` record contains:

- stable ID and title;
- security objective;
- implementation guidance;
- expected evidence;
- linked domains and techniques;
- minimum recommended assurance;
- references and limitations.

Controls are technology-neutral outcomes. For example, “protect calibration integrity” is a control; a particular vendor signing mechanism is one possible implementation.

## Control states

| State | Meaning |
|---|---|
| `not_implemented` | No effective implementation evidence |
| `planned` | Approved design or plan, not operating |
| `partial` | Some assets, paths or lifecycle stages covered |
| `implemented` | In scope and operating, with internal evidence |
| `verified` | Reproducibly tested against acceptance criteria |
| `independently_assured` | Reviewed by a competent independent party or formal scheme |
| `not_applicable` | Explicit, justified exclusion |
| `unknown` | Evidence insufficient |

## Design families

The 48 controls fall into recurring families:

- inventory and dependency visibility;
- secure configuration and cryptographic policy;
- identity, segmentation and least privilege;
- integrity, signing, attestation and provenance;
- isolation, scheduling and resource governance;
- monitoring, baselines and anomaly detection;
- resilient architecture, fallback and recovery;
- verification, reproducibility and independent assurance.

## Control inheritance

A customer may inherit controls from a cloud provider or QKD network operator. Inheritance does not remove accountability. The assessment must record:

- provider and service boundary;
- contractual or technical evidence;
- customer configuration responsibilities;
- failure/exit strategy;
- last validation date;
- residual assumptions.

## Mapping discipline

Mappings to NIST CSF, NIST SP 800-53, ISO/IEC 27001, Common Criteria, MITRE ATT&CK/D3FEND or OWASP are informative, versioned and non-equivalent. A mapping means conceptual relationship, not compliance inheritance.
