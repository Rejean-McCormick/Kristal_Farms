# Data platform architecture

## PostgreSQL schemas

```text
raw        Source-faithful imports
staging    Normalization / ETL workspace
core       Canonical geographic and infrastructure entities
research   Evidence, sources, observations, research state
scenario   User/model hypotheses and results
publish    Stable views for APIs, tiles, and exports
system     Catalog, policies, versions, operational metadata
```

## Why PostGIS

PostGIS provides a durable professional geospatial source of truth that can serve the Web application, Python workflows, QGIS, standards-based APIs, and tile generation without converting every workflow into frontend-specific JSON.

## Derived formats

| Need | Representation |
|---|---|
| Small interchange | GeoJSON |
| Large analytical files | GeoParquet |
| Web vector rendering | MVT |
| Immutable public tiles | PMTiles |
| Raster | Cloud Optimized GeoTIFF |
| Portable GIS exchange | GeoPackage |
| Future large 3D | 3D Tiles |

Derived artifacts must record their source dataset version and publication timestamp.
