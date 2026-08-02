# Governance Model

## Initial stewardship

The initial community draft is stewarded by Edwin Javier Peñuela Camacho as creator and principal author. Stewardship includes identifier allocation, release approval, evidence-quality review and resolution of safety concerns.

## Decision principles

1. Evidence outranks popularity or vendor interest.
2. Stable identifiers are never silently repurposed.
3. Hypotheses remain clearly labeled until stronger evidence exists.
4. Changes that reduce safe-testing constraints require enhanced review.
5. Conflicts of interest are declared in the pull request or decision record.

## Change classes

- **Editorial:** language or formatting with no semantic change.
- **Compatible:** new optional metadata, mappings, references or tests.
- **Catalog-semantic:** technique/control/test meaning or relationship change.
- **Breaking:** identifier behavior, schema or risk-model incompatibility.

Catalog-semantic and breaking changes require a public rationale and release note. A future multi-stakeholder technical steering group should replace single-maintainer release authority before version 1.0.
