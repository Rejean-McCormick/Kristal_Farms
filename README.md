# Kristal Farms

> Northern energy / compute / fibre research, evidence system, geospatial application, and scenario-analysis monorepo.

## Canonical repository

This is the **single canonical Kristal Farms repository**. It consolidates:

- the cumulative research/evidence program through Pass 14;
- the PostGIS/application data model developed in Passes 11–14;
- the supplied Kristal Farms application documentation v0.1;
- database migrations, ingestion/validation/economic pipelines, schemas, catalog configuration, fixtures and public-release artifacts;
- the target implementation structure for Showcase, Explorer and Scenario Studio.

The GitHub Wiki is intentionally a **separate repository**: `Kristal_Farms.wiki`.

## Naming boundary

**Kristal Farms is not the Kristal/Kristals semantic-knowledge system.**

Kristal Farms may host many kinds of compute workloads. Kristals may be hosted or used elsewhere. There is no architectural dependency between the two projects.

The working name `kristal-platform` / “Kristal Geospatial Platform” used during Passes 11–14 is **superseded**. Its useful code, migrations and data contracts are absorbed here as Kristal Farms application/data infrastructure. The old wording is retained only in `archive/naming-superseded/` for provenance.

## Product surfaces

1. **Showcase** — public narrative experience.
2. **Explorer** — evidence-first professional map and data interface.
3. **Scenario Studio** — reproducible scenario comparison and economics.

All three share the same canonical data model. PostGIS is the intended operational source of truth; GeoJSON/PMTiles/COG and similar outputs are published artifacts.

## Repository layout

```text
kristal-farms/
├── apps/web/
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
├── database/
├── contracts/
├── data/
├── docs/
├── sources/
├── tests/
├── scripts/
├── infra/
└── archive/
```

## Start here

### Application / implementation

- [`docs/product/vision.md`](docs/product/vision.md)
- [`docs/architecture/overview.md`](docs/architecture/overview.md)
- [`docs/architecture/repository-structure.md`](docs/architecture/repository-structure.md)
- [`docs/data/data-model.md`](docs/data/data-model.md)
- [`docs/data/evidence-model.md`](docs/data/evidence-model.md)
- [`docs/product/explorer.md`](docs/product/explorer.md)
- [`docs/product/showcase.md`](docs/product/showcase.md)
- [`docs/product/scenario-studio.md`](docs/product/scenario-studio.md)

### Kristal Farms research / project state

- [`docs/00-control/PROJECT_STATE.md`](docs/00-control/PROJECT_STATE.md)
- [`docs/00-control/MASTER_INDEX.md`](docs/00-control/MASTER_INDEX.md)
- [`docs/10-core/Kristal_Farms_Reference_Architecture_EN.md`](docs/10-core/Kristal_Farms_Reference_Architecture_EN.md)
- [`docs/10-core/Architecture_de_reference_Kristal_Farms_FR.md`](docs/10-core/Architecture_de_reference_Kristal_Farms_FR.md)
- [`docs/40-economics/`](docs/40-economics/)
- [`docs/50-research/`](docs/50-research/)
- [`docs/60-application-data/`](docs/60-application-data/)

## Current research governance

- screening mode: **unranked**;
- `ranking_allowed = false`;
- existing autonomous-grid planning margin is **not** compute-hosting capacity;
- community loads are priority loads;
- multi-MW Kristal Farms concepts require their own generation/electrical architecture;
- external renewable projects are references unless explicitly reclassified;
- evidence may be valid without geometry;
- unknown values stay unknown rather than being silently filled.

## Implementation status

The repository contains a mature research/evidence baseline, PostGIS migrations/contracts, operational research pipelines and publish fixtures, but **does not contain a completed production web application or API service**. The `apps/` and `services/` directories are implementation homes defined by the supplied application architecture, not invented completed software.

## Wiki

The explanatory/public wiki is maintained separately in the **`Kristal_Farms.wiki`** repository. It is not the source of truth for technical/evidence state.
