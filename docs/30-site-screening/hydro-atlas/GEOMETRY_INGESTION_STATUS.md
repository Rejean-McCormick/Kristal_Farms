# Geometry Ingestion Status — Pass 9

Pass 9 verified the official WSC, GRHQ, Canada1Water/NHN and HRDEM source families. It did **not** successfully ingest WSC basin ZIPs, GRHQ UDH binaries or Canada1Water regional GeoPackages in the current execution environment.

Accordingly:

- WSC station points are real/sourced geometry;
- basin polygons are `null`;
- river flowlines are `null`;
- terrain profiles and hydraulic head are `null`;
- no straight-line substitute is permitted.

Machine log: `data/processed/pass9/GEOMETRY_INGESTION_LOG_PASS9.json`.
