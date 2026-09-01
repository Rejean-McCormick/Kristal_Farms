import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / 'data/fixtures/current'


def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text(encoding="utf-8").splitlines() if x.strip()]


def test_unranked_governance():
    g = rows('system_governance_state.jsonl')[0]
    assert g['screening_mode'] == 'unranked' and g['ranking_allowed'] is False


def test_community_geometry_semantics():
    places = [x for x in rows('core_place.jsonl') if x['place_type'] == 'community']
    for place in places:
        if place['geometry'] is not None:
            assert place['metadata']['geometry_role'] == 'legacy_approximate_community_centroid'
            assert place['metadata']['not_port_coordinate'] is True


def test_no_conceptual_corridor_geometry():
    for corridor in rows('core_corridor.jsonl'):
        if corridor['corridor_type'] == 'conceptual':
            assert corridor['geometry'] is None
            assert corridor['metadata'].get('not_route') is True


def test_external_projects_are_not_candidates():
    for project in rows('core_project.jsonl'):
        if project['role'] == 'external_reference':
            assert project['metadata'].get('kristal_farms_candidate') is not True


def test_legacy_environment_is_not_active_no_go():
    for evidence in rows('research_evidence.jsonl'):
        if evidence['evidence_type'] == 'legacy_environment_context':
            assert evidence['status'] == 'unverified'
            assert evidence['metadata']['active_no_go_authority'] is False


def test_catalog_story_alignment():
    catalog = json.loads((ROOT / 'packages/catalog/catalog.json').read_text(encoding="utf-8"))
    story = json.loads((ROOT / 'packages/showcase/story.json').read_text(encoding="utf-8"))
    ids = {layer['id'] for layer in catalog['layers']}
    for scene in story['scenes']:
        assert set(scene['visible_layers']).issubset(ids)


def test_public_release_omits_legacy_tier():
    public = json.loads((ROOT / 'data/publish/current/communities_public.geojson').read_text(encoding="utf-8"))
    for feature in public['features']:
        assert 'legacy_tier' not in feature['properties']


def test_fibre_planned_vs_operating_separate():
    entities = {e['canonical_key']: e for e in rows('core_entity.jsonl') if e['entity_type'] == 'corridor'}
    assert entities['corridor:fibre:nunavik:eaufon-1']['status'] == 'operating'
    assert entities['corridor:fibre:nunavik:eaufon-2']['status'] == 'operating'
    assert entities['corridor:fibre:nunavik:eaufon-3']['status'] == 'planned_2027'
