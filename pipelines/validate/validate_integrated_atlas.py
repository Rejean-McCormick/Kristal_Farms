#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / 'data/fixtures/current'

def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text().splitlines() if x.strip()]

errors = []
entities = rows('core_entity.jsonl')
entity_ids = {e['id'] for e in entities}
for relation in rows('core_entity_relation.jsonl'):
    if relation['from_entity_id'] not in entity_ids or relation['to_entity_id'] not in entity_ids:
        errors.append('orphan entity relation')
for relation in rows('research_evidence_relation.jsonl'):
    if relation['entity_id'] not in entity_ids:
        errors.append('orphan evidence relation')
for corridor in rows('core_corridor.jsonl'):
    if corridor['corridor_type'] == 'conceptual' and corridor['geometry'] is not None:
        errors.append('conceptual corridor has geometry')
for project in rows('core_project.jsonl'):
    if project['role'] == 'external_reference' and project.get('metadata', {}).get('kristal_farms_candidate') is True:
        errors.append('external reference promoted to candidate')
for evidence in rows('research_evidence.jsonl'):
    if evidence['evidence_type'] == 'legacy_environment_context' and evidence['status'] != 'unverified':
        errors.append('legacy environment evidence promoted')

catalog = json.loads((ROOT / 'packages/catalog/catalog.json').read_text())
if catalog['ranking_allowed'] is not False:
    errors.append('catalog ranking enabled')
story = json.loads((ROOT / 'packages/showcase/story.json').read_text())
layer_ids = {x['id'] for x in catalog['layers']}
for scene in story['scenes']:
    if not set(scene['visible_layers']).issubset(layer_ids):
        errors.append('showcase references missing catalog layer')

print(json.dumps({'ok': not errors, 'errors': errors, 'entities': len(entities), 'relations': len(rows('core_entity_relation.jsonl')), 'catalog_layers': len(catalog['layers']), 'showcase_scenes': len(story['scenes'])}, indent=2))
raise SystemExit(1 if errors else 0)
