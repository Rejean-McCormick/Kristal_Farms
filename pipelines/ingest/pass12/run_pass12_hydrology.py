#!/usr/bin/env python3
"""Generate or execute Pass-12 HYDAT jobs for canonical stations."""
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]

def rows(p): return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--execute',action='store_true'); ap.add_argument('--out',default=str(ROOT/'data/raw/pass12')); a=ap.parse_args()
    assets=rows(ROOT/'data/fixtures/pass12/core_asset.jsonl'); script=Path(__file__).parent/'fetch_geomet_hydat.py'
    for asset in assets:
        st=asset.get('metadata',{}).get('station_number');
        if not st: continue
        for kind in ['daily','monthly','annual']:
            out=Path(a.out)/'geomet_hydat'/kind/st
            cmd=[sys.executable,str(script),'--kind',kind,'--station',st,'--out',str(out)] + (['--execute'] if a.execute else [])
            subprocess.run(cmd,check=True)
if __name__=='__main__': main()
