#!/usr/bin/env python3
"""Recompute the generic enabling-infrastructure economic frontier."""
import csv, json, pathlib
from compare_architectures import reference_frontier

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'data/publish/current/economic_frontier_cases_recomputed.csv'

# Reference ratios are intentionally research benchmarks, not site-cost estimates.
tx_low = 1300000000 / 439
tx_high = 1271000000 / 262
road_low = 2100000000 / 809
road_high = 2700000000 / 809
fibre_low = 79419117 / 933
fibre_high = 271937242 / 1300

rows = []
for hv_km in [25, 50, 100, 200]:
    for road_km in [10, 25, 50, 100]:
        for fibre_km in [100, 250, 500, 933]:
            result = reference_frontier(
                hv_km, road_km, fibre_km,
                tx_low=tx_low, tx_high=tx_high,
                road_low=road_low, road_high=road_high,
                fibre_low_proxy=fibre_low, fibre_high_proxy=fibre_high,
            )
            rows.append({
                'case_key': f'hv{hv_km}_road{road_km}_fibre{fibre_km}',
                'hv_export_line_km': hv_km,
                'export_road_km': road_km,
                'fibre_km': fibre_km,
                **{k: round(v, 2) if isinstance(v, float) else v for k, v in result.items()},
            })

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open('w', newline='', encoding='utf-8') as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
print(json.dumps({'cases': len(rows), 'output': str(OUT)}, indent=2))
