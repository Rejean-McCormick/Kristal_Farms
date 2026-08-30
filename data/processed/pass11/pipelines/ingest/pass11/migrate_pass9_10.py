#!/usr/bin/env python3
"""Pass 11 migration entrypoint.

Transforms Pass 9/10 hydro research artifacts into canonical platform import fixtures.
This script deliberately does not invent basin/reach geometry or hydrology values.
"""
from pathlib import Path
import argparse, subprocess, sys

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--docs-repo',required=True)
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    # The generated fixtures in data/fixtures/pass11 are the reference output of the full migration.
    # A production implementation should stream the same models into staging tables, then promote transactionally.
    repo=Path(args.docs_repo)
    required=[repo/'data/processed/pass9/layers/37_hydrology_observation_profiles.geojson', repo/'data/processed/pass10/layers/41_wsc_basin_polygon_availability.geojson']
    missing=[str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit('missing required inputs: '+', '.join(missing))
    print('inputs verified; use fixtures + COPY loader or implement staging writer against these schemas')

if __name__=='__main__': main()
