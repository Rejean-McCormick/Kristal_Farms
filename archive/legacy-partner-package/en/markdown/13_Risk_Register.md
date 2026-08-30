# 13_Risk_Register.md

# Kristal Farms — Risk Register

**Document status:** Partner-facing diligence draft  
**Project focus:** Labrador coast, with Nain as the first target and Labrador coastal communities as the replication logic  
**Version:** v1.0  
**Prepared for:** Partner review and due diligence  
**Distribution:** Partner-facing; financial details and site-specific engineering assumptions to be shared only after validation / NDA where appropriate

---

## 1. Purpose

This risk register identifies the main risks that must be evaluated before advancing Kristal Farms from concept to partner-aligned project development.

The register is organized around the project thesis:

- co-locate compute with cold hydro;
- place modular compute containers near village heat users;
- avoid long high-voltage transmission corridors;
- export compute by fibre, not electricity;
- reuse server heat locally before rejecting it;
- operate tenant containers as black-box compute pads;
- prioritize community heat, consent, governance, and measurable local value.

This document is not a final engineering, legal, environmental, or investment risk assessment. It is a working due-diligence framework for partner conversations.

---

## 2. Risk rating method

### Probability

| Rating | Meaning |
|---|---|
| Low | Unlikely based on current concept, but still requires monitoring |
| Medium | Plausible and should be actively managed |
| High | Likely unless specific mitigation is completed |

### Impact

| Rating | Meaning |
|---|---|
| Low | Manageable within normal project planning |
| Medium | Could delay, resize, or materially change the project |
| High | Could block investment, permitting, consent, construction, or operation |

### Status

| Status | Meaning |
|---|---|
| Open | Risk still needs evidence, partner input, or study |
| Active mitigation | Mitigation path exists and should be advanced |
| Watchlist | Risk is not blocking now but should be tracked |
| Gate item | Must be resolved before a major decision gate |

---

## 3. Summary risk matrix

| # | Risk | Probability | Impact | Status |
|---:|---|---|---|---|
| 1 | Hydro resource and firm capacity risk | Medium | High | Gate item |
| 2 | Site-selection and data validation risk | Medium | High | Gate item |
| 3 | Short MV interconnection and substation risk | Medium | High | Open |
| 4 | Coastal access and sealift logistics risk | Medium | Medium | Active mitigation |
| 5 | Ice, weather, and seasonal construction risk | High | Medium | Active mitigation |
| 6 | Fibre availability and resilience risk | Medium | High | Gate item |
| 7 | Community consent / FPIC risk | Medium | High | Gate item |
| 8 | Governance structure risk | Medium | High | Open |
| 9 | Environmental permitting and aquatic ΔT risk | Medium | High | Gate item |
| 10 | Heat offtake risk | Medium | High | Active mitigation |
| 11 | Winter building compatibility risk | Medium | Medium | Active mitigation |
| 12 | Summer heat sink risk | Medium | Medium | Active mitigation |
| 13 | Cooling source outage or restriction risk | Low–Medium | High | Active mitigation |
| 14 | Tenant demand and occupancy risk | Medium | High | Open |
| 15 | Commercial model and SLA risk | Medium | High | Open |
| 16 | Black-box tenancy and data-boundary risk | Low–Medium | High | Active mitigation |
| 17 | Construction cost and modular supplier risk | Medium | High | Open |
| 18 | Operations, staffing, and maintenance risk | Medium | Medium | Open |
| 19 | Public-benefit proof and dashboard risk | Low–Medium | Medium | Active mitigation |
| 20 | Replication risk beyond Nain | Medium | Medium | Watchlist |

---

## 4. Detailed risk register

## 1. Hydro resource and firm capacity risk

**Risk:**  
The target hydro resource may not provide the dependable capacity, seasonal flow profile, winter output, or development economics required to support both community needs and a compute pad pilot.

**Why it matters:**  
The project depends on local clean power. If the hydro resource is weaker, more seasonal, more expensive, or more environmentally constrained than expected, the project may need to resize the compute load, delay the pilot, or revise the site strategy.

**Probability:** Medium  
**Impact:** High  
**Status:** Gate item  
**Primary owner:** Hydro / utility partner  
**Supporting owners:** Kristal Farms, engineering advisor, community/government partner

**Mitigation:**

- Complete hydro pre-feasibility for Nain / target river.
- Confirm winter firm output, seasonal flow, and expected curtailment.
- Size the first compute pad to verified firm capacity, not theoretical peak output.
- Preserve local community electricity and heat priorities before allocating surplus to compute.
- Avoid dependence on mega-dam or long inland transmission logic.

**Next evidence needed:**

- Hydrology data.
- Preliminary generation profile.
- Firm capacity estimate.
- Interconnection concept.
- Environmental constraints.
- Existing or proposed hydro project documentation.

---

## 2. Site-selection and data validation risk

**Risk:**  
Current site information may contain preliminary, incomplete, outdated, or non-project-specific assumptions.

**Why it matters:**  
Partner documents must distinguish confirmed facts from screening hypotheses. Unvalidated site claims can damage partner confidence and create permitting, community, or investment problems.

**Probability:** Medium  
**Impact:** High  
**Status:** Gate item  
**Primary owner:** Kristal Farms  
**Supporting owners:** hydro partner, mapping/GIS advisor, local partner

**Mitigation:**

- Maintain a single authoritative site inventory.
- Separate candidate, excluded, and deferred sites.
- Label all preliminary figures as “to be validated.”
- Use Nain as the first target only if site data, energy data, fibre data, and community process support it.
- Keep Nunavik, Churchill Falls, inland, and mega-project material as comparison or exclusion logic, not the central project thesis.

**Next evidence needed:**

- Current Labrador coast KML.
- Feature inventory CSV.
- Validation CSV.
- Site ranking logic.
- Source list for each included and excluded feature.

---

## 3. Short MV interconnection and substation risk

**Risk:**  
The intended short medium-voltage connection from the hydro source to the village substation may be more difficult, costly, or delayed than expected.

**Why it matters:**  
The cost advantage depends on avoiding long high-voltage transmission and placing containers near heat users. If the short MV concept is not feasible, the project architecture must be revised.

**Probability:** Medium  
**Impact:** High  
**Status:** Open  
**Primary owner:** Utility / electrical engineering partner  
**Supporting owners:** Kristal Farms, hydro operator, local authority

**Mitigation:**

- Confirm MV route options.
- Confirm voltage class, right-of-way, substation location, protection, grounding, and metering needs.
- Prioritize a village-edge or port-area energy center that keeps heat loops short.
- Avoid architecture that places compute at the dam if heat cannot be reused locally.

**Next evidence needed:**

- Conceptual one-line diagram.
- Route map.
- Interconnection study.
- Substation concept.
- Preliminary cost range.
- Constructability and permitting review.

---

## 4. Coastal access and sealift logistics risk

**Risk:**  
Equipment delivery, container handling, port access, and seasonal sealift windows may constrain deployment.

**Why it matters:**  
The model depends on modular marine logistics. Missed shipping windows, insufficient port handling capability, or weather disruption could delay construction and increase cost.

**Probability:** Medium  
**Impact:** Medium  
**Status:** Active mitigation  
**Primary owner:** Logistics / marine partner  
**Supporting owners:** modular data center supplier, local authority, Kristal Farms

**Mitigation:**

- Design around standard 20-foot or 40-foot modular containers.
- Use port-adjacent or village-edge pads where possible.
- Sequence construction and deliveries around realistic seasonal windows.
- Pre-stage critical spares, pumps, valves, controls, fibre materials, and heat loop components.
- Avoid overpromising year-round marine access.

**Next evidence needed:**

- Port capability assessment.
- Barge / sealift calendar.
- Lift and transport plan.
- Laydown area assessment.
- Winter storage plan.
- Local contractor capacity review.

---

## 5. Ice, weather, and seasonal construction risk

**Risk:**  
Ice, storms, freeze-thaw cycles, winter darkness, and short construction seasons may affect schedule, cost, and maintainability.

**Why it matters:**  
Labrador coastal conditions require conservative planning. Construction and maintenance windows may be narrower than in southern data center markets.

**Probability:** High  
**Impact:** Medium  
**Status:** Active mitigation  
**Primary owner:** EPC / construction partner  
**Supporting owners:** local partner, logistics partner, operations lead

**Mitigation:**

- Use prefabricated modules and skids to reduce on-site work.
- Design all external piping, valves, and controls for freeze protection.
- Use insulated and heat-traced critical components where required.
- Build maintenance access into pad layout.
- Schedule commissioning around weather windows.

**Next evidence needed:**

- Climate design basis.
- Ice and snow load assumptions.
- Seasonal construction plan.
- Freeze protection design.
- Emergency maintenance access plan.

---

## 6. Fibre availability and resilience risk

**Risk:**  
The project may not have sufficient, reliable, redundant, or commercially acceptable fibre connectivity for compute tenants.

**Why it matters:**  
Kristal Farms exports compute results by fibre, not electricity. Without reliable connectivity, compute tenancy, SLA credibility, and partner economics weaken.

**Probability:** Medium  
**Impact:** High  
**Status:** Gate item  
**Primary owner:** Telecom / fibre partner  
**Supporting owners:** NOC operator, compute tenant, Kristal Farms

**Mitigation:**

- Confirm fibre path, capacity, latency, availability, and upgrade plan.
- Design A/B pad links where possible.
- Establish NOC monitoring and incident response.
- Define which workloads are acceptable under available latency and reliability conditions.
- Prioritize batch, resilient, or delay-tolerant compute in early phases if needed.
- Keep exact SLA values out of early partner docs until telecom validation is complete.

**Next evidence needed:**

- Fibre route and ownership.
- Capacity quote.
- Latency estimate.
- Availability history.
- Redundancy options.
- Repair and splicing plan.
- NOC architecture.

---

## 7. Community consent / FPIC risk

**Risk:**  
The project may not secure or maintain community consent, including FPIC where applicable.

**Why it matters:**  
Community legitimacy is not optional. Without consent and benefit alignment, the project should not proceed.

**Probability:** Medium  
**Impact:** High  
**Status:** Gate item  
**Primary owner:** Community/government partner  
**Supporting owners:** Kristal Farms, legal advisor, local leadership

**Mitigation:**

- Start with information and listening before site commitments.
- Use a common FPIC process with site-specific timelines.
- Clearly distinguish confirmed principles from open design items.
- Ensure heat, jobs, training, and benefits are negotiated locally.
- Avoid presenting governance terms as finalized before community decisions are made.

**Next evidence needed:**

- Community engagement plan.
- FPIC process outline.
- Local decision timeline.
- Benefit priorities.
- Record of concerns and responses.
- Draft Community Benefits Agreement / IBA framework.

---

## 8. Governance structure risk

**Risk:**  
Project councils, heat committees, environment committees, Kristals councils, escalation paths, and decision rights may remain undefined too long.

**Why it matters:**  
Unclear governance can create disputes between the host, tenants, community, utility, government, and heat users.

**Probability:** Medium  
**Impact:** High  
**Status:** Open  
**Primary owner:** Governance / legal lead  
**Supporting owners:** community partner, Kristal Farms, utility partner, tenants

**Mitigation:**

- Separate governance into confirmed principles, open design items, and decisions required.
- Define committee composition, nomination rights, scope, decision authority, advisory authority, and escalation.
- Define heat allocation priorities before operation.
- Define publication authority for public dashboards.
- Define grievance, mediation, and arbitration process.

**Next evidence needed:**

- Draft governance charter.
- Draft committee terms of reference.
- Decision-rights matrix.
- Grievance process.
- Dispute escalation timeline.
- Community review comments.

---

## 9. Environmental permitting and aquatic ΔT risk

**Risk:**  
Heat rejection, water intake/outfall, construction, or hydro integration may trigger environmental permitting issues or ΔT compliance constraints.

**Why it matters:**  
The system depends on non-contact cooling and controlled heat rejection. Any environmental harm, perceived harm, or permit breach can stop operations.

**Probability:** Medium  
**Impact:** High  
**Status:** Gate item  
**Primary owner:** Environmental / permitting lead  
**Supporting owners:** hydro partner, heat system engineer, Environment Committee

**Mitigation:**

- Use two sealed circuits.
- Use plate heat exchangers for all environmental heat exchange.
- Keep river/bay water separate from IT and building loops.
- Use dry coolers as backup.
- Monitor ΔT, flow, temperatures, and alarms continuously.
- Throttle IT load if ΔT limits are approached.
- Publish environmental metrics in the dashboard where appropriate.

**Next evidence needed:**

- Environmental baseline.
- Intake/outfall concept.
- ΔT threshold from regulator.
- Fish and aquatic habitat review.
- Permitting pathway.
- Monitoring plan.
- Incident response plan.

---

## 10. Heat offtake risk

**Risk:**  
The village may not have enough connected heat demand to absorb the available server heat at the time and scale it is produced.

**Why it matters:**  
Heat reuse is a core differentiator. If useful heat is too low, the project loses community value and weakens its environmental case.

**Probability:** Medium  
**Impact:** High  
**Status:** Active mitigation  
**Primary owner:** Heat system partner  
**Supporting owners:** community partner, building owners, Kristal Farms

**Mitigation:**

- Start with public buildings: clinic, school, town hall, and other high-priority loads.
- Add nearby housing only after public loads are validated.
- Add greenhouse as shoulder-season and summer sink.
- Include stratified thermal storage.
- Phase compute pads only when heat sinks can absorb expected output.
- Track useful heat delivered and HUF.

**Next evidence needed:**

- Building heat load inventory.
- Public-building priority list.
- Pipe route.
- Substation design.
- Greenhouse feasibility.
- Thermal storage sizing.
- Seasonal HUF estimate.

---

## 11. Winter building compatibility risk

**Risk:**  
Existing buildings may need higher supply temperatures than server heat can provide directly.

**Why it matters:**  
If public buildings or homes rely on legacy radiators requiring 65–75°C, the project may need boosters, emitter upgrades, or a narrower heat-service scope.

**Probability:** Medium  
**Impact:** Medium  
**Status:** Active mitigation  
**Primary owner:** Mechanical engineering partner  
**Supporting owners:** building owners, heat operator, community partner

**Mitigation:**

- Survey building heating systems.
- Identify low-temperature-ready buildings first.
- Install central heat-pump booster where needed.
- Use fan-coils, oversized emitters, or targeted upgrades for problem buildings.
- Test performance on design-cold days before full service commitment.

**Next evidence needed:**

- Building audits.
- Radiator / emitter inventory.
- DHW requirements.
- Booster sizing.
- Building substation design.
- Commissioning test plan.

---

## 12. Summer heat sink risk

**Risk:**  
During summer, the greenhouse and storage may not absorb enough server heat, forcing more heat rejection or compute curtailment.

**Why it matters:**  
Summer sink limitations can reduce compute utilization or lower heat utilization metrics.

**Probability:** Medium  
**Impact:** Medium  
**Status:** Active mitigation  
**Primary owner:** Heat system partner  
**Supporting owners:** greenhouse operator, compute operator, Environment Committee

**Mitigation:**

- Use greenhouse as primary warm-season sink.
- Add storage to buffer daily heat mismatch.
- Define operational triggers for compute scheduling or throttling.
- Increase greenhouse area only when operationally and commercially justified.
- Treat rejection as last resort after reuse and storage.

**Next evidence needed:**

- Greenhouse thermal model.
- Summer heat balance.
- Tank sizing.
- Ventilation and greenhouse operating plan.
- Compute scheduling policy.
- Seasonal HUF target.

---

## 13. Cooling source outage or restriction risk

**Risk:**  
The primary cold source, such as seawater/bay water at the port, may be unavailable, restricted, fouled, iced, or temporarily unsuitable.

**Why it matters:**  
Compute pads require reliable cooling. A cooling constraint can force load reduction or shutdown.

**Probability:** Low–Medium  
**Impact:** High  
**Status:** Active mitigation  
**Primary owner:** Cooling system operator  
**Supporting owners:** environmental lead, compute tenant, NOC/operator

**Mitigation:**

- Use non-contact titanium plate heat exchangers for bay/seawater exchange.
- Do not depend on small rivers as the main sink.
- Include dry coolers as backup and shoulder-season support.
- Include alarms for flow, temperature, pressure, and ΔT.
- Define curtailment process for non-critical workloads.
- Maintain spare pumps, controls, and HX components.

**Next evidence needed:**

- Cold-source assessment.
- Intake/outfall design.
- Biofouling / corrosion review.
- Dry cooler sizing.
- Maintenance plan.
- Cooling failure runbook.

---

## 14. Tenant demand and occupancy risk

**Risk:**  
Compute tenants may not commit to enough capacity, duration, or lease terms to support the pilot economics.

**Why it matters:**  
Pad occupancy and lease revenue are essential to the commercial model. Underutilized pads still create fixed infrastructure costs.

**Probability:** Medium  
**Impact:** High  
**Status:** Open  
**Primary owner:** Commercial lead  
**Supporting owners:** Kristal Farms, infrastructure investor, compute partners

**Mitigation:**

- Prioritize tenants that value renewable power, heat reuse, black-box tenancy, and modular deployment.
- Offer phased pad leases instead of overbuilding.
- Match first pad size to contracted demand.
- Avoid speculative capacity expansion before tenant and heat offtake validation.
- Separate compute tenancy from optional Kristals public-interest compute.

**Next evidence needed:**

- Tenant pipeline.
- Letters of interest.
- Capacity requirements.
- SLA requirements.
- Lease term preferences.
- Tenant eligibility criteria.

---

## 15. Commercial model and SLA risk

**Risk:**  
Partner expectations around pricing, service guarantees, heat value, metering, curtailment, and responsibilities may not align.

**Why it matters:**  
A partner may be contributing capital, land, power, fibre, equipment, tenancy, or community support. Unclear roles can delay or derail negotiations.

**Probability:** Medium  
**Impact:** High  
**Status:** Open  
**Primary owner:** Commercial/legal lead  
**Supporting owners:** Kristal Farms, utility partner, investor, compute tenant, community partner

**Mitigation:**

- Define partner types and specific asks early.
- Keep sensitive economics under NDA.
- Define metered service boundaries: power, cooling, heat export, fibre, pad access.
- Define reversibility and end-of-lease responsibilities.
- Avoid multiple SLA tiers until the operating model requires them.
- Document best-effort surplus compute separately from guaranteed pad service.

**Next evidence needed:**

- Draft term sheet.
- SLA outline.
- Metering plan.
- Heat pricing / cost recovery concept.
- Insurance requirements.
- End-of-lease removal plan.

---

## 16. Black-box tenancy and data-boundary risk

**Risk:**  
Tenants may not trust host boundaries, or hosts/community partners may expect visibility that is inconsistent with black-box tenancy.

**Why it matters:**  
The project’s compute model requires tenant privacy. The host must monitor physical infrastructure without accessing tenant data, logs, model content, or packet payloads.

**Probability:** Low–Medium  
**Impact:** High  
**Status:** Active mitigation  
**Primary owner:** Security / tenancy lead  
**Supporting owners:** NOC operator, tenant, legal advisor

**Mitigation:**

- Define host-visible metrics clearly: energy, cooling ΔT/flow, uptime, aggregate bandwidth, and technical alarms.
- Explicitly exclude tenant logs, application data, model content, internal telemetry, and packet payload inspection.
- Offer hardware attestation as optional depending on tenant needs.
- Separate community / Kristals activity from tenant black-box workloads.
- Use anonymized and aggregated reporting for public dashboards.

**Next evidence needed:**

- Data boundary schedule.
- Security architecture.
- NOC access control policy.
- Tenant privacy clause.
- Optional attestation clause.
- Incident notification process.

---

## 17. Construction cost and modular supplier risk

**Risk:**  
Container modules, pads, cooling skids, heat loop materials, fibre components, and remote construction may cost more or take longer than expected.

**Why it matters:**  
Remote Labrador coastal work can face supplier lead times, shipping constraints, specialized labor constraints, and material escalation.

**Probability:** Medium  
**Impact:** High  
**Status:** Open  
**Primary owner:** EPC / procurement lead  
**Supporting owners:** modular data center supplier, logistics partner, investor

**Mitigation:**

- Use standard modular interfaces.
- Avoid custom designs unless required for cold climate or heat capture.
- Prequalify suppliers for container, cooling, power, controls, and fibre components.
- Include contingency for sealift, weather delays, and spares.
- Start with a pilot pad before expansion pads.

**Next evidence needed:**

- Supplier shortlist.
- Budgetary quotes.
- Lead time schedule.
- Shipping and installation cost.
- Spare parts strategy.
- Construction risk allowance.

---

## 18. Operations, staffing, and maintenance risk

**Risk:**  
The project may not have enough trained local operators, technicians, NOC support, or maintenance capacity for reliable operations.

**Why it matters:**  
The model depends on high uptime, safe heat delivery, and community trust. Local capability is also part of the community-benefit thesis.

**Probability:** Medium  
**Impact:** Medium  
**Status:** Open  
**Primary owner:** Operations lead  
**Supporting owners:** community partner, training provider, vendors, NOC operator

**Mitigation:**

- Define local roles early.
- Build a training program for pad operations, heat loop monitoring, safety, and basic fibre/NOC support.
- Use remote monitoring for specialist oversight.
- Keep a local spares inventory.
- Use vendor service agreements for critical systems.
- Track local jobs and training hours publicly.

**Next evidence needed:**

- Staffing model.
- Training plan.
- O&M budget.
- Vendor support contracts.
- Spare parts list.
- Safety procedures.

---

## 19. Public-benefit proof and dashboard risk

**Risk:**  
The project may fail to demonstrate community value in a simple, trusted, and auditable way.

**Why it matters:**  
Kristal Farms depends on visible benefits: heat delivered, diesel avoided, local jobs, training, fibre improvements, uptime, and greenhouse output. If these are not measured and reported, trust may decline.

**Probability:** Low–Medium  
**Impact:** Medium  
**Status:** Active mitigation  
**Primary owner:** Metrics / reporting lead  
**Supporting owners:** Project Council, Heat Committee, Environment Committee, operator

**Mitigation:**

- Use a stable public scorecard.
- Publish monthly dashboard updates.
- Hold quarterly reviews with governance bodies.
- Publish annual reports.
- Keep metric definitions centralized in the Metrics Dashboard and Audit Framework.
- Use independent audit where appropriate.

**Next evidence needed:**

- Final metric definitions.
- Dashboard mockup.
- Data ownership plan.
- Review cadence.
- Audit plan.
- Public reporting format.

---

## 20. Replication risk beyond Nain

**Risk:**  
A model that works in Nain may not replicate cleanly in Hopedale, Makkovik, Postville, Rigolet, or other Labrador coastal communities.

**Why it matters:**  
The expansion logic is coastal replication, but each community may differ in hydro resource, port access, fibre path, heat demand, governance, permitting, and local priorities.

**Probability:** Medium  
**Impact:** Medium  
**Status:** Watchlist  
**Primary owner:** Kristal Farms strategy lead  
**Supporting owners:** local partners, hydro/fibre partners, community/government partner

**Mitigation:**

- Treat Nain as first target and learning site, not proof of universal fit.
- Build a replication scorecard.
- Separate standardized architecture from site-specific decisions.
- Do not commit to expansion communities before local screening and consent.
- Capture lessons from pilot pad, heat loop, governance, and fibre validation.

**Next evidence needed:**

- Community-by-community screening matrix.
- Hydro/fibre/port/heat demand comparison.
- Local engagement roadmap.
- Replication assumptions log.
- Expansion decision criteria.

---

## 5. Decision gates tied to risk closure

| Gate | Decision | Minimum risk evidence required |
|---|---|---|
| Gate A | Partner interest | Partner roles, preferred structure, preliminary risk allocation |
| Gate B | Site data validated | Hydro data, map inventory, port/fibre/heat demand screening |
| Gate C | Community process initiated | FPIC path, engagement plan, governance principles |
| Gate D | Pilot economics approved | Tenant interest, capex range, heat offtake plan, SLA outline |
| Gate E | Construction readiness | Permits, interconnection, fibre, logistics, supplier quotes, O&M plan |
| Gate F | Operational launch | Commissioned heat loop, pad interfaces, NOC, dashboard, incident runbooks |

---

## 6. Risks that should not be hidden

The following issues should be stated clearly in partner conversations:

1. Hydro and fibre data must be validated before final sizing.
2. Nain is the first target, not a guaranteed final site until due diligence is complete.
3. Community consent and FPIC are gating requirements.
4. Governance structure is not fully finalized and should be co-designed.
5. Financial projections should not be presented as validated until partner data is available.
6. Heat reuse is central, but seasonal heat offtake must be engineered carefully.
7. The model should avoid inland mega-project logic and long HV transmission assumptions.
8. Black-box tenancy limits what the host can see, even when the host is responsible for physical infrastructure.

---

## 7. Immediate due-diligence workplan

### Technical

- Hydro pre-feasibility.
- MV interconnection concept.
- Fibre route and capacity confirmation.
- Port and sealift assessment.
- Cold-source and ΔT assessment.
- Heat-load inventory for public buildings and nearby homes.
- Pilot pad concept design.

### Community and governance

- Initial engagement plan.
- FPIC process map.
- Community-benefit priorities.
- Draft governance model.
- Grievance and escalation process.
- Public dashboard concept.

### Commercial

- Partner ask and role matrix.
- Tenant pipeline.
- SLA boundary.
- Preliminary capex and opex categories.
- Risk allocation matrix.
- NDA data room plan.

---

## 8. Risk ownership map

| Risk area | Primary owner |
|---|---|
| Hydro resource | Hydro / utility partner |
| Site selection | Kristal Farms + engineering advisor |
| MV interconnection | Utility / electrical partner |
| Logistics | Marine / logistics partner |
| Fibre | Telecom / fibre partner |
| FPIC and community consent | Community / government partner |
| Governance | Governance / legal lead |
| Environmental permitting | Environmental lead |
| Heat system | Heat system partner |
| Tenant demand | Commercial lead |
| SLA and lease model | Commercial / legal lead |
| Black-box boundary | Security / tenancy lead |
| Construction | EPC / procurement lead |
| Operations | Site operator |
| Dashboard and audit | Metrics / reporting lead |

---

## 9. Open questions for partners

1. Which partner is expected to own hydro development or hydro offtake?
2. Which partner owns the MV connection and village substation?
3. Who owns and operates the compute pad yard?
4. Who owns the heat loop and building substations?
5. Who owns the fibre/NOC architecture?
6. Which public buildings are first-priority heat users?
7. What is the local process for consent, review, and benefit agreement approval?
8. What data can be shared before NDA, and what belongs in the data room?
9. What tenant workloads are acceptable for the first pilot pad?
10. Which risks must be closed before a partner can issue a letter of intent?

---

## 10. Source basis

This risk register is based on the current Kristal Farms source corpus, especially:

- Kristal Farms — Heat Recycling Plan.
- Kristal Farms Internal Reference Document.
- Kristal Farms — Cost Advantage & Strategic Rationale.
- Documentation Kristal Farms.
- Potentiel hydroélectrique isolé au Nunavik et au Labrador.
- Kristal Farms article-style synthesis PDF.
- Vendor and modular data center background files.

The risk register should be updated after each major partner conversation, technical study, community meeting, and site-data validation step.

---
