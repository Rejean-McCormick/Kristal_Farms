# Mine Reuse Screening Method

**As of:** 2026-08-31  
**Status:** C4 research method / unranked screening.  
**Purpose:** Evaluate mine infrastructure as a possible input to a Kristal Farms corridor dossier without treating a mine marker as evidence of project feasibility.

## 1. Scope

Kristal Farms may examine mining assets in northern Québec and Labrador in three non-exclusive roles:

1. **subsurface compute / hardened infrastructure reuse** — reuse of modern underground workings or mine-service infrastructure;
2. **mine-pit energy storage** — reuse of open pits as pumped-storage reservoirs;
3. **surface brownfield reuse** — reuse of roads, camps, airstrips, workshops, utility corridors or previously disturbed industrial land.

A single site can have more than one role, but each role must be evaluated independently.

## 2. No-ranking rule

This method does **not** create a mine score, traffic-light preference, ordered shortlist or hidden suitability rank. `ranking_allowed = false` remains controlling.

The permitted output is a set of dimension states such as:

- evidence available / missing;
- technically plausible / not yet tested;
- constraint identified;
- current use conflict;
- legal or restoration status unresolved;
- no-go only where a clear controlling constraint is established.

## 3. Lifecycle classification

Record the mine lifecycle explicitly:

- `ACTIVE`
- `CARE_AND_MAINTENANCE`
- `SUSPENDED`
- `CLOSURE_RESTORATION`
- `CLOSED_RECENT`
- `CLOSED_HISTORICAL`
- `ABANDONED_STATE_LIABILITY`
- `RESTORED_OR_RELEASED`
- `UNKNOWN`

Do not collapse these states into “abandoned.” In Québec, an abandoned mine under State responsibility has a specific restoration/liability meaning and is not equivalent to a recently idled privately controlled mine.

## 4. Reuse classes

### A. Underground / compute infrastructure

Research preference:

- recent cessation or care-and-maintenance status;
- documented ramp/shaft/cavern geometry;
- maintained dewatering and ventilation;
- intact electrical distribution and communications;
- independent egress potential;
- all-season logistics or credible seasonal operating plan.

Recency is a **useful predictor of asset preservation**, not proof of availability or suitability.

### B. Mine-pit pumped storage

Mine age is **not** an exclusion criterion. Required evidence is driven by physics and environmental constraints:

- usable pit volume and operating water-level range;
- vertical separation between reservoirs under operating conditions;
- hydraulic distance and tunnel/penstock concept;
- rock-mass and pit-wall stability under cyclic water levels;
- seepage and groundwater connectivity;
- water chemistry, acid-rock drainage and contaminant mobilization;
- environmental and rights/governance acceptability;
- grid or local-system value for charging and discharge.

### C. Surface brownfield

Treat existing roads, airstrips, camps, utility corridors, foundations and industrial pads as **observed assets only where current evidence confirms they still exist and can legally be reused**.

## 5. Required fields

Use `metadata` during research until a stable governed mine model is justified. Recommended fields:

```text
mine_method                    open_pit | underground | mixed | unknown
lifecycle_status
last_operating_date
care_maintenance_status
owner_or_responsible_party
restoration_status
current_use_conflict

# underground reuse
ramp_access_known
shaft_depth_m
underground_extent_known
flooding_status
dewatering_status
ventilation_status
ground_support_status
underground_substations_known
surface_powerhouse_known
communications_infrastructure_known

# reservoir reuse
pit_geometry_source
pit_usable_volume_m3
upper_operating_level_m
lower_operating_level_m
gross_head_m
hydraulic_distance_km
lower_reservoir_type           mine_pit | constructed | freshwater | ocean | unknown
seawater_exposure
seepage_status
pit_wall_stability_status
acid_rock_drainage_status
contamination_status

# common enabling infrastructure
historical_power_voltage_kv
historical_load_mw
current_available_capacity_mw  # never infer from historical load
road_access
airstrip_access
rail_access
fibre_evidence
community_rights_context
```

## 6. Critical semantic rules

- `historical_power_mw` **is not** `current_available_capacity_mw`.
- `mine_depth_m` **is not** hydraulic head.
- `pit_volume_m3` **is not** usable operating volume.
- a flooded pit **is not** automatically a reservoir that may be cycled.
- an underground mine **is not** automatically safe or code-compliant for occupied compute use.
- “care and maintenance” **is not** “available for Kristal Farms.”
- restoration liability, land rights, mining titles and acquisition rights must be established separately.
- infrastructure reuse must not interfere with required closure, remediation or environmental monitoring.

## 7. Promotion gate

A mine-related record may be promoted from exploratory research toward a corridor/site dossier only when the evidence pack identifies:

1. legal owner/responsible party and lifecycle status;
2. source-backed geometry/infrastructure condition;
3. environment/restoration obligations;
4. rights-holder/community context;
5. power and telecom evidence;
6. engineering questions and next field verification;
7. explicit unknowns and current-use conflicts.

Promotion means **deeper study**, not selection.

## 8. Authoritative starting sources

- Gouvernement du Québec — mining activity maps, including active and care-and-maintenance mines: https://www.quebec.ca/en/agriculture-environment-and-natural-resources/mining/mining-data-maps/maps-mining-activities
- Gouvernement du Québec — abandoned mine restoration program: https://www.quebec.ca/en/agriculture-environment-and-natural-resources/mining/mining-reclamation/restoration-abandoned-mining-site/work-plan-investments
- Gouvernement du Québec — mine-site reclamation requirements and liability context: https://www.quebec.ca/agriculture-environnement-et-ressources-naturelles/mines/restauration-miniere/a-propos

These registries are starting points. Project use requires current site-specific evidence.
