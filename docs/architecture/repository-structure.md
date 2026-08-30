# Repository structure

Kristal Farms uses **one canonical monorepo**. The GitHub Wiki is the only intentionally separate repository.

```text
kristal-farms/
├── apps/
│   └── web/
├── services/
│   ├── kristal-farms-api/
│   ├── ogc-api/
│   └── tiles/
├── packages/
│   ├── schemas/
│   ├── catalog/
│   ├── map-style/
│   ├── ui/
│   ├── showcase/
│   └── shared/
├── pipelines/
│   ├── ingest/
│   ├── transform/
│   ├── validate/
│   ├── economics/
│   └── publish/
├── database/
│   ├── migrations/
│   ├── functions/
│   ├── views/
│   └── seeds/
├── contracts/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── fixtures/
│   ├── publish/
│   ├── catalog/
│   ├── examples/
│   └── legacy/
├── docs/
├── sources/
├── scripts/
├── tests/
├── infra/
├── archive/
└── .github/
```

## What belongs where

- `apps/`, `services/`: production implementation homes. They are scaffold-only until actual code is written.
- `database/`, `pipelines/`, `packages/`: application/data foundation developed through Pass 14.
- `contracts/`: machine-readable API, schema, release, story, layer and policy contracts.
- `data/raw/`: immutable/source data.
- `data/processed/`: pass/research outputs with provenance.
- `data/fixtures/`: loadable canonical app/data fixtures.
- `data/publish/`: immutable public-release artifacts.
- `docs/00-control` through `docs/50-research`: cumulative Kristal Farms research/program documentation.
- `docs/architecture`, `docs/data`, `docs/product`, etc.: active application implementation documentation.
- `docs/60-application-data`: migration/data-contract documents from Passes 11–14, renamed into Kristal Farms terminology.
- `archive/`: superseded/historical material that must not control active state.

## Separate wiki

`Kristal_Farms.wiki` is a separate Git repository for the public/explanatory GitHub Wiki. It is not the technical source of truth.
