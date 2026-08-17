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
