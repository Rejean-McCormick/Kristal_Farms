# Publish pipelines

Implementation home for immutable public releases, PMTiles/COG/GeoJSON generation and release manifests.

## Target villages

`build_target_villages_public.py` promotes `research/communities/targets/*.yaml` into the governed `data/publish/current/target_villages_public.json` artifact and writes `data/processed/current/target_villages_audit.csv`. The web application consumes only the published artifact.
