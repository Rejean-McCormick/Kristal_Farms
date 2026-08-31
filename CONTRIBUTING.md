# Contributing

See [`docs/contributing/development-workflow.md`](docs/contributing/development-workflow.md) and [`docs/contributing/pull-requests.md`](docs/contributing/pull-requests.md).

## Software / data architecture

Changes to data semantics, architecture, security boundaries, publication rules or public cartographic meaning require accompanying documentation and, when durable, an ADR.

## Research / evidence

Every substantive research change should identify the affected workstream/decision, sources/evidence, numeric claims, unresolved caveats, share-level impact and whether EN/FR synchronization is required. Never overwrite raw source data to “clean it up”; preserve supplied inputs and add transformed data with provenance.

Exploratory code belongs under `research/`. Reproducible production transforms belong under `pipelines/`. A research result must be promoted through validation/contracts before `apps/` or `services/` depend on it; direct runtime imports from `research/` or `pipelines/` are prohibited.

## Human/community programs

Changes concerning host communities, education, language, culture, housing or human infrastructure must identify the relevant rights-holder/community decision process, safeguarding/privacy implications and applicable legal/governance questions.

## Ranking

No contributor may introduce site ranking, traffic-light preference styling or hidden priority scores while `ranking_allowed = false`.
