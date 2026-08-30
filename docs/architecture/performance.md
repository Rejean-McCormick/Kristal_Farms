# Performance

## Principles

- Avoid sending large raw GeoJSON collections to browsers.
- Use MVT/PMTiles for large vector layers.
- Use COG for raster.
- Generalize geometry by zoom.
- Load specialized analysis layers only when enabled.
- Cache immutable release artifacts aggressively.
- Keep selection/detail requests separate from map rendering payloads.

## Suggested budgets

These are engineering targets, not hard guarantees:

- initial public shell should become interactive quickly on normal broadband;
- map interaction should remain visually smooth during pan/zoom;
- layer toggles should not require full application reload;
- detail/evidence panels should use indexed queries and paginated evidence where needed;
- public releases should be CDN-cacheable and independent of live DB latency for core visuals.

## Database

Use spatial indexes for geometry filters and conventional indexes for commonly filtered metadata. Validate query plans for large publish views before exposing them as live endpoints.
