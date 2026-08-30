# Kristal Farms

Kristal Farms is a northern energy-and-compute infrastructure project built around a simple inversion:

> **Bring flexible compute to remote renewable energy and export digital value by fibre instead of defaulting to long roads and long high-voltage export corridors.**

The project focuses on northern Québec and Labrador, where hydro resources, marine logistics, community infrastructure and telecommunications can be evaluated as one system.

## What Kristal Farms is

Kristal Farms combines four infrastructure layers:

1. **Remote renewable generation** — primarily hydro where technically, environmentally and socially justified.
2. **Protected community interface** — community and critical loads have priority over flexible compute.
3. **Serviced compute sites** — power, cooling interface, fibre handoff, physical security, metering and logistics; tenants may bring and control their own hardware and software.
4. **Digital export by fibre** — move computation and data products rather than defaulting to long-distance electrical export.

Marine access, local roads, heat reuse, storage and short electrical interties are site-specific components, not universal requirements.

## Application

The repository also contains the architecture and data contracts for the Kristal Farms application:

- **Showcase** — guided public narrative;
- **Explorer** — evidence-first professional geospatial workspace;
- **Scenario Studio** — reproducible infrastructure and economic comparisons.

The application is data-driven. PostgreSQL/PostGIS is the intended operational source of truth; MapLibre/deck.gl, OGC APIs, QGIS workflows and immutable public releases consume derived views and artifacts.

## Evidence discipline

The repository deliberately separates facts, observations, derived values, assumptions and unknowns.

Core rules:

- planning margin is **not** validated compute-hosting capacity;
- community loads are priority loads;
- external projects are references unless explicitly reclassified;
- evidence may be valid without geometry;
- a gauge point is not a dam site;
- terrain drop is not project head;
- a benchmark is not a site cost;
- unknown or unpriced values remain explicit;
- site ranking is disabled until a transparent methodology and governance decision exist.

## Repository layout

```text
kristal-farms/
├── apps/                   # Web application implementation home
├── services/               # Domain API, OGC API and tile services
├── packages/               # Schemas, catalog, map style, UI/shared packages
├── database/               # PostGIS migrations, views, functions and seeds
├── pipelines/              # Ingestion, transformation, validation and economics
├── contracts/              # Machine-readable API/data/policy contracts
├── data/                   # Current fixtures, public releases and controlled inputs
├── docs/                   # Product, architecture, domain and research documentation
├── sources/                # Controlled source material and project-direction records
├── tests/                  # Automated model/data/economic tests
├── infra/                  # Deployment configuration
└── archive/                # Superseded material and historical research snapshots
```

## Start here

### Project and domain

- [Project state](docs/00-control/PROJECT_STATE.md)
- [Strategic principles](docs/00-control/STRATEGIC_PRINCIPLES.md)
- [Reference architecture — English](docs/10-core/Kristal_Farms_Reference_Architecture_EN.md)
- [Architecture de référence — français](docs/10-core/Architecture_de_reference_Kristal_Farms_FR.md)
- [Deployment strategy — English](docs/10-core/deployment/DEPLOYMENT_STRATEGY_EN.md)
- [Stratégie de déploiement — français](docs/10-core/deployment/STRATEGIE_DE_DEPLOIEMENT_FR.md)
- [Corridor dossier strategy](docs/00-control/CORRIDOR_DOSSIER_STRATEGY.md)

### Application and data

- [Documentation index](docs/index.md)
- [Product vision](docs/product/vision.md)
- [Architecture overview](docs/architecture/overview.md)
- [Data model](docs/data/data-model.md)
- [Evidence model](docs/data/evidence-model.md)
- [Explorer](docs/product/explorer.md)
- [Showcase](docs/product/showcase.md)
- [Scenario Studio](docs/product/scenario-studio.md)

### Research methods

- [Hydro Resource Atlas method](docs/30-site-screening/hydro-atlas/HYDRO_RESOURCE_ATLAS_METHOD.md)
- [Hydro geometry pipeline](docs/30-site-screening/hydro-atlas/GEOMETRY_PIPELINE_METHOD.md)
- [Economic architecture frontier](docs/40-economics/ECONOMIC_ARCHITECTURE_FRONTIER.md)
- [Economic benchmark register](docs/40-economics/ECONOMIC_BENCHMARK_REGISTER.md)

## Current status

The repository contains a substantial evidence base, current canonical fixtures, reproducible research pipelines, PostGIS schema/migrations, economic sensitivity tooling and public-release artifacts. It does **not** yet establish a selected project site, buildable hydro capacity, environmental authorization, community authorization, fibre route, heavy-lift logistics plan or bankable project economics.

Development now proceeds through named **corridor and site dossiers** that replace general proxies with real geometry, hydrology, engineering, logistics, rights/governance work, commercial quotations and project-specific economics.

## Wiki

The GitHub Wiki is maintained as a separate repository: `Kristal_Farms.wiki`. It is an explanatory surface, not the technical source of truth.

## Long-horizon concepts

Optional human-infrastructure, learning and education concepts are isolated under [`docs/70-long-horizon/`](docs/70-long-horizon/README.md). They are not prerequisites for the first energy/compute project and must not be presented as committed institutions or programs.
