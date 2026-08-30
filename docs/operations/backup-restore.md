# Backup and restore

## PostgreSQL

Production must have automated backups appropriate to the chosen hosting platform, with restore procedures tested periodically.

## What to protect

- canonical PostGIS data;
- source registry;
- evidence relations;
- scenario records requiring retention;
- system/catalog configuration stored in DB;
- migration history.

## Public artifacts

PMTiles/COG releases are immutable and may be reproducible, but retained published versions should still be protected through object-storage versioning/replication or equivalent policy.

## Restore test

A backup is not considered operationally valid until a restore has been tested in a non-production environment.
