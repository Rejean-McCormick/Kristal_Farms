import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
P=ROOT/'data/fixtures/pass13'
def jl(n):
    p=P/n
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def test_unranked_governance():
    g=jl('system_governance_state.jsonl')[0]
    assert g['screening_mode']=='unranked' and g['ranking_allowed'] is False
def test_community_geometry_semantics():
    places={x['entity_id']:x for x in jl('core_place.jsonl') if x['place_type']=='community'}
    for p in places.values():
        if p['geometry'] is not None:
            assert p['metadata']['geometry_role']=='legacy_approximate_community_centroid'
            assert p['metadata']['not_port_coordinate'] is True
def test_no_conceptual_corridor_geometry():
    for c in jl('core_corridor.jsonl'):
        if c['corridor_type']=='conceptual':
            assert c['geometry'] is None and c['metadata'].get('not_route') is True
def test_external_projects_are_not_candidates():
    for p in jl('core_project.jsonl'):
        if p['metadata'].get('external_reference') or p['role']=='external_reference':
            assert p['role']=='external_reference'
def test_legacy_env_not_active_no_go():
    for e in jl('research_evidence.jsonl'):
        if e['evidence_type']=='legacy_environment_context':
            assert e['status']=='unverified'
            assert e['metadata']['active_no_go_authority'] is False
def test_no_hosting_capacity_observation_created():
    metrics={o['metric'] for o in jl('research_observation.jsonl')}
    assert 'validated_hosting_capacity_kw' not in metrics
    assert 'design_flow_m3s' not in metrics
    assert 'project_gross_head_m' not in metrics
def test_broadband_not_completed():
    for p in jl('core_project.jsonl'):
        if p['entity_id']==str(__import__('uuid').uuid5(__import__('uuid').NAMESPACE_URL,'https://kristal.farms/project:external:nl:labrador-north-wireless-broadband')):
            assert p['project_status']=='provider_withdrawn_2025'
            assert p['metadata']['completed_backbone_confirmed'] is False
def test_screening_matrix_no_ranking():
    for s in jl('research_screening_dimension_state.jsonl'):
        assert s['metadata'].get('ranking_allowed') is False
def test_showcase_references_catalog_layers():
    catalog=json.loads((ROOT/'packages/catalog/catalog.pass13.json').read_text())
    ids={l['id'] for l in catalog['layers']}
    story=json.loads((ROOT/'packages/showcase/story.pass13.json').read_text())
    for sc in story['scenes']:
        assert set(sc['visible_layers']).issubset(ids)
def test_public_release_omits_legacy_tier():
    pub=json.loads((ROOT/'data/publish/pass13/communities_public.geojson').read_text())
    for f in pub['features']:
        assert 'legacy_tier' not in f['properties']
def test_fibre_planned_vs_operating_separate():
    corr={e['canonical_key']:e for e in jl('core_entity.jsonl') if e['entity_type']=='corridor'}
    assert corr['corridor:fibre:nunavik:eaufon-1']['status']=='operating'
    assert corr['corridor:fibre:nunavik:eaufon-2']['status']=='operating'
    assert corr['corridor:fibre:nunavik:eaufon-3']['status']=='planned_2027'
def test_station_points_still_official_monitoring_geometry():
    for a in jl('core_asset.jsonl'):
        if a['asset_type']=='hydrometric_station':
            assert a['metadata']['geometry_role']=='official_hydrometric_station_position'
