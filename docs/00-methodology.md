# Q-SECAT Methodology Specification

## 1. Purpose

Q-SECAT provides a repeatable method for evaluating cyber risk across classical, post-quantum and quantum system components. It is designed for architecture reviews, readiness assessments, product security, procurement, red-team planning in authorized environments, laboratory validation and independent assurance preparation.

The unit of analysis is an **assessment object**: a bounded system, service, device, protocol, workflow or organizational capability with a named owner and explicit authorization.

## 2. Required outputs

Every complete assessment produces:

- scope, assumptions, exclusions and authorization record;
- asset and dependency inventory;
- data-lifetime and mission-impact profile;
- QSD domain applicability statement;
- QTA/QTE threat model;
- QSC control applicability and implementation state;
- QSTEST plan and results;
- evidence register with provenance and assurance level;
- residual-risk register with confidence interval;
- treatment plan, owner, due date and revalidation trigger.

## 3. Lifecycle

### Phase 0 — Authorization and safety

Define owner, legal authority, laboratory safety boundaries, data handling, third-party restrictions, stop conditions and responsible disclosure route. Physical interference, optical injection, electromagnetic experimentation or changes to production calibration are out of scope unless a qualified facility has explicitly approved them.

### Phase 1 — System decomposition

Model the system as six interacting planes:

1. **Business and mission plane** — purpose, decisions, safety and data lifetime.
2. **Classical digital plane** — identity, API, network, operating system, cloud and storage.
3. **Quantum logical plane** — algorithms, circuits, protocols, error mitigation/correction and measurement semantics.
4. **Quantum physical plane** — qubits, photons, sensors, memories, transducers and channels.
5. **Control and support plane** — firmware, electronics, calibration, timing, cryogenics and laboratory systems.
6. **Supply and assurance plane** — vendors, components, build systems, updates, attestation and certification.

### Phase 2 — Inventory and criticality

For each asset record owner, version, location, trust boundary, dependencies, cryptography, data classification, confidentiality lifetime, integrity/availability/safety requirements, update mechanism and evidence source. Use CBOM/SBOM/HBOM representations where available.

### Phase 3 — Domain selection

Mark each of the 12 QSD domains as:

- `applicable` — material to the assessment;
- `inherited` — controlled by another service or provider;
- `not_applicable` — justified exclusion;
- `unknown` — insufficient evidence, which creates an assessment gap.

### Phase 4 — Threat modeling

Select QTE techniques using architecture, assets, trust boundaries and plausible attacker objectives. Record preconditions, affected security property, observables, existing controls and uncertainty. Classical attack paths must be included because most quantum services depend on classical control infrastructure.

### Phase 5 — Control selection

A QSC control is applicable when it reduces the likelihood or impact of one or more selected techniques. Controls are written as outcomes, not vendor features. An implementation claim must have an owner, scope and evidence.

### Phase 6 — Test design and execution

Choose a QSTEST procedure for each material technique/control pair. Start with the least intrusive method that can produce sufficient evidence:

1. documentary review;
2. static analysis and configuration inspection;
3. simulation or emulation;
4. isolated software/hardware testbed;
5. controlled laboratory experiment;
6. independent evaluation or certification.

Record prerequisites, dataset, tools and versions, baseline, expected result, actual result, limitations and artifact hashes.

### Phase 7 — Scoring and assurance

Calculate impact, likelihood, control effectiveness and residual risk with `qsecat score`. Assign QAL and evidence confidence separately. Scores prioritize work; they do not substitute expert judgment.

### Phase 8 — Treatment and revalidation

Choose avoid, reduce, transfer/contractually allocate or accept. Define measurable exit criteria. Revalidate on material architecture changes, provider changes, protocol/algorithm updates, new threat evidence, failed controls, incidents or expiry of evidence.

## 4. Roles

| Role | Accountability |
|---|---|
| Assessment sponsor | Purpose, risk acceptance and resources |
| System owner | Scope, inventory and remediation ownership |
| Quantum subject-matter expert | Physical/logical validity and laboratory safety |
| Cybersecurity assessor | Threat, control, test and evidence quality |
| Cryptography lead | Algorithm, key, protocol and migration decisions |
| Safety/legal/privacy representatives | Constraints and impact review |
| Independent reviewer | Challenge assumptions and verify reproducibility |

One person may hold multiple roles in a small assessment, but conflicts of interest must be declared.

## 5. Conformance language

- **MUST**: required for a Q-SECAT conformant assessment.
- **SHOULD**: expected unless a documented reason justifies deviation.
- **MAY**: optional based on context.

A report may claim “Q-SECAT assessment performed” only if it includes scope, domain applicability, risk entries, evidence and limitations. It must not claim Q-SECAT certification.
