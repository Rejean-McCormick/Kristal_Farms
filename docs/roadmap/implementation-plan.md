# Implementation plan

## Current web implementation checkpoint

The repository contains the first Observatory Explorer vertical slice under `apps/web/`. It implements the shared map interaction foundation over the current public release: communities and hydrometric stations, proximity/hover/selection, search, catalog visibility controls, persistent Entity Inspector, evidence summary, non-geographic relation constellation, comparison pins and shareable URL state.

This checkpoint does **not** mark Phase 1 or Phase 2 complete. Terrain/globe narrative work, the complete layer catalog, filters, timeline, exports, production tiles/API integration and full comparison workflows remain roadmap items.

## Phase 0 — Foundation

Deliver:

- monorepo/repository structure;
- local containers;
- PostGIS migrations;
- canonical IDs;
- evidence/source model;
- layer catalog schema;
- controlled research-data importer;
- QA framework;
- initial public release pipeline.

## Phase 1 — Showcase MVP

Deliver:

- visual identity and base map;
- Observatory interaction foundation (semantic symbols, hover/focus, persistent selection);
- globe/terrain entry scene;
- northern communities;
- external renewable reference projects;
- Kristal Farms system architecture animation;
- simplified evidence inspector;
- static release via PMTiles/CDN;
- responsive/reduced-motion behavior.

## Phase 2 — Explorer

Deliver:

- full layer catalog UI;
- search;
- filters;
- timeline;
- evidence matrix;
- full Entity Inspector, relation constellation and compare interaction;
- shareable URLs;
- metadata/export;
- live API/OGC access where justified;
- QGIS workflow documentation.

## Phase 3 — Scenario Studio

Deliver:

- scenario data model;
- assumption editor;
- deterministic first energy model;
- result visualization;
- comparison;
- reproducibility metadata.

## Phase 4 — Geospatial screening

Integrate:

- DEM/hydrology;
- telecom/fibre;
- marine/road logistics;
- environmental constraints;
- governance/rights datasets;
- candidate site research;
- spatial queries.

Ranking remains disabled unless governance explicitly changes.

## Phase 5 — Engineering 3D

Only when real engineering data justifies it:

- CesiumJS;
- 3D Tiles;
- LiDAR/photogrammetry;
- CAD/BIM;
- detailed dam/penstock/transmission visualization.
