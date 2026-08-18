# Kristal Farms

> **Public working repository — English primary narrative**

Kristal Farms is a northern infrastructure model built around a simple inversion:

> **Bring compute to renewable energy, consume the electricity locally, export digital value by fibre, and reuse the heat.**

The model is designed for remote northern sites where moving electricity to distant markets can require large transmission corridors, substations, access works and long construction schedules. Instead of treating remoteness and cold as disadvantages, Kristal Farms tries to make them part of the infrastructure advantage.

For the class of sites Kristal Farms is designed to select, the goal is a **significantly lower total infrastructure burden** than the realistic alternative of exporting electricity over long distances.

## The qualifying rule

A site should not qualify merely because it has renewable energy. It should demonstrate a strong combination of:

- renewable energy close to the load;
- short local electrical connections;
- cold-climate cooling advantage;
- marine or compact logistics where available;
- a credible fibre export path;
- useful local heat demand;
- low ecological conflict or previously disturbed land;
- community and rights-holder support;
- modularity, reversibility and measurable economics.

**Structural advantage is a site-selection requirement, not a marketing afterthought.**

## Current public narrative

The current public explanation of the project is the English GitHub Wiki source in [`public-wiki/`](public-wiki/Home.md).

Start with:

1. [`Home`](public-wiki/Home.md)
2. [`The Core Idea`](public-wiki/The-Core-Idea.md)
3. [`Structural Cost Advantage`](public-wiki/Structural-Cost-Advantage.md)
4. [`Transmission vs Digital Export`](public-wiki/Transmission-vs-Digital-Export.md)
5. [`Cold Climate Cooling`](public-wiki/Cold-Climate-Cooling.md)
6. [`Heat First`](public-wiki/Heat-First.md)
7. [`Fibre as the Export Corridor`](public-wiki/Fibre-as-the-Export-Corridor.md)
8. [`Secure Compute and Black-Box Tenancy`](public-wiki/Secure-Compute-and-Black-Box-Tenancy.md)
9. [`Environmental Design and Site Selection`](public-wiki/Environmental-Design-and-Site-Selection.md)
10. [`What Is Validated and What Is Being Tested`](public-wiki/What-Is-Validated-and-What-Is-Being-Tested.md)
11. [`Source Basis`](public-wiki/Source-Basis.md)

The wiki is a **narrative layer**, not a replacement for the technical and source material below.

## Evidence base

The main evidence families already in this repository are:

- [`Kristal_Farms_Internal_Reference.md`](docs/10-core/Kristal_Farms_Internal_Reference.md) — detailed baseline architecture, heat-first system, modular pads, fibre, black-box tenancy, governance, metrics and reversibility;
- [`deployment/`](docs/10-core/deployment/) — gradual and harmonious deployment plans;
- [`docs/20-partner-package/en/markdown/`](docs/20-partner-package/en/markdown/) — inherited numbered Nain/Labrador partner package;
- [`docs/30-site-screening/`](docs/30-site-screening/) — Labrador, Nunavik and climate screening;
- [`docs/40-economics/`](docs/40-economics/) — transmission, cooling and economic working studies;
- [`data/raw/`](data/raw/) — supplied CSV/XLSX datasets;
- [`sources/originals/`](sources/originals/) — supplied original analysis files;
- [`sources/legacy/`](sources/legacy/) — earlier source archive and supporting material;
- [`sources/owner-direction/`](sources/owner-direction/) — recorded project-owner strategic direction.

See [`NARRATIVE_SOURCE_MAP.md`](docs/00-control/NARRATIVE_SOURCE_MAP.md) for the direct map between wiki topics and repository sources.

## Current project state

The supplied documentation consistently develops these design principles:

- local consumption of renewable power;
- short local electrical integration;
- modular containerized compute pads;
- heat-first operation;
- closed-loop/non-contact cooling;
- black-box tenancy;
- fibre as the compute-export path;
- staged expansion;
- community governance/FPIC;
- public metrics;
- reversibility and restoration.

Nain remains the **first application** in the partner package. A preliminary **15–20 MW Fraser River concept** exists in the screening material, but it is not construction-ready and still requires hydrology, engineering, fibre, environmental, community and economic validation.

Strategic opportunities still being tested include exact site-specific cost advantage, lifecycle ecological comparison, subsea fibre, a northern fibre network, secure mine/brownfield sites, future AI demand, international university institutions and long-term welcoming-community programs.

## Confidence model

The repository uses the confidence levels defined in the public wiki:

1. **Design principle** — deliberate part of the architecture or governance model.
2. **Working assumption** — number or condition used to test economics or engineering.
3. **Screening evidence** — information used to decide what deserves deeper study.
4. **Strategic hypothesis** — direction worth investigating but not yet proven.
5. **Validated site fact** — supported by current site-specific engineering, legal, environmental, commercial or community evidence.
6. **Operational result** — measured performance from a functioning project.

The goal is not to remove uncertainty. It is to **label uncertainty correctly**.

## Control layer

For project state and orchestration, use:

- [`PROJECT_STATE.md`](docs/00-control/PROJECT_STATE.md)
- [`DOCUMENT_AUTHORITY.md`](docs/00-control/DOCUMENT_AUTHORITY.md)
- [`DECISIONS_REQUIRED.md`](docs/00-control/DECISIONS_REQUIRED.md)
- [`CLAIMS_TO_VALIDATE.md`](docs/00-control/CLAIMS_TO_VALIDATE.md)
- [`WORKSTREAMS.md`](docs/00-control/WORKSTREAMS.md)
- [`NARRATIVE_SOURCE_MAP.md`](docs/00-control/NARRATIVE_SOURCE_MAP.md)
- [`PUBLICATION_POLICY.md`](docs/00-control/PUBLICATION_POLICY.md)
- [`SOURCE_TRACEABILITY.md`](docs/00-control/SOURCE_TRACEABILITY.md)
- [`DATA_CATALOG.md`](data/catalog/DATA_CATALOG.md)

## Repository structure

```text
.
├── public-wiki/                  # Current public English narrative
├── docs/
│   ├── 00-control/               # State, authority, decisions, validation, orchestration
│   ├── 10-core/                  # Detailed architecture, deployment, dignity/education frameworks
│   ├── 20-partner-package/       # Inherited v1 Nain/Labrador partner deliverables
│   ├── 30-site-screening/        # Labrador, Nunavik, climate and infrastructure screening
│   ├── 40-economics/             # Working cost/transmission/cooling studies
│   └── 50-research/              # Supporting research
├── data/
│   ├── raw/                      # Supplied structured data, preserved
│   └── catalog/                  # Data and file manifests
├── sources/
│   ├── originals/                # Supplied originals
│   ├── extracted/                # Searchable extracts
│   ├── legacy/                   # Previous source material
│   └── owner-direction/          # Recorded project direction
└── archive/                      # Superseded repository/narrative layers retained for history
```

## Public working repository

Kristal Farms is intended to be developed transparently. A public repository can include unfinished research without pretending it is final.

Do not commit credentials, private tenant data, personal information, legally restricted third-party material, confidential rights-holder information, or operational-security details whose publication would create a credible risk. See [`PUBLICATION_POLICY.md`](docs/00-control/PUBLICATION_POLICY.md).

No open-source or open-document licence is assigned by this repository state.

## Scope boundary

Kristal Farms is an infrastructure, compute, energy, fibre, heat, community, knowledge and education-capability project. Separatism, border revision, sovereignty disputes and territorial-status strategies are outside the operational project scope. See [`SCOPE_BOUNDARIES.md`](docs/00-control/SCOPE_BOUNDARIES.md).
