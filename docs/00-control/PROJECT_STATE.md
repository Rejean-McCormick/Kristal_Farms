# Project State

**As of:** 2026-08-30  
**Status:** Working synthesis of supplied materials plus project-owner strategic direction; not an engineering approval, environmental conclusion, market forecast or investment decision.

## 1. Strategic model — v3

The repository now distinguishes two layers:

### A. Source-supported baseline

The supplied internal reference and partner package consistently describe a cold-climate modular compute model that places compute close to local renewable energy and heat users, exports compute results over fibre, reuses server heat before rejection, uses black-box tenancy, and expands through staged, reversible deployment with community governance/FPIC and public metrics.

Primary internal reference: [`Kristal_Farms_Internal_Reference.md`](../10-core/Kristal_Farms_Internal_Reference.md)

### B. Owner strategic direction added 2026-08-17

The v3 platform framing broadens the project from a Nain-first hydro/compute application into a possible **northern compute infrastructure platform**. The strategic direction is to test whether Québec and Labrador can use cold climate, difficult-to-export renewable resources, fibre, coastal access, heat recovery, modular construction and differentiated physical/data security to support a network of compute nodes.

New strategic hypotheses include:

- local renewable consumption may avoid part of the cost and ecological footprint of long electrical transmission;
- coastal sites may support direct or advantageous subsea-fibre connectivity;
- decommissioned mines/brownfield infrastructure may support higher-security compute variants;
- a connected "northern fibre crown" could increase resilience and network value;
- accumulated cold-climate construction and operations expertise could become a strategic asset;
- future AI demand may create a large market for this infrastructure.

These are **not yet validated facts**. They have been converted into decisions, claims-to-validate and research workstreams.

Source classes:

- [`2026-08-17-strategic-direction.md`](../../sources/owner-direction/2026-08-17-strategic-direction.md)
- [`2026-08-17-international-learning-direction.md`](../../sources/owner-direction/2026-08-17-international-learning-direction.md)

Strategic narrative: [`PLATFORM_VISION_EN.md`](../10-core/strategy/PLATFORM_VISION_EN.md) / [`VISION_PLATEFORME_FR.md`](../10-core/strategy/VISION_PLATEFORME_FR.md)

## 2. Platform architecture

The v3 strategy separates the overall platform from site-specific architectures.

Current archetypes:

1. **Community-integrated node** — renewable energy + modular compute + heat reuse + local fibre/port/community integration.
2. **Coastal connectivity node** — marine logistics and potential terrestrial/subsea fibre advantage.
3. **Secure brownfield/mine node** — exploratory higher-security physical infrastructure; dedicated engineering required.
4. **Regional node** — larger scale only where energy, fibre, environmental, community/rights and economic conditions support it.

The existing detailed internal reference remains primarily the first archetype.

## 3. Current screening governance — unranked

The supplied raw village inventory and legacy My Maps preserve historical Tier 1/2/3/4 classifications, including Nain-first language. These classifications are now **provenance only** and do not control current decision use.

Effective 2026-08-30, the platform state is:

- `screening_mode = unranked`;
- `ranking_allowed = false`;
- Nain legacy priority = `legacy_priority_superseded_unranked`;
- Inukjuak/Innavik = `reference_case_not_ranked`;
- other communities = unranked evidence/context screening.

Pass 13 public community releases deliberately omit legacy tiers so the interface cannot recreate an implicit ranking. The complete legacy values remain inspectable through provenance/evidence.

Dataset: [`data/processed/pass13/screening_state_override_pass13.csv`](../../data/processed/pass13/screening_state_override_pass13.csv)

## 4. Labrador hydro evidence base

The supplied Labrador hydro dataset contains **58 records** across operating, planned, partially harnessed, unexploited, preliminary, interprovincial, former and small-hydro categories.

- 57 records are marked mappable.
- 22 records are explicitly marked `needs_review = true`.
- The data carries a `status_checked_date` field and must be treated as dated source evidence, not timeless project truth.

Datasets:

- [`labrador_hydroelectric_potential.csv`](../../data/raw/labrador_hydroelectric_potential.csv)
- [`labrador_hydro_google_mymaps_points_v1.csv`](../../data/raw/labrador_hydro_google_mymaps_points_v1.csv)

## 5. Deployment concept

The supplied EN/FR gradual-deployment documents propose a broader sequence:

**coastal wind → local training → construction energy → site preparation → fibre/monitoring → small hydro assets → modular compute → heat recovery → expansion**

The v3 strategy generalizes this as an **integration sequence** rather than making coastal wind mandatory everywhere. The exact order remains site-dependent.

Working documents:

- [`Gradual_and_Harmonious_Deployment_Plan_EN.md`](../10-core/deployment/Gradual_and_Harmonious_Deployment_Plan_EN.md)
- [`Plan_de_deploiement_graduel_et_harmonieux_FR.md`](../10-core/deployment/Plan_de_deploiement_graduel_et_harmonieux_FR.md)

## 6. Québec / Nunavik research

The current source set adds:

- river inventories north of Chisasibi / La Grande;
- west-coast Nunavik transmission-cost screening;
- precipitation source data;
- broader community screening.

These expand the evidence base, but the current numbered partner package remains Labrador-coast/Nain-first. Nunavik therefore remains a **research and replication/screening workstream** unless a project-scope decision changes that.

## 7. Transmission avoidance and ecological footprint

The repository includes a working transmission-cost screen and partner documents that argue for short MV/local delivery rather than new long HV corridors. This supports the **question** of transmission avoidance but does not yet prove a universal cost or environmental advantage.

The v3 requirement is a site-specific comparison that includes both sides of the system: generation, local feeder, compute, fibre, cooling/heat infrastructure versus the realistic electrical-export alternative, including lifecycle land/ecological effects.

Research agenda: [`STRATEGIC_INFRASTRUCTURE_RESEARCH_AGENDA.md`](../30-site-screening/infrastructure/STRATEGIC_INFRASTRUCTURE_RESEARCH_AGENDA.md)

## 8. Fibre / subsea strategy

Existing documents already treat fibre as essential because the project exports compute rather than electricity. The new owner direction elevates coastal/subsea fibre and a possible northern fibre ring/crown to a strategic platform workstream.

Current status: **concept / screening only**. No specific marine route, landing point, capacity, right, permit, cost or carrier arrangement is validated by the current repository.

## 9. Data security and secure-site variants

The existing black-box model is well developed in the internal reference and partner package: the host manages physical infrastructure while tenant data, models, software and logs remain outside the host boundary.

The v3 strategy adds a separate research track for **decommissioned mines and hardened brownfield sites** as potential higher-physical-security compute locations.

Current status: **site-archetype hypothesis only**. The repository contains no completed mine candidate inventory or mine-specific geotechnical, fire/life-safety, ventilation, flooding, remediation, power or fibre feasibility.

## 10. Economics

The repository includes:

- the existing partner cost workbook;
- an economic cost-advantage and savings model;
- a Canada server-farm cost distribution/cooling report;
- a west-Nunavik transmission-cost benchmark.

These are useful working inputs, but several inputs are market-, tariff-, project- or date-sensitive and require refresh/validation before use as hard partner or investor claims.

The workbook remains an illustrative cost-index conversation model (100 conventional vs 40 Kristal Farms, savings gap 60); final values require engineering, tariffs, site selection, heat demand, fibre design and partner commitments.

## 11. Future AI compute opportunity

The v3 strategy positions growing AI compute intensity as a possible long-term demand driver for a Québec–Labrador platform.

Current status: **strategic market hypothesis**. The repository does not yet contain a validated forecast of AI demand, tenant commitments, addressable market, regional market share, rack density trajectory or required capacity.

## 12. Human infrastructure / welcoming-community concept

The owner vision also extends beyond technical infrastructure toward climate-adapted northern living environments and, over the long term, the possibility of welcoming voluntary culturally distinct newcomer communities through lawful pathways. The working concept emphasizes high-quality indoor civic space, housing, health, education, food production, culture, flexible use of favourable outdoor conditions, portability and a real right to leave rather than a company-town dependency.

Current status: **long-term strategic concept only**. No immigration pathway, settlement partner, funding model, community agreement or operating program is established by the current repository. Specific communities should not be presented as committed participants without actual partnership and consent.

This concept is explicitly separated from territorial politics. Separatism, border revision, sovereignty disputes and internationalization of Labrador as a jurisdictional objective are outside project scope. See [`SCOPE_BOUNDARIES.md`](SCOPE_BOUNDARIES.md).

Strategy: [`HUMAN_INFRASTRUCTURE_VISION_EN.md`](../10-core/strategy/HUMAN_INFRASTRUCTURE_VISION_EN.md) / [`VISION_INFRASTRUCTURE_HUMAINE_FR.md`](../10-core/strategy/VISION_INFRASTRUCTURE_HUMAINE_FR.md)


## 13. International learning / university pathway

The latest owner direction adds a distinct education and research layer. The long-term concept is to convert real northern infrastructure expertise into technical training, applied research, visiting-student/research programs, recognized joint credentials and, only where the necessary approvals and governance exist, potential university institutions.

A defining principle is **skills circulation**: some learners may come from other countries or communities for a defined period, build practical and academic capabilities, and return with portable skills, credentials and professional networks. International participation is therefore not synonymous with permanent settlement.

The proposed language model aims, where the host people so choose and to the maximum extent permitted by applicable law, to designate the language or languages of the host people as official local institutional languages within project-controlled community/cultural life, while using translation and additional working languages for science and international exchange.

Culture, rites, religion and customs are supported within a common Human Dignity Framework that also protects individual consent, equality, safety, freedom of conscience, privacy, child safeguarding, independent remedy and a real ability to leave.

Current status: **long-term strategic concept / governance design**. No Kristal Farms site is represented as an accredited university, and the repository contains no established degree-granting authority, academic accreditation, international-student quota or institutional partner commitment.

Strategy:

- [`INTERNATIONAL_LEARNING_VISION_EN.md`](../10-core/strategy/INTERNATIONAL_LEARNING_VISION_EN.md) / [`VISION_APPRENTISSAGE_INTERNATIONAL_FR.md`](../10-core/strategy/VISION_APPRENTISSAGE_INTERNATIONAL_FR.md)
- [`HUMAN_DIGNITY_FRAMEWORK_EN.md`](../10-core/strategy/HUMAN_DIGNITY_FRAMEWORK_EN.md) / [`CADRE_DIGNITE_HUMAINE_FR.md`](../10-core/strategy/CADRE_DIGNITE_HUMAINE_FR.md)

## 14. Bilingual partner package

For each numbered partner document `00` through `14`, the repository retains:

- English Markdown;
- English PDF;
- French PDF;
- French DOCX with logo;
- searchable Markdown extraction of the French DOCX.

These files represent the **v1 Nain/Labrador partner package**. They predate the full v3 platform framing and are therefore not considered synchronized with the new strategic layer until rebuilt/reviewed.

See [`BILINGUAL_MATRIX.md`](BILINGUAL_MATRIX.md) and [`V3_REBUILD_MAP.md`](../20-partner-package/V3_REBUILD_MAP.md).

## 15. Known source hygiene issue

At least one Nunavik research document and the existing deep-research report contain assistant/UI-style citation artifacts such as `turn...search`, `filecite`, or private-use citation markers. These are **not publication-ready citations**.

See [`CONTENT_SANITATION.md`](CONTENT_SANITATION.md).


## 14. Hydro Resource Atlas — pass 9

Pass 9 establishes a **24-river hydrometric evidence atlas** spanning Côte-Nord/Basse-Côte-Nord, Nunavik and Labrador. Each record has an official WSC station position and station-linked drainage-area value. No new dam site, head, design flow, MW estimate or project ranking is asserted.

Official WSC basin packages (`MDA_ADP_02.zip`, `MDA_ADP_03.zip`), GRHQ hydrography, Canada1Water/NHN and HRDEM were identified as the source stack. Binary basin/flowline ingestion was not successful in the current execution environment, so basin and river-line geometry remain null.

Method: [`HYDRO_RESOURCE_ATLAS_METHOD.md`](../30-site-screening/hydro-atlas/HYDRO_RESOURCE_ATLAS_METHOD.md)  
Report: [`PASS9_HYDRO_RESOURCE_ATLAS.md`](../30-site-screening/hydro-atlas/PASS9_HYDRO_RESOURCE_ATLAS.md)


## 15. Geometry / terrain pipeline — pass 10

Pass 10 confirms **24/24** Hydro Resource Atlas WSC station IDs are present in the official national basin-polygon inclusion registry. The current execution container still cannot resolve the WSC/GRHQ/NRCan service hosts, so actual basin/flowline/DTM assets remain non-ingested.

The repository now contains a deterministic fail-closed pipeline under `scripts/pass10/`, operational request windows, source schemas and a mandatory manual connected-reach review gate. Request-window polygons are **not basin or project boundaries**. No new project head, design flow, MW or site rank is introduced.

Report: [`PASS10_GEOMETRY_TERRAIN_PIPELINE.md`](../30-site-screening/hydro-atlas/PASS10_GEOMETRY_TERRAIN_PIPELINE.md).


## Platform state — Pass 11

The uploaded **Kristal Farms application architecture v0.1** is an **architecture proposal**, not an externally validated technical fact. Pass 11 uses it to define a compatible data foundation without treating it as geographic evidence.

Current implementation state:

- PostGIS-oriented schema/migration SQL prepared;
- canonical `core.entity` identity model added for stable cross-interface IDs;
- `core.natural_feature` added for rivers/watersheds/reaches;
- Pass 9/10 WSC station and river research converted to canonical fixtures;
- evidence, source, observation, screening-state and ingestion-job fixtures generated;
- no live PostGIS instance was started in this runtime;
- no flow series, river line, watershed polygon, project head, design flow, MW or ranking was fabricated.

The proposed architecture remains evolvable; Pass 11 ADRs are accepted for the foundation package, not declarations that all future product decisions are closed.


### Pass 12 hydrology state

The 24 Hydro Resource Atlas rivers now have an app-native HYDAT ingestion contract and source/version provenance. Current status remains **partial** because the full daily/monthly/annual source series could not be materialized in this runtime. Natashquan has additional current CEHQ metadata and a historical government flow summary; Alexis has documented long-record/regression-reference evidence. No river receives design flow, MW or ranking from these records.


## 15. App-native integrated atlas — Pass 13

Pass 13 connects the Hydro Resource Atlas to community, marine, telecom, energy and evidence context through canonical IDs and relations. Exact geometry is not required for knowledge objects: conceptual corridors, fibre/service context and external projects remain geometry-null when no controlled geometry is ingested.

The public snapshot is release `2026.08.30-pass13`; live research remains separate. Environment and rights/governance remain research-required rather than inferred from legacy screening or geographic proximity.

See [`PASS13_INTEGRATED_ATLAS.md`](../60-application-data/PASS13_INTEGRATED_ATLAS.md).


## Pass 14 — broad research phase complete

The cross-project research phase now has an integrated atlas, versioned hydrology model and evidence-backed economic frontier. The central architecture remains a thesis to test site-by-site: new remote generation + protected community interface + flexible local compute + fibre export can avoid/reduce long road and HV export burdens at some sites.

Pass 14 does **not** establish bankability or a preferred river. Future work moves to corridor/site dossiers with real engineering, logistics, fibre quotations, environmental/rights work and commercial terms.
