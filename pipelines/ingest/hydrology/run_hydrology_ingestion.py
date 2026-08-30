#!/usr/bin/env python3
"""Generate or execute HYDAT ingestion jobs for canonical hydrometric stations."""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def rows(path: Path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--out', default=str(ROOT / 'data/raw/hydrology'))
    args = parser.parse_args()

    assets = rows(ROOT / 'data/fixtures/current/core_asset.jsonl')
    fetcher = Path(__file__).parent / 'fetch_geomet_hydat.py'
    for asset in assets:
        station = asset.get('metadata', {}).get('station_number')
        if not station:
            continue
        for kind in ['daily', 'monthly', 'annual']:
            out = Path(args.out) / 'geomet_hydat' / kind / station
            command = [sys.executable, str(fetcher), '--kind', kind, '--station', station, '--out', str(out)]
            if args.execute:
                command.append('--execute')
            subprocess.run(command, check=True)


if __name__ == '__main__':
    main()
