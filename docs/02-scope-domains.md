# Scope and Security Domains

Q-SECAT uses 12 domains (`QSD`) to prevent a narrow “PQC-only” interpretation of quantum cybersecurity.

| ID | Domain | Central security question |
|---|---|---|
| QSD-01 | Cryptographic Transition & Agility | Can vulnerable cryptography be found, prioritized, replaced and rolled back safely? |
| QSD-02 | Quantum Cryptography & QKD | Are QKD protocol, implementation, authentication, KMS and trust assumptions valid? |
| QSD-03 | Quantum Networks & Internet | Are quantum links, network control, orchestration, timing and boundaries resilient? |
| QSD-04 | QRNG, Entropy & Key Lifecycle | Is randomness characterized, monitored, conditioned, delivered and governed correctly? |
| QSD-05 | Quantum Hardware & Physical Environment | Can physical conditions, shared resources or access alter, leak or degrade operation? |
| QSD-06 | Control Electronics, Firmware & Calibration | Are pulses, firmware, calibration and telemetry authentic, authorized and recoverable? |
| QSD-07 | Quantum Software, Compilers & Circuits | Is code/circuit transformation trustworthy, reproducible and protected from tampering? |
| QSD-08 | Quantum Cloud, API & Multi-tenancy | Are identity, jobs, data, results, scheduling and tenant boundaries secure? |
| QSD-09 | Hybrid Workflows & Quantum ML | Is the classical-quantum loop protected against data, optimizer and orchestration manipulation? |
| QSD-10 | Quantum Sensing, Metrology & Timing | Are sensor inputs, references, calibration and measurements authentic and available? |
| QSD-11 | Supply Chain, Provenance & Lifecycle | Can components, updates, services and evidence be traced and sustained? |
| QSD-12 | Governance, Assurance & Resilience | Are ownership, claims, skills, incident response and independent assurance adequate? |

## Cross-domain properties

Every assessment considers:

- confidentiality and intellectual-property protection;
- integrity of configuration, circuits, measurements and results;
- availability and graceful degradation;
- authenticity, authorization and non-repudiation where relevant;
- privacy and data sovereignty;
- physical and mission safety;
- reproducibility and scientific integrity;
- interoperability and portability;
- supply-chain provenance;
- auditability and evidence quality.

## Technologies included

Quantum information science is commonly organized around computing, communication/networking and sensing/metrology. Q-SECAT adds the security-relevant supporting layers: PQC, QKD, QRNG, classical control, cloud, software, hybrid workflows, supply chain and governance.

## Scope profiles

A project may publish a profile without changing core IDs:

- `QSP-PQC` — enterprise cryptographic transition;
- `QSP-QKD` — QKD product/network evaluation;
- `QSP-QCLOUD` — cloud quantum service;
- `QSP-QHW` — hardware laboratory and control stack;
- `QSP-QNET` — quantum-network testbed;
- `QSP-QSENSE` — quantum sensing/metrology;
- `QSP-FULL` — integrated quantum information system.
