# API overview

Kristal Farms uses different interfaces for different jobs.

| Interface | Purpose |
|---|---|
| FastAPI domain API | Kristal Farms-specific workflows and scenarios |
| OGC API | Standards-based geospatial feature access |
| Martin MVT | High-performance map rendering |
| PMTiles/COG | Immutable public release delivery |
| PostGIS | Controlled professional/QGIS and service access |

## Rule

Do not force all geospatial access through proprietary endpoints when a standard collection interface is appropriate. Conversely, do not distort domain workflows to fit a generic OGC feature API.

## Contracts

A starter OpenAPI contract is provided at `contracts/api/kristal-farms-api.openapi.yaml`.
