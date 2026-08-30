# Data publishing

## Public release strategy

The canonical database is live and mutable; public release artifacts are immutable and versioned.

```text
PostGIS -> publish views -> QA -> PMTiles/COG/metadata -> object storage/CDN
```

## Publish views

The `publish` schema should contain explicit public/professional views. Avoid having the release script infer security from arbitrary application state.

## Artifacts

Typical release may include:

```text
manifest.json
catalog.json
*.pmtiles
*.tif / COG
metadata/*.json
checksums.txt
```

## Release manifest

Must record:

- release version;
- generated timestamp;
- source DB migration/version;
- included collections;
- artifact hashes;
- classification/publication policy version;
- QA result.

## Rollback

Because artifacts are immutable, rollback should mean repointing the public release alias/config to a previous validated version, not rewriting files in place.
