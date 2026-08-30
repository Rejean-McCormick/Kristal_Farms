# Geometry ingestion status

The Hydro Resource Atlas has verified the official WSC, GRHQ, Canada1Water/NHN and HRDEM source families. In the current canonical fixture, authoritative natural-feature geometry has **not** yet been materialized for the full 24-river set.

Accordingly:

- WSC station points are sourced geometry;
- basin polygons remain `null` in the current fixture;
- river flowlines remain `null` until authoritative connected reaches are ingested and accepted;
- terrain profiles remain unavailable until accepted flowline geometry exists;
- hydraulic project head remains unavailable until an engineering layout exists;
- no straight-line or hand-drawn substitute is permitted.

Historical execution logs are retained under `archive/research-snapshots/`.
