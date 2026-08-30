# Layer catalog

## Purpose

The layer catalog makes the application data-driven. Generic layers are described declaratively and instantiated by shared rendering code.

Machine schema:

`contracts/layers/layer-catalog.schema.json`

Example:

`contracts/layers/layer-catalog.example.yaml`

## Catalog responsibilities

A layer definition may control:

- ID/title/group;
- source type and collection;
- geometry types;
- renderer;
- style token or expressions;
- min/max zoom;
- legend;
- filters;
- temporal behavior;
- inspector fields;
- evidence support;
- export capability;
- classification/permissions;
- feature-state behavior.

## Source types

Initial source types:

```text
vector_tiles
pmtiles
ogc_features
geojson_small
cog
api_derived
scenario
```

## Special layers

A custom component is appropriate when a layer requires behavior not expressible through the generic catalog, such as an interactive scenario network or engineering 3D model.

## Validation

Catalog configuration must be schema-validated in CI and at application build/startup. Unknown source types, missing IDs, invalid permissions, or malformed field mappings should fail fast.
