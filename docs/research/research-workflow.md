# Research workflow

## Objective

Move from external information to traceable Kristal Farms evidence without losing source scope, uncertainty, or superseded states.

## Workflow

```text
question
  ↓
source discovery
  ↓
source registration
  ↓
claim / observation extraction
  ↓
subject linking
  ↓
verification / conflict review
  ↓
QA
  ↓
publish eligibility decision
```

## Research records

A research entry should capture the source and the exact scope of what is supported. Avoid generalizing a source beyond its stated geography, time, asset, or planning context.

## Conflicts

When sources conflict, retain both with dates/scopes and create a conflict/supersession relationship. Do not silently choose the most convenient value.

## Non-findings

Important unresolved questions should be represented explicitly. A non-finding can prevent the UI or model from implying that a missing fact is known.

## Owner direction

Owner direction may establish project intent and screening governance but remains distinct from independent technical evidence.

## Repository boundary

Exploratory research code belongs under the top-level `research/` workspace. Reproducible ingestion, normalization, validation and publication belong under `pipelines/` and the governed data platform.

A research conclusion is not an Observatory input until it has been promoted through a reproducible pipeline/contract and published as governed data. `apps/web` must not import or execute files from `research/` or `pipelines/`.

See [Workspace boundaries](../architecture/workspace-boundaries.md).
