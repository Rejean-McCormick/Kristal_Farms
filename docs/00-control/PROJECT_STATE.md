# Project State

**As of:** 2026-08-31  
**Status:** Active research and development baseline. This document is not an engineering approval, environmental conclusion, community authorization, market forecast or investment decision.

## Core project thesis

Kristal Farms is a northern hydro/renewable resource-access architecture. The primary design question is whether some remote energy resources can be developed more effectively by bringing flexible compute to the energy and exporting digital value by fibre, rather than defaulting to long roads and long high-voltage electrical export corridors.

The architecture under study is:

> **new remote generation → protected community interface → flexible local compute → fibre export**

Community and critical loads have priority over interruptible compute.

## Geography

- **Côte-Nord** is the pilot/learning geography because it can provide northern operating conditions while retaining comparatively practical logistics and services for early learning.
- **Northern Québec and Labrador** are the longer-term resource geography, where distance from roads and major electrical corridors creates the strongest structural contrast.
- No active site is currently ranked or selected.

## Physical architecture

Three compute layouts remain valid:

1. generation-side;
2. community/port-side;
3. split/hybrid.

Selection depends on electrical distance, fibre, marine/ground logistics, maintenance, environment, security, heat value and host-community preference.

## Compute commercial model

Kristal Farms can provide serviced compute sites rather than owning every server. Shared infrastructure may provide power handoff, cooling interface, fibre handoff, security, metering/telemetry and logistics. Tenants can retain control of their hardware, operating systems, models, data, logs and cryptographic keys.

## International tenancy and confidentiality

International tenants are an intended market, subject to a selective counterparty-governance policy. The current owner-directed policy excludes United States-based or United States-controlled counterparties from tenant, anchor-offtaker and tenant-operator roles. Other jurisdictions default to enhanced due diligence until an explicit eligibility posture is documented.

The normal service boundary is a **tenant-controlled encrypted environment** (black-box tenancy): Kristal Farms operates agreed shared physical services and minimum necessary service telemetry while the tenant controls private compute, models, datasets and cryptographic keys. Routine content inspection is not part of the operating model.

No organization in the research prospect inventory should be presented as interested, committed or contracted without direct commercial evidence.

## Mine infrastructure reuse and storage

Kristal Farms may evaluate existing mining assets as an **optional infrastructure-reuse pathway**, not as a project prerequisite. Two distinct hypotheses are active at research level:

1. recently closed, suspended or care-and-maintenance underground mines may retain ramps, shafts, electrical distribution, pumping, ventilation, communications, camps, roads or other infrastructure that could reduce new-build scope for a compute node;
2. open-pit mines — including historical/old mines — may be screened as possible upper or lower reservoirs for pumped-storage hydropower where usable volume, head, geotechnics, hydrogeology, environment, rights/governance and system value are credible.

Mine age is therefore a **reuse-context field**, not a universal exclusion rule: recency matters more for preservation of underground/industrial assets, while old pits remain eligible for reservoir screening. A mine record does not establish availability, safe occupancy, storage feasibility, current electrical capacity or project rights.

## Heat

Heat is a useful co-product, not a universal siting rule. Recovery is justified where useful-heat value exceeds the cost and complexity of recovery and distribution.

## Evidence and screening

Current screening is **unranked**:

- `screening_mode = unranked`;
- `ranking_allowed = false`.

The research base includes official hydrometric station references, structured evidence/provenance, community and infrastructure context, external reference projects, telecom/marine evidence and economic benchmarks. Missing geometry and missing values remain explicit.

## What is established

- PostGIS-oriented canonical data model for places, assets, projects, corridors, natural features, evidence, observations and scenarios.
- 24-river hydrology research set anchored to official WSC station references.
- Repeatable geometry/hydrology ingestion workflows with manual acceptance gates.
- Integrated application catalog and public-release model.
- Structural economic comparison method that can support or reject a generic distance configuration.

## What is not established

The repository does not yet establish:

- a preferred river or project site;
- authoritative connected river geometry for every research river;
- engineering intake/powerhouse alignments;
- project gross/net head;
- design flow or buildable MW;
- environmental acceptability or authorization;
- Indigenous/community authorization or benefit arrangements;
- exact fibre routes/capacity/SLA;
- heavy-project-cargo capability at a specific port;
- final local electrical design;
- vendor quotations;
- a committed international anchor tenant or offtake agreement;
- a mine approved or available for Kristal Farms reuse;
- an underground mine certified as safe/fit for compute occupancy;
- a mine-pit pumped-storage site with validated usable volume, head, water balance, geotechnics, environmental acceptability or grid value;
- bankable CAPEX/OPEX, NPV or IRR.

## Development mode

The next unit of work is the **corridor/site dossier**. Each dossier replaces broad research proxies with project-specific evidence across hydrology, terrain, engineering, environment, rights/governance, logistics, telecom, electrical architecture and economics.
