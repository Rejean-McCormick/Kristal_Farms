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
- `database/`, `pipelines/`, `packages/`: application/data foundation and reproducible analysis code.
- `contracts/`: machine-readable API, schema, release, story, layer and policy contracts.
- `data/raw/`: immutable/source data.
- `data/processed/current/`: current derived research outputs with provenance.
- `data/fixtures/current/`: loadable canonical application/data fixtures.
- `data/publish/current/`: current immutable public-release artifacts.
- `docs/00-control` through `docs/50-research`: active Kristal Farms project/research documentation.
- `docs/architecture`, `docs/data`, `docs/product`, etc.: active application implementation documentation.
- `docs/60-application-data`: current application-specific research/data contracts.
- `archive/`: superseded/historical material that must not control active state.

## Separate wiki

`Kristal_Farms.wiki` is a separate Git repository for the public/explanatory GitHub Wiki. It is not the technical source of truth.
