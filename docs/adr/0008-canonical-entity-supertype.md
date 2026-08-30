# ADR-008 — Canonical entity supertype

**Status:** Accepted

## Context

The architecture already has a conceptual `ENTITY`, while evidence and observations need to reference places, assets, projects, corridors and future natural features with referential integrity. A polymorphic `(entity_type, entity_id)` pair cannot be protected by a normal foreign key.

## Decision

Introduce `core.entity` as the canonical identity table. `core.place`, `core.asset`, `core.project`, `core.corridor` and `core.natural_feature` are subtype tables keyed by the same UUID. Evidence/observations/relations reference `core.entity(id)`.

## Consequence

Canonical IDs remain stable across Web, QGIS, APIs, tiles and future 3D. Evidence does not need to know which subtype table holds geometry.
