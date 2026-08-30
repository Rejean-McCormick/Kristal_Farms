#!/usr/bin/env python3
"""Pass 10 orchestrator. Intentionally stops before manual reach acceptance/terrain calculation."""
import argparse,pathlib,subprocess,sys
HERE=pathlib.Path(__file__).resolve().parent
def run(*args): subprocess.run([sys.executable,*map(str,args)],check=True)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--targets',required=True); ap.add_argument('--windows',required=True); ap.add_argument('--work-dir',required=True); ap.add_argument('--wsc-cache-dir'); a=ap.parse_args()
    w=pathlib.Path(a.work_dir); w.mkdir(parents=True,exist_ok=True)
    cmd=[HERE/'fetch_wsc_basins.py','--targets',a.targets,'--out',w/'wsc_target_basins.geojson']
    if a.wsc_cache_dir: cmd += ['--cache-dir',a.wsc_cache_dir]
    run(*cmd)
    run(HERE/'fetch_grhq_candidates.py','--windows',a.windows,'--out-dir',w/'grhq_candidates')
    run(HERE/'fetch_canada1water_candidates.py','--windows',a.windows,'--out-dir',w/'canada1water_candidates')
    print('STOP: manual connected-reach review is required before HRDEM discovery or terrain computation.')
if __name__=='__main__': main()
