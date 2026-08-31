# ADR 0023 — Satellite imagery is a static local snapshot

- Status: Accepted
- Date: 2026-08-31

## Context

The Observatory benefits from photographic context at high zoom, but a
third-party satellite tile API introduces changing imagery, runtime network
dependencies, provider keys, cost exposure and reproducibility problems.

## Decision

Satellite imagery used by the product is manually acquired and published as an
immutable local snapshot.

Runtime flow:

```text
reviewed source GeoTIFF
        ↓ manual promotion
pipelines/imagery/build_local_satellite.py
        ↓
data/publish/imagery/current/imagery_manifest.json
        ↓ deployment copy
apps/web/public/imagery/<snapshot>/{z}/{x}/{y}.png
        ↓
MapLibre raster layer
```

The product must not contain a MapTiler/Esri/Sentinel-Hub satellite API key and
must not automatically refresh satellite imagery.

Photographic context is not evidence. Evidence and geometry provenance remain
separate.

## Consequences

- A release is visually reproducible.
- Imagery updates require an explicit reviewed promotion.
- Repository/deployment size can be large.
- Source licensing and attribution must be reviewed before publishing tiles.
- The contextual vector basemap remains a separate concern and may still be
  externally hosted unless separately snapshotted.
