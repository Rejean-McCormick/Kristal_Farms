# Data Catalog

## Raw-data rule

Files under `data/raw/` are preserved as supplied. Do not overwrite them with cleaned/derived values. Create a new version or a processed dataset when transformations are required.

### `kristal_farms_village_inventory.csv`

**Rows:** 21  
**Columns:** 8

`category`, `tier`, `village_community`, `region`, `river_hydro_anchor`, `kristal_farms_status`, `decision_use`, `notes`
### `labrador_hydroelectric_potential.csv`

**Rows:** 58  
**Columns:** 32

`schema_version`, `record_id`, `feature_id`, `display_name`, `alternate_names`, `feature_type`, `river_system`, `site_name`, `observation_type`, `mw_value`, `mw_min`, `mw_max`, `mw_unit`, `mw_kind`, `current_status`, `development_level`, `status_confidence`, `is_mappable`, `map_layer`, `latitude`, `longitude`, `location_hint`, `google_my_maps_description`, `source_name`, `source_year`, `source_url`, `source_detail`, `source_quality`, `data_confidence`, `notes`, `needs_review`, `status_checked_date`
### `labrador_hydro_google_mymaps_points_v1.csv`

**Rows:** 88  
**Columns:** 24

`Entry_ID`, `Point_Role`, `Point_Mappable`, `Feature_ID`, `Map_Name`, `Latitude`, `Longitude`, `Label`, `Description`, `River_or_watercourse`, `Hydro_site_or_reference`, `Capacity_or_potential`, `Current_status`, `Dam_or_site_lat`, `Dam_or_site_lon`, `Dam_point_used`, `Dam_point_confidence`, `Mouth_or_coast_lat`, `Mouth_or_coast_lon`, `Mouth_or_coast_point_used`, `Mouth_point_type`, `Mouth_confidence`, `Mapping_note`, `Source_URLs_or_notes`


### `Kristal_Farms_Partner_Cost_Advantage.xlsx`

Working cost workbook retained from the prior repository.

Sheets:
- `Dashboard`
- `Cost_Model`
- `Chart_Data`
- `Partner_Message`
- `Sources`

The cost model is explicitly an **illustrative index model**: conventional remote compute totals **100**, Kristal Farms totals **40**, and the modeled savings gap is **60**. The workbook itself cautions that it is a presentation tool and that final values require engineering, utility tariffs, site selection, heat demand, fibre design, and partner commitments.

Treat these outputs as scenario/model results, not a validated project financial case. Assumptions require explicit version and source control before external use.

## Current inventory summary

### Village inventory
- Total records: **21**
- Tier 1: **1**
- Tier 2: **1**
- Tier 3: **11**
- Tier 4: **7**
- Boundary cases: **1**

### Labrador hydro dataset
- Total records: **58**
- Mappable: **57**
- Marked `needs_review`: **22**

### Map-points dataset
- Total point records: **88**
- `Dam_or_site`: **44**
- `Mouth_or_coast`: **44**

## Data governance to add next

- schema validation;
- unique-key checks;
- coordinate validation;
- source URL/status checks;
- dated data releases;
- processed/release map layers;
- link from every externally used numeric claim back to a dataset/source record.


## Pass 9 — Hydro Resource Atlas

Path: `data/processed/pass9/`

- `layers/34_authoritative_watershed_polygons.geojson` — WSC basin registry; polygons null until official package ingestion.
- `layers/35_authoritative_river_reaches.geojson` — connected-flowline registry; lines null until authoritative hydrography ingestion.
- `layers/36_dem_terrain_profiles.geojson` — HRDEM status; terrain/head fields null.
- `layers/37_hydrology_observation_profiles.geojson` — sourced WSC station points and drainage metadata.
- `layers/38_hydro_research_reaches.geojson` — unranked research objects; no engineering MW/head.
- `layers/39_reach_logistics_context.geojson` — join status only; no invented access route.
- `layers/40_hydro_opportunity_evidence_matrix.geojson` — documentation completeness only; no opportunity score.
- `GEOMETRY_INGESTION_LOG_PASS9.json` — records failed/deferred official binary ingestion.
- `sources_pass9.json` — controlled external/internal source registry.
- `QA_PASS9.json` — machine checks.


## Pass 11 — platform-native canonical fixtures

`data/processed/pass11/` is the first application-oriented migration package. It does not replace raw/pass GeoJSON provenance. It adds canonical entity/evidence/observation fixtures, PostGIS migrations, schemas, catalog configuration and publish fixtures.

Important migration rule: pass-numbered analysis windows, extraction jobs and readiness gates are **research/system objects**, not permanent domain layers. The only physical geometry in the pass-11 canonical fixture is the official WSC hydrometric-station Point geometry.


## Processed pass 12 datasets

`data/processed/pass12/` is an app-native hydrology evidence snapshot, not a new GIS layer stack. It contains the HYDAT source manifest, controlled sources/evidence/observations, updated hydrology screening states, ingestion jobs and metric registry.

The directory intentionally contains **no fabricated daily/monthly flow series**. Runtime DNS prevented official series download. Once executed in a network-enabled environment, raw responses must enter the platform through `raw → staging → research.observation_series / research.observation`, not directly into `core`.


## Pass 13 — integrated platform snapshot

`data/processed/pass13/` is an application-native snapshot, not a new layer-number series. It includes canonical communities/corridors/projects/assets, source/evidence/observation relations, the unranked screening override, the data-driven catalog, Showcase story configuration and immutable public-release fixtures.

Important semantics:

- community point geometry = legacy approximate centroid, not port/project coordinate;
- conceptual corridors = geometry null, not route/boundary;
- marine/fibre/energy context = evidence relations and observations;
- legacy tiers/no-go records = provenance only;
- public release omits legacy tiers;
- rights/governance remains research-required until authoritative evidence is added.


## Pass 14 — economic frontier datasets

`data/processed/pass14/` is the final broad-research economic snapshot. It is application-native scenario/evidence data, not a site financial model.

Key files:

- `research_economic_benchmark.jsonl` — external completed-project/funding/efficiency references; every benchmark has `usable_as_site_estimate=false`;
- `scenario_scenario.jsonl` — conventional-export, Kristal-local-compute and reference-frontier scenario templates;
- `scenario_assumption.jsonl` — sourced inputs plus explicit `UNPRICED` site-specific Kristal components;
- `scenario_sensitivity_case.jsonl` — 64 generic non-site distance stress cases;
- `economic_frontier_cases_public.csv` — public derived frontier table;
- `economic_frontier_summary_public.json` — public summary with explicit non-savings warnings;
- `sources_pass14.json` — controlled source subset;
- `catalog.pass14.json` and `story.pass14.json` — Explorer/Showcase configuration.

Pass 14 does not publish project NPV, IRR, site score, site rank or bankability.
