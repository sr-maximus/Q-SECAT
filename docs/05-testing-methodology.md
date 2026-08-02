# Security Testing Methodology

## Test philosophy

A Q-SECAT test verifies a claim against explicit acceptance criteria. It is not merely a scanner invocation. Tests are designed to be safe, repeatable and proportional to the system's maturity.

## Test classes

| Class | Typical methods | Default environment |
|---|---|---|
| T1 Documentary | policy, architecture, contract, provenance and evidence review | Non-invasive |
| T2 Static | configuration, code, dependency, CBOM/SBOM and schema inspection | Offline/read-only |
| T3 Simulation | circuit, protocol, noise, failure and migration simulation | Simulator/emulator |
| T4 Isolated integration | API, interoperability, key lifecycle and workflow tests | Dedicated test tenant/lab |
| T5 Controlled physical | calibrated environmental, hardware or optical validation | Authorized specialist laboratory |
| T6 Independent assurance | third-party reproduction, Common Criteria or other scheme | Independent evaluator |

## Mandatory test record

- test ID and version;
- authorization and target identifier;
- linked QTE and QSC IDs;
- hypothesis and acceptance criteria;
- method, tools, versions and configuration;
- data set or generated workload;
- baseline and comparison method;
- result: pass, fail, partial, inconclusive or not run;
- evidence URIs and hashes;
- limitations, uncertainty and side effects;
- tester, reviewer and timestamps.

## Safety rules

- Use simulators and synthetic workloads before hardware.
- Never test shared production resources without provider approval and tenant isolation.
- Never alter production calibration, optical power, environmental conditions or timing references without a written laboratory procedure and stop conditions.
- Do not collect other tenants' data or infer workload content.
- Sanitize circuit IP, keys, credentials, measurement data and supplier information.
- Stop on unexpected safety, stability, availability or data-exposure effects.

## Result interpretation

A pass demonstrates only the tested claim under recorded conditions. An inconclusive result is not a pass. A failed control with low-quality evidence remains a failure candidate and should be prioritized for better evidence rather than discounted.

## Reproducibility

For T3–T6 tests, store enough metadata to reproduce the result: random seeds, backend identifier, calibration snapshot, circuit hash, compiler version, number of shots/samples, confidence method and environmental constraints. Raw sensitive evidence may remain in a protected repository; Q-SECAT can retain a signed manifest and hash.
