# Contributing to Q-SECAT

Q-SECAT accepts evidence-backed corrections, techniques, controls, tests, mappings and tooling improvements.

## Requirements for catalog changes

1. Use a stable identifier and do not recycle retired identifiers.
2. State the affected domain, preconditions, impact and observable evidence.
3. Cite at least one primary or authoritative source when the claim is externally verifiable.
4. Map every new technique to at least one control and one safe test.
5. Avoid operational instructions that facilitate unauthorized interference with physical or digital systems.
6. Add or update automated tests.

## Development

```bash
python -m pip install -e .[dev]
pytest
python scripts/check_traceability.py
```

## Pull requests

Explain the problem, evidence, design decision, compatibility impact and test results. Sign off commits using `git commit -s` to certify the Developer Certificate of Origin in `DCO.md`.
