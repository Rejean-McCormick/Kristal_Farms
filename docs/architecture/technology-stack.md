# Technology stack

## Selected foundation

| Layer | Technology | Role |
|---|---|---|
| Web application | React + TypeScript + Next.js | Product UI and routing |
| Primary map | MapLibre GL JS | Cartographic renderer |
| Advanced visualization | deck.gl | GPU analytical/flow layers |
| Canonical database | PostgreSQL + PostGIS | Geospatial source of truth |
| Domain API | FastAPI | Kristal Farms-specific operations and models |
| Standards API | pygeoapi | OGC-oriented geospatial access |
| Tile serving | Martin | MVT delivery from PostGIS/tile archives |
| Public vector release | PMTiles | Immutable CDN-friendly vector archive |
| Raster release | COG | Cloud-friendly raster distribution |
| Professional desktop GIS | QGIS | Analysis/editing for authorized users |
| Analytical file interchange | GeoParquet | Large columnar geospatial datasets |
| Future engineering 3D | CesiumJS + 3D Tiles | Deferred engineering/terrain mode |

## Version policy

Application dependencies should be pinned by package/lock files and updated deliberately. Architecture documentation should generally describe capabilities and compatibility constraints rather than becoming a second dependency lock file.

## Re-evaluation triggers

A technology decision should be revisited when a measurable requirement changes: dataset size, rendering type, data governance, offline use, 3D engineering data, cloud constraints, or external partner integration.
