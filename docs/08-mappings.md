# External Mappings

## Purpose

Mappings help teams reuse existing governance and threat practices. They are informative crosswalks, not claims of equivalence or compliance.

## Mapping types

- `related_to` — shares a concept;
- `specializes` — Q-SECAT gives quantum-specific detail;
- `implements` — control can help implement an external requirement;
- `evidences` — test may provide evidence for a requirement;
- `mitigates` — control reduces a technique;
- `detects` — control/test may detect a technique;
- `depends_on` — Q-SECAT item relies on another control or assumption.

## Principal references

| Q-SECAT area | Useful external reference |
|---|---|
| Enterprise risk and governance | NIST CSF 2.0; ISO/IEC 27001/27002 |
| Control implementation | NIST SP 800-53; CIS Controls where applicable |
| Adversary behavior | MITRE ATT&CK; CAPEC; CWE |
| Defensive concepts | MITRE D3FEND |
| Software/supply chain | SLSA; SPDX; CycloneDX SBOM/CBOM |
| PQC algorithms | NIST FIPS 203, 204, 205 and related validation guidance |
| Crypto agility | NIST CSWP 39upd1 |
| QKD evaluation | ISO/IEC 23837-1/-2; ETSI GS QKD 016; Common Criteria |
| QKD networks | ITU-T Y.3800, X.1710, X.1711, Y.3832; ETSI QKD APIs |
| Entropy/RNG | NIST SP 800-90 series and entropy validation |
| Cloud assurance | CSA CCM; ISO/IEC 27017/27018 where applicable |
| AI/ML hybrid workflows | NIST AI RMF; MITRE ATLAS where applicable |

## OWASP/MITRE positioning

Q-SECAT's Top 10 is an independent project artifact intended to improve prioritization. It is not an OWASP project. QTA/QTE uses tactic/technique concepts for usability but is not part of MITRE ATT&CK and should not use ATT&CK branding.

## Versioning

Every mapping entry includes source name, version/date, relationship type and reviewer. When an external standard changes, the mapping may become stale without changing the underlying Q-SECAT control.
