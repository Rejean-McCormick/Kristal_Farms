import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'packages/schemas/python'))
from kristal_farms_models import Entity, Observation, ScreeningDimensionState

FIX = ROOT / 'data/fixtures/current'

def rows(name):
    return [json.loads(x) for x in (FIX / name).read_text().splitlines() if x.strip()]


def test_entities_validate():
    for item in rows('core_entity.jsonl'):
        Entity.model_validate(item)


def test_observations_validate_and_no_automatic_engineering_values():
    obs = rows('research_observation.jsonl')
    for item in obs:
        Observation.model_validate({k: v for k, v in item.items() if k in Observation.model_fields})
    forbidden = {'project_gross_head_m', 'project_net_head_m', 'design_flow_m3s', 'capacity_mw', 'validated_hosting_capacity_kw'}
    assert not forbidden.intersection({x['metric'] for x in obs})


def test_screening_unranked():
    for item in rows('research_screening_dimension_state.jsonl'):
        ScreeningDimensionState.model_validate(item)
        assert item['metadata']['ranking_allowed'] is False


def test_station_geometries_are_only_station_points():
    stations = [a for a in rows('core_asset.jsonl') if a['asset_type'] == 'hydrometric_station']
    assert len(stations) == 24
    for station in stations:
        assert station['geometry']['type'] == 'Point'
        assert station['metadata']['geometry_role'] == 'official_hydrometric_station_position'


def test_research_rivers_have_no_fabricated_geometry():
    rivers = [x for x in rows('core_natural_feature.jsonl') if x['feature_type'] == 'river']
    assert len(rivers) == 24
    assert all(r['geometry'] is None for r in rivers)


def test_geometry_jobs_remain_system_objects():
    jobs = rows('system_ingestion_job.jsonl')
    kinds = {x['job_type'] for x in jobs}
    assert 'extract_authoritative_hydrography_candidates' in kinds
    assert 'extract_hrdem_terrain_assets' in kinds
    assert 'external_geometry_ingestion_attempt' in kinds
    assert any(x['request_geometry'] is not None for x in jobs)
