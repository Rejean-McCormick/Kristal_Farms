# ADR-0007 — Cesium deferred until engineering 3D data justifies it

**Status:** accepted  
**Date:** 2026-08-30

## Context

A 3D globe can create visual impact, but the MVP's core information is 2D/2.5D geospatial research and evidence. MapLibre already supports terrain/globe-style presentation.

## Decision

Do not use CesiumJS as the primary MVP renderer. Reconsider it for a dedicated engineering mode when LiDAR, photogrammetry, CAD/BIM, detailed terrain, or 3D infrastructure becomes material.

## Consequences

The MVP remains simpler while preserving a future path to 3D Tiles/Cesium. Stable entity IDs and backend separation should make a later second renderer feasible.
