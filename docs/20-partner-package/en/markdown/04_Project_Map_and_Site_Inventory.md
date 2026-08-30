# 04_Project_Map_and_Site_Inventory

**Project:** Kristal Farms — Labrador Coast Partner Package  
**Document type:** Partner-facing map and site inventory brief  
**Version:** v0.1 draft  
**Status:** Working draft pending final KML/CSV validation  
**Primary geography:** Labrador coast  
**First target:** Nain, Nunatsiavut, Labrador  
**Replication logic:** Hopedale, Makkovik, Postville, Rigolet, and other coastal-accessible Labrador communities where the same hydro/compute/heat model may be screened.

---

## 1. Purpose

This document explains the project map package and the site-selection inventory for Kristal Farms’ Labrador coast opportunity.

The map package is designed to help partners quickly understand:

1. why the project starts with **Nain**;
2. which Labrador coastal features matter for site selection;
3. which features are included in the current map inventory;
4. which features are deliberately excluded from the partner package;
5. what data still needs validation before engineering, investment, permitting, or community decisions.

The map is not intended to be a final engineering drawing, permitting map, land-rights map, or construction layout. It is a partner-screening tool that organizes the current thesis: **use local coastal hydro, place modular compute near village heat users, export compute by fibre, reuse heat locally, and expand by replicating the model across coastal communities rather than by pursuing inland megaprojects.**

---

## 2. Partner-facing map package

The intended map/data package is:

```text
04_Project_Map_and_Site_Inventory.md
maps/
  kristal_farms_LABRADOR_COAST_PROJECT_ONLY_colored.kml
  kristal_farms_LABRADOR_COAST_PROJECT_ONLY_feature_inventory.csv
  kristal_farms_LABRADOR_COAST_PROJECT_ONLY_validation.csv
```

### Current status

| File | Status | Use |
|---|---|---|
| `kristal_farms_LABRADOR_COAST_PROJECT_ONLY_colored.kml` | Pending final attachment/validation | Visual map layer for Google Earth or GIS viewers. |
| `kristal_farms_LABRADOR_COAST_PROJECT_ONLY_feature_inventory.csv` | Pending final attachment/validation | Structured inventory of mapped features. |
| `kristal_farms_LABRADOR_COAST_PROJECT_ONLY_validation.csv` | Pending final attachment/validation | Evidence and validation status for each mapped feature. |

Until the KML/CSV files are final, this document should be read as the **map architecture and inventory specification**, not as a final map release.

---

## 3. Project map logic

The map should show only the Labrador coast project logic. It should not become a general northern hydro map, a Nunavik planning map, or a map of every possible dam or data center concept.

The selected map logic is:

```text
Labrador coast focus
  → Nain as first target
  → coastal-accessible hydro screening
  → village-first compute pad siting
  → heat users near the pad yard
  → short MV electrical connection
  → fibre export of compute output
  → replication across other coastal communities
```

This means the map should prioritize features that help answer practical partner questions:

- Where is the first community target?
- Where is the candidate hydro resource?
- Is there plausible marine access?
- Can containers be placed near heat users?
- Can heat be delivered through short pipe runs?
- Is a short MV power connection plausible?
- Is fibre connectivity a required dependency?
- Which sites are included only as replication candidates?
- Which sites are excluded because they distract from the coastal community-scale model?

---

## 4. Included map layers

The KML should use clear, limited layers. Each layer should have a practical partner-facing purpose.

### Layer 1 — Project geography

**Purpose:** Define the geographic scope of the partner package.

Include:

- Labrador coast project boundary or focus corridor;
- Nunatsiavut / Labrador coastal community context, where appropriate and validated;
- Nain as the first target community;
- replication communities for later screening.

Do not include broad Canada-wide or global strategy layers in this partner map.

---

### Layer 2 — First target: Nain

**Purpose:** Make Nain visually and strategically central.

Include:

- Nain community marker;
- Nain harbour / marine access marker, if validated;
- possible village-edge or port-edge compute pad screening zone;
- nearby public heat users to be validated;
- possible greenhouse heat-use area to be validated.

Nain should be marked as:

```text
Priority 1 — first target / site-confirmation candidate
```

The map should not imply final land control, final pad location, final permits, or final community approval.

---

### Layer 3 — Candidate hydro resource

**Purpose:** Show the current hydro screening basis.

Include:

- Fraser River / Nain-area hydro candidate marker or screening corridor;
- hydro intake / powerhouse concepts only if sourced and clearly preliminary;
- hydro-to-village short MV connection concept line, if available;
- evidence status for capacity estimates and field-validation needs.

Current source basis identifies Fraser River near Nain as a potential community-scale hydro candidate in the approximate 15–20 MW range. This should be labeled as **preliminary source basis — not bankable engineering data**.

Recommended map label:

```text
Fraser River / Nain Hydro Candidate
Status: preliminary screening
Capacity: source basis indicates ~15–20 MW; requires hydrology, geotechnical, environmental, Indigenous governance, and engineering validation
Role: potential local hydro supply for village-first compute/heat model
```

---

### Layer 4 — Electrical connection concept

**Purpose:** Show the preferred infrastructure logic: avoid long high-voltage transmission.

Include:

- candidate short medium-voltage connection from hydro source to village substation;
- village substation or energy hub placeholder;
- compute pad feeder concept;
- metering handoff points, if available at concept level.

Recommended label:

```text
Short MV Feed Concept
Purpose: connect local hydro to village energy hub / compute pad yard without long HV transmission build-out
Status: concept only; route and voltage class require utility and engineering review
```

Do not include speculative long HV corridors or inland transmission extensions.

---

### Layer 5 — Compute pad yard

**Purpose:** Show where modular compute containers would logically sit.

The current design logic is village-first: data containers should be near heat users, not remote at the dam.

Include:

- candidate compute pad yard screening zone;
- port-edge or village-edge logistics access, if validated;
- fencing / controlled access area concept;
- distance to heat users and fibre access points, if known.

Recommended label:

```text
Compute Pad Yard Screening Zone
Purpose: modular black-box compute containers near heat users and logistics access
Status: screening zone only; final site requires land, geotechnical, community, permitting, fibre, utility, and thermal-loop validation
```

---

### Layer 6 — Heat users and thermal loop

**Purpose:** Show that heat reuse is not a side benefit; it is part of the site-selection logic.

Include candidate or validated heat users such as:

- public buildings;
- homes or housing clusters;
- school / clinic / community buildings, if validated;
- greenhouse site or greenhouse screening area;
- thermal storage location, if applicable;
- short district heat loop concept.

Recommended label:

```text
Heat Reuse Candidate
Priority: public buildings and homes first; greenhouse as seasonal/summer sink
Status: candidate only unless confirmed by building audits and community process
```

Do not map private buildings as confirmed heat offtakers unless consent and validation exist.

---

### Layer 7 — Cooling source / rejection safeguard

**Purpose:** Show the heat-first cooling hierarchy and environmental safeguards.

Include:

- seawater/bay non-contact heat exchanger concept location, if validated;
- dry-cooler backup zone, if applicable;
- no-contact environmental exchange note;
- exclusion note for small rivers as primary heat sink.

Recommended label:

```text
Cold Source / Backup Heat Rejection Concept
Rule: reuse → store → reject
Design: non-contact plate heat exchange; IT loop and building/environment loops remain sealed and separate
Status: requires environmental, marine, thermal, corrosion, and permitting review
```

---

### Layer 8 — Fibre / connectivity dependency

**Purpose:** Show that the project exports compute, not electricity.

Include:

- known or candidate fibre landing / network point, if validated;
- NOC / network handoff placeholder;
- fibre dependency note;
- redundancy requirement or path-protection note, if known.

Recommended label:

```text
Fibre / Network Dependency
Purpose: export compute results and tenant traffic, not bulk electricity
Status: availability, latency, redundancy, service provider, and SLA must be validated
```

Do not imply tenant data visibility by the host. The map should show physical network dependency only.

---

### Layer 9 — Replication communities

**Purpose:** Show expansion logic without diluting the Nain-first pitch.

Include markers for:

- Hopedale;
- Makkovik;
- Postville;
- Rigolet;
- other Labrador coastal locations only if relevant and sourced.

Recommended label:

```text
Replication Screening Community
Status: future screening only
Role: potential Labrador coast replication candidate if hydro, heat, fibre, logistics, governance, and community value conditions are met
```

These communities should not be presented as selected sites unless separate due diligence has been completed.

---

## 5. Excluded map layers

The partner-facing map should deliberately exclude distracting or non-canonical layers.

| Excluded layer | Reason for exclusion |
|---|---|
| Churchill Falls / inland mega-hydro project layers | The Labrador coast package is not pursuing inland megaprojects or long-transmission strategies. |
| Broad Nunavik mega-river development layers | Useful as background only; distracts from Nain-first Labrador coast focus. |
| Global AI infrastructure layers | Belongs in archive/background, not this site inventory. |
| Manicouagan-specific proposal layers | Not part of the Labrador coast partner package. |
| Speculative financial zones or revenue areas | Not validated and not appropriate for a map inventory. |
| Unconfirmed private property / land access claims | Land status must be verified before mapping as available. |
| Final engineering alignments | This document is pre-feasibility / partner-screening level. |
| Sensitive cultural, ecological, or community sites | Should not be mapped externally unless approved through the proper community and governance process. |

---

## 6. Why certain sites are removed or de-prioritized

The map inventory should use a transparent removal logic. A site can be removed, archived, or de-prioritized for any of the reasons below.

### 6.1 Inland / transmission-heavy sites

Sites are removed from the partner-facing package if they require large inland transmission build-out, new long high-voltage corridors, or major remote substations. This conflicts with the project thesis: **use local hydro near coastal communities and export compute by fibre instead of exporting electricity by long transmission.**

### 6.2 Mega-dam or reservoir-heavy concepts

Large hydro concepts that require major reservoirs, large flooding areas, or significant river-system transformation are not part of the current partner thesis. They may remain in the internal source archive as comparison material, but they should not be presented as part of the Labrador coast community-scale model.

### 6.3 Poor heat-use geography

Sites are de-prioritized if compute containers cannot be located near real heat users. A technically attractive hydro site is not enough. The heat-first model requires short, practical thermal distribution to public buildings, homes, or greenhouse loads.

### 6.4 Weak marine or seasonal logistics access

Coastal-accessible sites are preferred because the project relies on modular container logistics. Sites requiring major roadwork, repeated long-haul trucking, or complex inland access are weaker candidates.

### 6.5 Unclear fibre dependency

Compute can be powered locally, but the business model depends on data connectivity. Sites without a credible fibre path, network partner, redundancy plan, or acceptable latency profile should be marked as unresolved or de-prioritized.

### 6.6 Environmental or governance sensitivity

Sites are removed or held back if they overlap with protected areas, sensitive habitat, unresolved rights issues, or community concerns that have not been addressed. No site should be advanced without a proper FPIC/community process and environmental review.

### 6.7 Inconsistent with Nain-first sequencing

A site may be technically interesting but still excluded from the first package if it distracts from the initial partner story. The first partner package should prove one clear model: Nain first, then Labrador coastal replication.

---

## 7. Site inventory structure

The feature inventory CSV should use a simple, auditable structure.

Recommended fields:

```text
feature_id
feature_name
feature_type
community
region
latitude
longitude
geometry_type
priority_level
status
source_basis
validation_status
partner_relevance
included_in_kml
included_in_partner_package
exclusion_reason
next_evidence_needed
notes
```

### Feature types

Use controlled feature types such as:

```text
community
hydro_candidate
port_or_marine_access
compute_pad_screening_zone
heat_user_candidate
greenhouse_candidate
thermal_storage_candidate
village_substation_candidate
mv_connection_concept
fibre_or_network_point
cooling_source_candidate
dry_cooler_backup_zone
replication_screening_community
excluded_site
archive_reference
```

### Priority levels

Use three priority levels:

| Priority | Meaning |
|---|---|
| **Priority 1** | Nain-first features required to evaluate the initial pilot. |
| **Priority 2** | Labrador coast replication screening features. |
| **Priority 3** | Background, archive, or comparison features not included in the first partner package. |

### Validation status

Use standard validation statuses:

| Status | Meaning |
|---|---|
| **Confirmed** | Supported by verified source, reviewed, and safe to use externally. |
| **Preliminary** | Source basis exists but requires validation before partner reliance. |
| **Concept** | Planning logic only; no validated site evidence yet. |
| **To validate** | Needs external evidence, partner input, or field work. |
| **Excluded** | Deliberately removed from partner package. |
| **Internal only** | May be useful, but not for external distribution. |

---

## 8. Current working site inventory

The following inventory is a working partner-facing structure. Coordinates and geometry should be populated only from validated KML/CSV/GIS sources.

| Feature ID | Feature | Type | Priority | Status | Partner relevance | Next evidence needed |
|---|---|---:|---:|---|---|---|
| KF-LAB-001 | Nain | Community / first target | 1 | Preliminary / to validate | First site-confirmation candidate | Community process, heat-load audit, land/pad screening, fibre status, utility input. |
| KF-LAB-002 | Fraser River / Nain hydro candidate | Hydro candidate | 1 | Preliminary | Possible local hydro supply for pilot model | Hydrology, flow seasonality, head, geotechnical, environmental, cost, permits, Indigenous governance. |
| KF-LAB-003 | Nain harbour / marine access | Port/logistics | 1 | To validate | Container delivery and modular logistics | Port capacity, sealift window, crane/lift limits, staging area, ice/seasonality. |
| KF-LAB-004 | Nain compute pad screening zone | Compute pad | 1 | Concept | Village-first container yard near heat users | Land access, geotech, noise, security, zoning, community acceptance, fibre/power access. |
| KF-LAB-005 | Nain public-building heat users | Heat users | 1 | To validate | Core community benefit and diesel displacement | Building list, heating systems, load profile, radiator temperatures, metering, owner consent. |
| KF-LAB-006 | Nain greenhouse candidate | Seasonal heat sink | 1 | Concept | Summer/warm-month heat use and food value | Greenhouse operator, site, thermal load, economics, water, staffing, governance. |
| KF-LAB-007 | Nain village substation / energy hub | Electrical node | 1 | Concept | Power handoff from hydro to pads and heat systems | Utility design, voltage, protection, metering, ownership, interconnection review. |
| KF-LAB-008 | Short MV hydro-to-village feed | Electrical route | 1 | Concept | Avoids long HV transmission | Route survey, land rights, cost, utility standards, environmental constraints. |
| KF-LAB-009 | Fibre / NOC handoff | Connectivity | 1 | To validate | Required for compute export and tenant SLA | Provider, capacity, latency, redundancy, outage history, service agreement. |
| KF-LAB-010 | Bay/seawater non-contact cold source | Cooling/rejection safeguard | 1 | Concept | Backup heat rejection and cooling resilience | Marine study, intake/rejection feasibility, corrosion design, thermal limits, permitting. |
| KF-LAB-011 | Hopedale | Replication community | 2 | Future screening | Labrador coast replication candidate | Hydro/fibre/heat/logistics/community screening. |
| KF-LAB-012 | Makkovik | Replication community | 2 | Future screening | Labrador coast replication candidate | Hydro/fibre/heat/logistics/community screening. |
| KF-LAB-013 | Postville | Replication community | 2 | Future screening | Labrador coast replication candidate | Hydro/fibre/heat/logistics/community screening. |
| KF-LAB-014 | Rigolet | Replication community | 2 | Future screening | Labrador coast replication candidate | Hydro/fibre/heat/logistics/community screening. |
| KF-LAB-015 | Churchill Falls / inland mega-hydro | Excluded reference | 3 | Excluded | Not part of the current package | Keep as internal comparison only. |
| KF-LAB-016 | Broad Nunavik mega-river sites | Archive/comparison | 3 | Internal only | Shows why community-scale/coastal model is preferred | Use only in hydro appendix or exclusion logic. |
| KF-LAB-017 | Manicouagan-specific concept | Archive/comparison | 3 | Internal only | Older proposal geography; not Labrador package | Keep in internal source archive. |

---

## 9. Map legend

Recommended visual legend:

| Symbol / color | Feature type | Meaning |
|---|---|---|
| Large star | First target | Nain first target. |
| Blue circle | Hydro candidate | Candidate hydro source or hydro screening area. |
| Blue line | MV connection concept | Conceptual short medium-voltage connection. |
| Orange square | Compute pad | Candidate modular container pad yard. |
| Red / heat icon | Heat user | Public building, housing cluster, greenhouse, or thermal load. |
| Green house icon | Greenhouse | Seasonal heat sink / food-production opportunity. |
| Purple line / point | Fibre / NOC | Connectivity dependency or handoff. |
| Anchor icon | Marine logistics | Port, harbour, or sealift staging feature. |
| Grey marker | Excluded / archive | Not part of partner-facing first package. |
| Dashed outline | Screening zone | Conceptual area, not final site control. |

The KML should avoid visual clutter. Nain-first features should be visually dominant. Replication communities should be visible but secondary.

---

## 10. Validation checklist

Before release to a partner, each mapped feature should be checked against this list.

| Validation question | Required before external use? |
|---|---:|
| Is the feature name correct? | Yes |
| Are coordinates accurate enough for partner screening? | Yes |
| Is the feature clearly marked as confirmed, preliminary, concept, or excluded? | Yes |
| Is the source basis identified? | Yes |
| Is any sensitive community, cultural, or ecological information removed or generalized? | Yes |
| Does the feature imply land control or approval that has not been granted? | Must not |
| Does the feature imply final engineering design? | Must not |
| Does the feature support the Nain-first Labrador coast thesis? | Yes |
| Is the feature needed for partner decision-making? | Yes |
| Is the next evidence needed clearly stated? | Yes |

---

## 11. Recommended evidence package for site confirmation

The map inventory should lead to a focused evidence request, not a broad research exercise.

### For Nain / first target

Required next evidence:

1. community engagement and FPIC pathway;
2. hydro resource confirmation for the Fraser River / Nain candidate;
3. preliminary environmental screening;
4. port and sealift logistics review;
5. candidate pad-yard land screening;
6. short MV connection concept review with utility/engineering input;
7. fibre availability, redundancy, and SLA review;
8. heat-load audit for public buildings and housing clusters;
9. greenhouse feasibility and operator model;
10. permitting and governance map.

### For replication communities

Required next evidence:

1. community interest and governance pathway;
2. local or nearby hydro potential;
3. practical village-first siting option;
4. heat users within short thermal-loop distance;
5. fibre availability;
6. marine logistics access;
7. environmental constraints;
8. local economic and training opportunities.

---

## 12. Partner use of this document

A partner should use this document to decide whether to proceed to a more detailed site-confirmation phase.

The immediate decision questions are:

1. Is the Nain-first site logic credible enough to begin formal site confirmation?
2. Which partner can validate hydro, power connection, fibre, marine logistics, land, or community process?
3. Which mapped features are strong enough to keep in the partner package?
4. Which features should be moved to the internal archive?
5. What evidence is required before investment-grade diligence?

---

## 13. Source basis

This map inventory is based on the current Kristal Farms source corpus, especially:

- **Potentiel hydroélectrique isolé au Nunavik et au Labrador (≥ 15 MW)** — hydro screening basis and Labrador/Nain preliminary hydro candidate logic.
- **Kristal Farms — Heat Recycling Plan** — village-first siting, reuse → store → reject, two sealed circuits, non-contact exchange, public-building and greenhouse heat logic.
- **Kristal Farms — Cost Advantage & Strategic Rationale** — no long HV transmission, natural cold, heat as value, marine logistics, modular pads, export compute by fibre.
- **Kristal Farms Internal Reference Document** — technical architecture, local hydro integration, village substation, compute pads, heat loop, fibre/NOC, phasing.
- **Documentation Kristal Farms** — black-box tenancy boundary, SLA, governance, FPIC, metrics and validation framing.

---

## 14. Open items before v1 release

The following items must be completed before this file becomes a final partner-facing release:

- attach or generate the final Labrador-only KML;
- attach or generate the final feature inventory CSV;
- attach or generate the final validation CSV;
- confirm whether Nain harbour, pad-yard, heat-user, fibre, and cold-source points can be shown externally;
- remove or generalize sensitive community/environmental features;
- review all labels for overclaiming;
- confirm partner-facing status of Fraser River / Nain hydro estimate;
- confirm source names and version dates;
- align this file with `02_Labrador_Coast_Project_Thesis.md` and `05_Labrador_Coast_Hydro_Screening_Appendix.md` once drafted.

---

## 15. Distribution status

**Recommended distribution:** partner-facing after review.  
**Do not distribute as final until:** KML/CSV files are attached and validation statuses are reviewed.  
**Internal-only material:** raw hydro tables, old Nunavik mega-project material, Manicouagan proposal layers, unresolved land/rights data, unvalidated private heat-user locations, and any sensitive community/ecological sites.
