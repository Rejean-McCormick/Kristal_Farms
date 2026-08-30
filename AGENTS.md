# AGENTS.md — Instructions for AI coding agents

This file is a high-priority implementation contract for any AI agent modifying the Kristal Farms repository.

## Product intent

Kristal Farms is not a generic mapping demo. It is an evidence-driven geospatial platform with a public promotional surface and a professional technical surface sharing the same data model.

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
