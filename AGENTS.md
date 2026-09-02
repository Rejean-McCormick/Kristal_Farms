# AGENTS.md — Instructions for AI coding agents

This file is a high-priority implementation contract for any AI agent modifying the Kristal Farms repository.

## Product intent

Kristal Farms is a physical northern energy/compute/fibre infrastructure project supported by an evidence-driven geospatial application. The Showcase, Explorer and Scenario Studio share the same governed data model; the software exists to explain, evaluate and develop Kristal Farms rather than becoming a separate product identity.

## Non-negotiable architecture rules

1. **PostGIS is the operational source of truth.** Do not move canonical data into frontend constants or static JSON modules.
2. **Standard layers are catalog-driven.** Do not create one custom React component per dataset unless the layer requires genuinely unique interaction.
3. **Evidence is not geometry.** Claims, observations, and sources remain separate from places/assets/projects and may have no geometry.
4. **Scenarios are not observations.** Never write scenario assumptions into canonical observed-data tables.
5. **Planning margin is not compute capacity.** Never derive `available_compute_mw` from planning-margin data.
6. **Community load is priority.** Scenario logic must curtail flexible compute before essential community demand.
7. **No ranking while prohibited.** If policy says `ranking_allowed: false`, do not create score, rank, traffic-light styling, ordering, or badges that imply preference.
8. **External reference projects remain references** unless a governed data change explicitly changes their role.
9. **Public/private separation happens before publication.** Never place restricted records in public PMTiles/COG artifacts and rely on frontend hiding.
10. **The model layer owns business rules.** React components should present results, not implement scientific or regulatory logic.
11. **Respect the three-system boundary.** `research/` is exploratory, the data platform publishes governed contracts, and `apps/`/`services/` consume them. Product runtime code must not import or execute `research/` or `pipelines/`.
12. **Published artifacts are read-only product inputs.** Development bridges may read `data/publish/...`; product code must not mutate published artifacts or reach into `data/raw/`.

## Preferred implementation pattern

```text
UI -> typed client -> API / tiles -> PostGIS
                      |
                      -> scenario engine
```

Use shared schemas and generated types where practical. All material data-model changes require a migration and documentation update.

## Definition of done for a feature

A feature is not complete until it has, where applicable:

- typed contract;
- validation;
- tests;
- provenance behavior;
- permission behavior;
- URL/share-state behavior;
- documentation update;
- accessibility review;
- data QA implications reviewed.

## Before changing architecture

Read the relevant ADRs under `docs/adr/`. If the proposed change reverses or materially changes an accepted ADR, create a new superseding ADR instead of silently editing history.

## Data imports

Imports must pass through `raw -> staging -> core/research -> publish`. Preserve source identifiers and original source values when feasible. Do not silently normalize away ambiguity.

## Cartography

Visual design may be expressive, but uncertainty and hypothesis must remain visible. Do not make conceptual corridors look identical to verified infrastructure. Do not imply precision beyond the source geometry.

## AI-generated code

AI-generated implementation is acceptable, but generated code must obey the same tests, typing, schema, migration, and review expectations as human-written code. Avoid large opaque generated modules when a declarative configuration or reusable abstraction is clearer.

## Active-state search discipline

Treat `archive/` as historical provenance, not active implementation context. Do not search, summarize or copy architecture from `archive/` unless the task explicitly asks for history, migration provenance or superseded behavior. The root `.ignore` excludes `archive/` from common local search/index tools by default.

When documentation location is ambiguous, use the two-axis model in `docs/architecture/information-architecture.md`: numbered folders are project/domain authority and research maturity; responsibility folders (`architecture`, `data`, `product`, `frontend`, `api`, `scenarios`, etc.) are software/data-platform documentation.
