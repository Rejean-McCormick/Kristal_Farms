# ADR-0001 — MapLibre as primary Web renderer

**Status:** accepted  
**Date:** 2026-08-30

## Context

Kristal Farms requires a visually strong public experience, professional interactive mapping, data-driven styling, vector tiles, terrain/globe capability, and freedom from a proprietary geospatial application backend.

## Decision

Use **MapLibre GL JS** as the primary Web map renderer, with **deck.gl** for specialized GPU visualizations.

## Alternatives considered

- Leaflet: simpler but less suitable for the desired modern WebGL experience and large tiled datasets.
- OpenLayers: excellent Web GIS capabilities but less aligned with the desired visual/product experience.
- ArcGIS: strong enterprise ecosystem but higher platform lock-in.
- CesiumJS: excellent 3D globe/engineering capabilities but unnecessary as the primary renderer for the MVP.

## Consequences

The Web team owns more custom product UX, which is desirable. Professional GIS capability is provided through PostGIS/QGIS/OGC interfaces rather than forcing the frontend to replicate desktop GIS.
