import csv,json,pathlib
from compare_architectures import reference_frontier
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'data/publish/pass14/economic_frontier_cases_recomputed.csv'
tx_low=1300000000/439; tx_high=1271000000/262
road_low=2100000000/809; road_high=2700000000/809
fibre_low=79419117/933; fibre_high=271937242/1300
rows=[]
for h in [25,50,100,200]:
  for r in [10,25,50,100]:
    for f in [100,250,500,933]:
      x=reference_frontier(h,r,f,tx_low=tx_low,tx_high=tx_high,road_low=road_low,road_high=road_high,fibre_low_proxy=fibre_low,fibre_high_proxy=fibre_high)
      rows.append({'case_key':f'hv{h}_road{r}_fibre{f}','hv_export_line_km':h,'export_road_km':r,'fibre_km':f,**{k:round(v,2) if isinstance(v,float) else v for k,v in x.items()}})
OUT.parent.mkdir(parents=True,exist_ok=True)
with OUT.open('w',newline='',encoding='utf-8') as fp:
  w=csv.DictWriter(fp,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(json.dumps({'cases':len(rows),'output':str(OUT)},indent=2))
