# Imagery source archive

Place manually downloaded, georeferenced source imagery here after source and
license review.

Recommended characteristics:

- GeoTIFF / COG with valid CRS and georeferencing
- true-color satellite or orthophoto mosaic
- documented acquisition/mosaic date
- reviewed redistribution/storage license
- source checksum retained in the published imagery manifest

Nothing in `apps/web` downloads satellite imagery automatically.

Large rasters generally exceed normal GitHub file limits. If originals must be
versioned in GitHub, use Git LFS and verify that the imagery license permits
repository distribution.
