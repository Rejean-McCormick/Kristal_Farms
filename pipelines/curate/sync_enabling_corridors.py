#!/usr/bin/env python3
"""Sync non-electrical enabling-corridor research into governed fixtures."""
from __future__ import annotations
import argparse, csv, json, uuid
from pathlib import Path
import yaml

BASE="https://kristal.farms/"
def uid(key): return str(uuid.uuid5(uuid.NAMESPACE_URL, BASE+key))
def rows(path): return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
def write(path, data): path.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in data),encoding="utf-8")
def upsert(old,new,key):
    repl={key(r):r for r in new}; seen=set(); out=[]
    for r in old:
        k=key(r)
        if k in repl: out.append(repl[k]); seen.add(k)
        else: out.append(r)
    for r in new:
        k=key(r)
        if k not in seen and all(key(x)!=k for x in old): out.append(r)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo-root",type=Path,default=Path(__file__).resolve().parents[2]); a=ap.parse_args(); root=a.repo_root.resolve()
    reg=yaml.safe_load((root/"research/infrastructure/enabling_corridors.yaml").read_text(encoding="utf-8"))
    if reg.get("schema")!="kristal-enabling-corridors-research/v1" or reg.get("ranking_allowed") is not False: raise SystemExit("invalid enabling corridor registry")
    fix=root/"data/fixtures/current"; entities=rows(fix/"core_entity.jsonl"); corridors=rows(fix/"core_corridor.jsonl"); relations=rows(fix/"core_entity_relation.jsonl"); evidence=rows(fix/"research_evidence.jsonl"); evsrc=rows(fix/"research_evidence_source.jsonl"); evrel=rows(fix/"research_evidence_relation.jsonl"); sources=rows(fix/"research_source.jsonl")
    entity_by_key={r["canonical_key"]:r for r in entities}; source_by_key={r["source_key"]:r for r in sources}
    ne=[]; nc=[]; nr=[]; nev=[]; nes=[]; ner=[]; ncan=[]
    for item in reg["corridors"]:
        key=item["canonical_key"]; eid=uid(key)
        ne.append({"id":eid,"canonical_key":key,"entity_type":"corridor","name":item["name"],"status":item["corridor_status"],"visibility":"PUBLIC","metadata":{"role":"enabling_context","not_kristal_route":True,"electrical_commitment":False}})
        nc.append({"entity_id":eid,"corridor_type":item["corridor_type"],"corridor_status":item["corridor_status"],"geometry":None,"operator":item.get("operator"),"metadata":item.get("metadata",{})})
        for c in item.get("communities",[]):
            target=entity_by_key.get(c["entity_key"])
            if not target: raise SystemExit(f"missing community {c['entity_key']}")
            nr.append({"id":uid(f"entity-relation:{key}:serves_context:{c['entity_key']}"),"from_entity_id":eid,"to_entity_id":target["id"],"relation_type":"serves_context","valid_from":None,"valid_to":None,"metadata":{"conceptual":True,"not_route_relation":True,"electrical_commitment":False}})
        ev=item["evidence"]; evid=uid(f"evidence:enabling-corridor:{key}")
        nev.append({"id":evid,"evidence_key":f"evidence:enabling-corridor:{key}","evidence_type":ev["evidence_type"],"claim":ev["claim"],"status":"verified","confidence":ev["confidence"],"valid_from":None,"valid_to":None,"observed_at":None,"published_at":ev.get("published_at"),"retrieved_at":"2026-09-01","metadata":{"conceptual":True,"electrical_commitment":False}})
        ner.append({"evidence_id":evid,"entity_id":eid,"relation_type":"describes"})
        for sk in item["source_keys"]:
            if sk not in source_by_key: raise SystemExit(f"missing source {sk}")
            nes.append({"evidence_id":evid,"source_id":source_by_key[sk]["id"],"source_role":"supports"})
        ncan.append({"legacy_id":"","canonical_entity_id":eid,"canonical_key":key,"entity_type":"corridor","mapping_role":"integrated_atlas_context","source_context":"enabling_corridors_registry"})
    write(fix/"core_entity.jsonl",upsert(entities,ne,lambda r:r["id"])); write(fix/"core_corridor.jsonl",upsert(corridors,nc,lambda r:r["entity_id"])); write(fix/"core_entity_relation.jsonl",upsert(relations,nr,lambda r:r["id"])); write(fix/"research_evidence.jsonl",upsert(evidence,nev,lambda r:r["id"])); write(fix/"research_evidence_source.jsonl",upsert(evsrc,nes,lambda r:(r["evidence_id"],r["source_id"],r["source_role"]))); write(fix/"research_evidence_relation.jsonl",upsert(evrel,ner,lambda r:(r["evidence_id"],r["entity_id"],r["relation_type"])))
    cp=fix/"canonical_id_registry.csv"; old=list(csv.DictReader(cp.open(encoding="utf-8",newline=""))); merged=upsert(old,ncan,lambda r:r["canonical_entity_id"])
    with cp.open("w",encoding="utf-8",newline="") as h: w=csv.DictWriter(h,fieldnames=["legacy_id","canonical_entity_id","canonical_key","entity_type","mapping_role","source_context"]); w.writeheader(); w.writerows(merged)
    print(json.dumps({"status":"ok","corridors_synced":len(nc),"relations_synced":len(nr)},indent=2))
if __name__=="__main__": main()
