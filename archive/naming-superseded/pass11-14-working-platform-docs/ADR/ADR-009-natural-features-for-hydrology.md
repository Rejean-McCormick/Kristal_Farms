# ADR-009 — Natural features for hydrology

**Status:** Accepted for Pass 11 foundation

## Context

The Hydro Resource Atlas contains rivers, watersheds and river reaches. They are not infrastructure `asset`, development `project`, or necessarily `corridor`. Forcing them into those types would blur factual geography and scenarios.

## Decision

Add `core.natural_feature` with types `river`, `watershed`, `river_reach`, `lake`, `coastline`, `other`. Geometry may be `NULL`.

A WSC hydrometric station is a `core.asset`; the river it monitors is a `core.natural_feature`; `core.entity_relation(relation_type='monitors')` links them.

## Consequence

Pass 9–10 can migrate without turning station points into river geometry or projects. Future accepted WSC/GRHQ/Canada1Water geometry can attach to the natural feature without changing its canonical ID.
