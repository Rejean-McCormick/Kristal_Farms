#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / 'data/fixtures/current'

def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text().splitlines() if x.strip()]

errors = []
entities = rows('core_entity.jsonl')
entity_ids = {x['id'] for x in entities}
if len(entity_ids) != len(entities):
    errors.append('duplicate entity UUID')
if any(('rank' in x.get('metadata', {}) or 'score' in x.get('metadata', {})) for x in entities):
    errors.append('implicit ranking metadata')

observations = rows('research_observation.jsonl')
forbidden = {'project_gross_head_m', 'project_net_head_m', 'design_flow_m3s', 'capacity_mw', 'validated_hosting_capacity_kw'}
if forbidden.intersection({x['metric'] for x in observations}):
    errors.append('forbidden automatic engineering/hosting metric')

states = rows('research_screening_dimension_state.jsonl')
if any(x.get('metadata', {}).get('ranking_allowed') is not False for x in states):
    errors.append('ranking_allowed not false')

stations = [x for x in rows('core_asset.jsonl') if x['asset_type'] == 'hydrometric_station']
if len(stations) != 24:
    errors.append(f'expected 24 hydrometric stations, found {len(stations)}')
if any(x.get('metadata', {}).get('geometry_role') != 'official_hydrometric_station_position' for x in stations):
    errors.append('station geometry role mismatch')

rivers = [x for x in rows('core_natural_feature.jsonl') if x['feature_type'] == 'river']
if len(rivers) != 24:
    errors.append(f'expected 24 river references, found {len(rivers)}')
if any(x['geometry'] is not None for x in rivers):
    errors.append('research river geometry unexpectedly materialized')

print(json.dumps({'ok': not errors, 'errors': errors, 'counts': {'entities': len(entities), 'stations': len(stations), 'rivers': len(rivers), 'observations': len(observations), 'screening_states': len(states)}}, indent=2))
raise SystemExit(1 if errors else 0)
