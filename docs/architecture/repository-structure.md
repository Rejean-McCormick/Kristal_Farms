# Repository structure

Kristal Farms uses **one canonical monorepo with three logical systems**. The GitHub Wiki is the only intentionally separate repository.

```text
kristal-farms/
├── research/               # Knowledge: exploratory/non-runtime work
│   ├── hydrology/
│   ├── energy/
│   ├── communities/
│   └── experiments/
├── pipelines/              # Data platform: reproducible ingest/transform/QA/publish
│   ├── ingest/
│   ├── transform/
│   ├── validate/
│   ├── economics/
│   └── publish/
├── database/               # Data platform: PostGIS operational source of truth
├── contracts/              # Data platform: machine-readable boundaries
├── packages/               # Stable schemas/catalog/map-style/shared packages
├── data/
│   ├── raw/
│   ├── processed/
│   ├── fixtures/
│   ├── publish/
│   ├── catalog/
│   └── examples/
├── apps/
│   └── web/                # Product: Showcase / Observatory / Scenario Studio
├── services/
│   ├── kristal-farms-api/
│   ├── ogc-api/
│   └── tiles/
├── docs/
├── tools/                  # Specialist local/developer utilities
├── sources/
├── tests/
├── infra/
├── archive/
└── .github/
```

## Logical system 1 — Knowledge / research

- `research/`: active exploratory code, notebooks, candidate analysis and methodological experiments.
- `sources/`: controlled source material and owner-direction records.
- `docs/00-control`, `docs/10-core`, `docs/30-site-screening`, `docs/40-economics`, `docs/50-research` and `docs/70-long-horizon`: project/domain documentation organized by authority and maturity.
- `archive/`: superseded/historical research that must not control active state.

Research can be incomplete. It is not a runtime dependency and it is not publishable merely because it is committed.

## Logical system 2 — Data platform / contract

- `database/`: canonical operational PostGIS schemas and views.
- `pipelines/`: reproducible ingest, transform, validation, economics and publish logic.
- `contracts/`: machine-readable API, schema, release, story, layer and policy contracts.
- `packages/`: stable schemas, catalog, cartographic semantics and shared implementation packages.
- `data/raw/`: source-faithful/controlled input artifacts.
- `data/processed/current/`: current derived research outputs with provenance.
- `data/fixtures/current/`: loadable canonical development/application fixtures.
- `data/publish/current/`: current immutable public-release artifacts.

This system turns research into reproducible, governed data.

## Logical system 3 — Product

- `apps/web/`: Showcase, Explorer/Observatory and Scenario Studio implementation.
- `services/`: domain API, OGC API and tile delivery.
- `docs/architecture`, `docs/data`, `docs/product`, `docs/frontend`, `docs/api`, `docs/scenarios`, etc.: software/data-platform implementation documentation organized by responsibility.

Product code consumes governed APIs/tiles, stable packages/contracts or immutable publish artifacts. It must not import or execute `research/` or `pipelines/`. Specialist local utilities live under `tools/`; only the canonical rebuild and quick-start launchers remain at repository root.

## Direction of dependency

```text
research
   ↓ promote/review
data platform + contracts
   ↓ publish/API/tiles
product
```

See [Information architecture](information-architecture.md), [Workspace boundaries](workspace-boundaries.md) and [ADR-020](../adr/0020-one-monorepo-three-logical-systems.md).

## Separate wiki

`Kristal_Farms.wiki` is a separate Git repository for the public/explanatory GitHub Wiki. It is not the technical source of truth.
