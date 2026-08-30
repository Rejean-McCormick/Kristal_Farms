# Data release runbook

## Generate candidate

1. Freeze/select source database snapshot or release transaction boundary.
2. Record migration/data/policy versions.
3. Build publish views.
4. Run full QA.
5. Generate PMTiles/COG/metadata/export artifacts.
6. Compute checksums.
7. Run public/private leakage checks.
8. Generate release manifest.

## Review

- validate representative map views;
- validate feature counts against expected changes;
- inspect evidence links;
- inspect conceptual vs verified styling;
- confirm screening policy;
- verify public artifact contains no restricted attributes/geometries.

## Publish

Upload immutable versioned artifacts, then update the public release pointer/config only after validation.

## Rollback

Point the public application back to the prior immutable release.
