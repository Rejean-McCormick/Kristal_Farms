# Tile API

## Live tiles

Martin serves MVT from curated PostGIS publish views.

## Static public tiles

Stable public layers should normally be bundled into PMTiles for CDN delivery.

## Tile properties

Tile payloads should include only fields required for rendering, filtering, selection, and lightweight tooltips. Do not embed full source documents or large evidence payloads in vector tiles.

## Feature identity

Every selectable feature in a tile must carry a stable entity identifier that can be used to fetch full detail/evidence from an API.

## Generalization

Use zoom-dependent geometry simplification and attribute reduction where appropriate. Preserve canonical geometry in PostGIS.
