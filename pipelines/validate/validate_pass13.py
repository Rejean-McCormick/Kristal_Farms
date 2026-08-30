import json, pathlib, collections, re, sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
P=ROOT/'data/fixtures/pass13'
def jl(n): return [json.loads(x) for x in (P/n).read_text().splitlines() if x.strip()]
errors=[]
entities=jl('core_entity.jsonl'); ids=[e['id'] for e in entities]
if len(ids)!=len(set(ids)): errors.append('duplicate entity ids')
entityset=set(ids)
for r in jl('core_entity_relation.jsonl'):
    if r['from_entity_id'] not in entityset or r['to_entity_id'] not in entityset: errors.append('orphan entity relation')
for r in jl('research_evidence_relation.jsonl'):
    if r['entity_id'] not in entityset: errors.append('orphan evidence relation')
for e in entities:
    if e['metadata'].get('ranking_allowed') is True: errors.append('entity ranking allowed unexpectedly')
for p in jl('core_project.jsonl'):
    if p['role']=='external_reference' and p['metadata'].get('kristal_candidate') is True: errors.append('external reference candidate collision')
for c in jl('core_corridor.jsonl'):
    if c['corridor_type']=='conceptual' and c['geometry'] is not None: errors.append('conceptual corridor has geometry')
for e in jl('research_evidence.jsonl'):
    if e['evidence_type']=='legacy_environment_context' and e['status']!='unverified': errors.append('legacy environment promoted')
cat=json.loads((ROOT/'packages/catalog/catalog.pass13.json').read_text())
if cat['ranking_allowed'] is not False: errors.append('catalog ranking allowed')
story=json.loads((ROOT/'packages/showcase/story.pass13.json').read_text())
layerids={x['id'] for x in cat['layers']}
for s in story['scenes']:
    if not set(s['visible_layers']).issubset(layerids): errors.append('story missing catalog layer')
print(json.dumps({'pass':not errors,'errors':errors,'entities':len(entities),'relations':len(jl('core_entity_relation.jsonl')),'evidence':len(jl('research_evidence.jsonl')),'observations':len(jl('research_observation.jsonl'))},indent=2))
sys.exit(0 if not errors else 1)
