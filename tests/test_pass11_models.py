import json,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'packages/schemas/python'))
from kristal_farms_models import Entity,Observation,ScreeningDimensionState

def rows(name): return [json.loads(x) for x in (ROOT/'data/fixtures/pass11'/name).read_text().splitlines() if x]

def test_entities_validate():
    for x in rows('core_entity.jsonl'): Entity.model_validate(x)

def test_observations_validate_and_no_engineering_values():
    obs=rows('research_observation.jsonl')
    for x in obs: Observation.model_validate(x)
    assert not {x['metric'] for x in obs}.intersection({'project_gross_head_m','design_flow_m3s','capacity_mw','validated_hosting_capacity_kw'})

def test_screening_unranked():
    for x in rows('research_screening_dimension_state.jsonl'):
        ScreeningDimensionState.model_validate(x)
        assert x['metadata']['ranking_allowed'] is False

def test_station_geometries_are_only_station_points():
    assets=rows('core_asset.jsonl')
    assert len(assets)==24
    for a in assets:
        assert a['asset_type']=='hydrometric_station'
        assert a['geometry']['type']=='Point'
        assert a['metadata']['geometry_role']=='official_hydrometric_station_position'

def test_natural_features_have_no_fake_geometry():
    rivers=rows('core_natural_feature.jsonl')
    assert len(rivers)==24
    assert all(r['geometry'] is None for r in rivers)


def test_pass10_operational_objects_migrated_to_system():
    jobs=rows('system_ingestion_job.jsonl')
    schemas=rows('system_dataset_schema.jsonl')
    assert len(jobs)==125
    assert len(schemas)==3
    kinds={x['job_type'] for x in jobs}
    assert 'extract_authoritative_hydrography_candidates' in kinds
    assert 'extract_hrdem_terrain_assets' in kinds
    assert 'external_geometry_ingestion_attempt' in kinds
    # Request windows belong to jobs, never natural river geometry.
    assert any(x['request_geometry'] is not None for x in jobs)
    rivers=rows('core_natural_feature.jsonl')
    assert all(x['geometry'] is None for x in rivers)
