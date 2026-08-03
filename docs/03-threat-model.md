# Threat Model and Adversary Taxonomy

## Threat actors

Q-SECAT does not infer motivation from technology alone. Relevant actors may include:

- external cybercriminal or extortion actor;
- state-aligned or strategic intelligence actor;
- malicious or negligent insider;
- compromised supplier, maintainer or cloud operator;
- competing researcher or industrial espionage actor;
- opportunistic tenant of a shared service;
- automated malware or compromised orchestration component;
- environmental or operational fault that produces attack-like effects.

## Trust boundaries

At minimum, model boundaries between:

- user and quantum-cloud provider;
- tenant and tenant;
- compiler/transpiler and execution backend;
- classical controller and QPU/sensor;
- calibration authority and production configuration;
- QKD module, classical authenticated channel, KMS and application;
- network orchestrator, trusted node, repeater/memory and endpoint;
- supplier, integrator, maintainer and operator;
- measurement producer and downstream decision system.

## Tactics

| ID | Tactic | Adversary objective |
|---|---|---|
| QTA-01 | Reconnaissance & Profiling | Learn topology, modality, schedules, noise, versions or trust relationships |
| QTA-02 | Resource & Supply Preparation | Obtain access, dependencies, components or positions needed for later action |
| QTA-03 | Initial Access | Enter a classical, quantum, cloud, laboratory or supplier boundary |
| QTA-04 | Classical Control-Plane Compromise | Control identity, API, orchestration, host, network or storage supporting quantum operation |
| QTA-05 | Calibration & Environment Manipulation | Alter calibration or operating conditions to influence performance or trust |
| QTA-06 | Circuit, Job & Data Manipulation | Modify algorithms, circuits, inputs, measurements or results |
| QTA-07 | Shared-Resource & Multi-tenant Abuse | Exploit scheduling, crosstalk, reuse or shared infrastructure |
| QTA-08 | Side Channel & Leakage | Infer secrets, IP, workload or state from observable effects |
| QTA-09 | Identity, Keys & Randomness Abuse | Compromise authentication, entropy, key generation, storage, delivery or retirement |
| QTA-10 | Quantum Channel & Network Manipulation | Affect quantum links, nodes, timing, routing, orchestration or key service |
| QTA-11 | Persistence, Evasion & Evidence Manipulation | Retain access or obscure activity and assessment evidence |
| QTA-12 | Degradation, Denial & Corruption | Reduce key rate, fidelity, accuracy, availability or confidence in results |

## Technique evidence status

Each QTE entry uses one of these labels:

- `established-classical`: known classical weakness directly applicable to the quantum stack;
- `demonstrated-lab`: shown experimentally or through a reproducible proof of concept;
- `documented-implementation-class`: recognized in standards, protection profiles or peer-reviewed surveys;
- `plausible-research`: supported by system properties but not yet sufficiently demonstrated;
- `observed-incident`: supported by a public, attributable incident report.

No evidence label implies universal exploitability. The assessor must establish preconditions for the actual target.

## Attack-path rule

A material scenario should connect:

`actor → access path → QTA tactic → QTE technique → affected asset → security consequence → observable evidence → QSC control → QSTEST result`.

This chain is the minimum traceability unit in Q-SECAT.
