# Architecture Decision Records

ADRs preserve the reasoning behind durable decisions.

## Statuses

```text
proposed
accepted
superseded
deprecated
rejected
```

## Process

1. Copy `0000-template.md`.
2. Assign next number.
3. Describe context and alternatives.
4. Record consequences, including operational/data consequences.
5. Link superseded ADRs rather than rewriting their history.

## Initial ADRs

- [0001 — MapLibre as primary Web renderer](0001-maplibre-primary-renderer.md)
- [0002 — PostGIS as source of truth](0002-postgis-source-of-truth.md)
- [0003 — Evidence separated from geometry](0003-evidence-separated-from-geometry.md)
- [0004 — Open geospatial interoperability](0004-open-geospatial-interoperability.md)
- [0005 — Immutable public data releases](0005-immutable-public-data-releases.md)
- [0006 — Ranking disabled by policy](0006-ranking-disabled-by-policy.md)
- [0007 — Cesium deferred](0007-cesium-deferred.md)

- [0020 — One monorepo with three logical systems](0020-one-monorepo-three-logical-systems.md)
- [0021 — Tenant environments are content-blind by design](0021-content-blind-tenant-environments.md)
- [0022 — Responsible-tenancy controls are counterparty-based](0022-counterparty-screening-before-tenancy.md)
