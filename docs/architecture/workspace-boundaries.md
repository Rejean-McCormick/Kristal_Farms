# Workspace boundaries

Kristal Farms uses **one physical monorepo with three logical systems**.

This is an architectural boundary, not merely a folder convention.

## The three systems

```text
┌──────────────────────────────────────────────────────────────┐
│ 1. KNOWLEDGE / RESEARCH                                     │
│ research/ · sources/ · research documentation               │
│ exploratory, evidence-seeking, non-runtime                   │
└──────────────────────────────┬───────────────────────────────┘
                               │ reviewed promotion
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ 2. DATA PLATFORM / CONTRACT                                 │
│ pipelines/ · database/ · contracts/ · packages/ · data/     │
│ reproducible ingest, validation, canonicalization, publish   │
└──────────────────────────────┬───────────────────────────────┘
                               │ governed API/release contract
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ 3. PRODUCT                                                  │
│ apps/ · services/                                           │
│ Showcase, Explorer/Observatory, Scenario Studio              │
└──────────────────────────────────────────────────────────────┘
```

## Dependency rules

### Product (`apps/`, `services/`)

Product code:

- **MAY** depend on stable contracts and packages under `packages/` and `contracts/`;
- **MAY** consume `data/publish/...` as an immutable development/release artifact;
- **MAY** consume governed APIs/tiles backed by PostGIS;
- **MUST NOT** import or execute code from `research/`;
- **MUST NOT** import or execute ETL/analysis code from `pipelines/`;
- **MUST NOT** read `data/raw/` or ad-hoc research outputs at runtime;
- **MUST** treat published data as read-only.

The production target remains:

```text
UI -> typed client -> API / tiles -> PostGIS
```

The current Observatory vertical slice is allowed to read immutable files under `data/publish/current` server-side while services are still being activated. This is a development bridge, not a new canonical source of truth.

### Data platform (`pipelines/`, `database/`, `contracts/`, `packages/`, `data/`)

The data platform:

- **MAY** consume registered source material and promoted research inputs;
- **MUST** make transforms reproducible;
- **MUST** preserve provenance and uncertainty;
- **MUST** validate before publishing;
- **MUST NOT** rely on React/UI code for scientific or business rules;
- **MUST** separate raw, processed/canonical and publish states.

`data/publish/` is the artifact boundary for file-based consumers. PostGIS `publish` views and governed APIs are the service boundary for runtime consumers.

### Knowledge / research (`research/`)

Research:

- **MAY** be exploratory and incomplete;
- **MAY** generate candidate outputs and hypotheses;
- **MUST** label assumptions and source scope;
- **MUST NOT** be imported by product runtime code;
- **MUST NOT** become public/canonical merely by being committed;
- **MUST** be promoted through a reproducible pipeline before becoming a product data dependency.

## Promotion flow

```text
question / source
      ↓
research exploration
      ↓
reviewed method or result
      ↓
pipeline / canonical model
      ↓
validation + evidence QA
      ↓
publish view or immutable release
      ↓
API / tiles / public artifact
      ↓
Observatory
```

A shortcut from `research/` directly to `apps/web/` is an architecture violation.

## Hydrology example

The river work illustrates the boundary:

- candidate/source exploration may happen under `research/hydrology/`;
- official HYDAT/GeoMet retrieval and reproducible geometry workflows remain under `pipelines/ingest/`;
- normalization and validation belong to the data platform;
- publishable station/community outputs live under `data/publish/current`;
- Observatory renders those outputs and their evidence semantics, but does not know how HYDAT was fetched or how candidate rivers were selected.

## Why one repo

One monorepo keeps contracts, pipelines, data artifacts, application changes, tests and ADRs reviewable together while the project is still evolving quickly. The logical boundaries preserve the option to split repositories later without paying the coordination cost now.

A physical split becomes reasonable when deployment ownership, teams, release cadence or external consumers require independent versioning. Until then, the monorepo is canonical.
