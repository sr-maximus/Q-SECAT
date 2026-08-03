# Landscape Review and Design Gap

## Executive finding

The quantum-security ecosystem contains authoritative standards, research taxonomies, migration models and implementation tools, but they address different slices of the problem. Q-SECAT therefore acts as an integration and testing layer rather than claiming that no prior work exists.

## Existing work and its useful boundary

| Work | Primary contribution | Boundary relevant to Q-SECAT |
|---|---|---|
| NIST FIPS 203/204/205 | Standardized ML-KEM, ML-DSA and SLH-DSA | Algorithms and implementation requirements; not a full security-testing framework for quantum systems |
| NIST CSWP 39upd1 / NCCoE migration work | Crypto agility, discovery and PQC migration | Organizational/classical transition focus |
| ISO/IEC 23837-1/-2 | QKD security requirements, evaluation and testing | Specific to QKD and Common Criteria context |
| ETSI GS QKD 016 and QKD APIs | QKD protection profile and interfaces | Specific QKD modules and networks |
| ITU-T Y.3800/X.1710/X.1711/Y.3832 | QKD network overview, security, protocols and orchestration | Communications layer; not full compute/sensing stack |
| IEEE P1947 | Project for a quantum cybersecurity framework | Active standards project; public page describes scope but it is not a published final standard at this release date |
| QATT&CK | ATT&CK-style adversary taxonomy for quantum-computing infrastructure | Thesis-level taxonomy; focuses primarily on adversarial behavior and quantum computing infrastructure |
| QRAMM | Open organizational PQC-readiness maturity model | Readiness and migration rather than full quantum-system testing |
| QUASAR | Strategic post-quantum architecture/risk framework | Transition and readiness focus |
| Baseri et al. | Quantum-security risk assessment across algorithms, certificates and protocols | Strong PQC risk analysis, narrower than full QIS stack |
| Argonne QIS taxonomy/testbed paper | Preliminary vulnerability taxonomy and testbed concept | Research proposal that supports the need for an evolving experimental framework |
| Quantum hardware security literature | Crosstalk, calibration, compiler, cloud and IP risks | Research findings requiring normalization into controls and tests |

## Gap addressed

Q-SECAT combines five artifacts that are usually disconnected:

1. a **system-domain model** spanning computing, communication, sensing and supporting infrastructure;
2. an **adversary taxonomy** with stable IDs;
3. a **control catalog** expressed as verifiable outcomes;
4. a **safe testing catalog** with assurance levels;
5. a **risk and evidence model** that reports uncertainty instead of hiding it.

## Non-claims

Q-SECAT does not claim:

- that a cryptographically relevant quantum computer exists today;
- a precise date for such a capability;
- that QKD is automatically secure because it uses quantum physics;
- that PQC removes classical implementation, key-management or supply-chain risk;
- that all technique entries have been observed in production incidents;
- that a numerical score proves security.

Each technique contains an evidence-status field so hypotheses, laboratory demonstrations, implementation classes and observed incidents are not conflated.

## Naming review

The name “Q-SECAT” is used in this release as a project identifier for **Quantum Security Evaluation, Controls, Assurance & Testing**. A web search performed for this release did not identify a clearly conflicting quantum-cybersecurity framework with the exact name. This is not a legal trademark clearance; maintainers should conduct a formal review before commercial registration.
