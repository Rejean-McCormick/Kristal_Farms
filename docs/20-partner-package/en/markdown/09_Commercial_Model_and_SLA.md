# 09_Commercial_Model_and_SLA

**Kristal Farms — Commercial Model and SLA**  
**Partner-facing draft**  
**Project focus:** Labrador coast package, with Nain as first target and Labrador coastal replication as the expansion logic  
**Distribution:** Partner-facing, non-NDA version. Detailed pricing, financial model, tenant economics, project-level returns, and confidential partner terms should remain in the data room or NDA package.

---

## 1. Purpose

This document explains the commercial model for Kristal Farms and the service-level framework that would support partner, tenant, community, and infrastructure agreements.

Kristal Farms is designed as a **village-scale hydro / compute / heat platform**. The project uses coastal hydro potential to power modular compute pads, places the pads close to community heat users, exports compute results by fibre, and turns server heat into local value through public-building heating, domestic hot water support, greenhouse heat, and thermal storage.

The commercial thesis is simple:

> Kristal Farms monetizes compute infrastructure while turning the physical by-products of compute — heat, connectivity, and power reliability — into local community value.

This document does not present a final financial model. It defines the commercial structure, revenue categories, cost categories, SLA principles, metering logic, tenant eligibility, and end-of-lease reversibility needed for partner due diligence.

---

## 2. Commercial model summary

Kristal Farms should be presented as an **infrastructure platform**, not as an AI software company and not as a speculative token or data business.

The project provides:

1. **Prepared compute pads** with power, cooling, heat-export interface, fibre, monitoring, security, and access control.
2. **Hydro-backed power service** using local renewable power where available and validated.
3. **Cooling and heat-recovery service** based on liquid cooling, plate heat exchangers, and the reuse → store → reject hierarchy.
4. **Connectivity service** through fibre and a site Network Operations Center.
5. **Community heat service** for public buildings, homes, and greenhouse uses.
6. **Optional Kristals / knowledge layer**, only where surplus compute, governance approval, and privacy boundaries allow.

The preferred commercial posture is:

> Lease standardized infrastructure capacity to tenants, preserve tenant data isolation, retain host control over physical interfaces, and allocate community benefits through transparent governance agreements.

---

## 3. Partner and counterparty categories

Different partners may participate in different parts of the commercial structure. Kristal Farms should not approach every partner with the same ask.

| Partner type | Possible role | Commercial interest | Key agreement type |
|---|---|---|---|
| Hydro / utility partner | Power access, grid interface, substation support, operating constraints | New local demand, better use of hydro resource, reduced diesel dependence | Power services agreement, interconnection agreement, operating protocol |
| Infrastructure investor | Capital for pads, heat loop, fibre, substation, logistics | Long-term contracted infrastructure cash flow | Project company investment, debt facility, infrastructure JV |
| Compute tenant | Leases pad capacity or brings a container | Secure, renewable, lower-overhead compute environment | Pad lease, SLA, black-box tenancy agreement |
| Modular data center supplier | Provides container, cooling, electrical, monitoring, deployment support | Equipment sale, service contract, maintenance | EPC/supply agreement, O&M agreement, warranty package |
| Fibre / telecom partner | Trunk fibre, diversity, NOC equipment, network operations | Anchor customer, regional connectivity expansion | Fibre service agreement, IRU, capacity lease, NOC service agreement |
| Community / government partner | Consent process, benefits, heat allocation, permitting support | Local heat, jobs, training, infrastructure, community revenue | Community Benefits Agreement / IBA, FPIC process agreement, governance charter |

---

## 4. Revenue streams

The revenue model should be described in categories, not premature projections. Any dollar values, IRR targets, tenant pricing, or long-term revenue forecasts should be moved to an NDA-only financial model.

### 4.1 Compute pad leases

The primary revenue stream is the lease of standardized compute pads.

A compute pad may include:

- physical pad space;
- electrical handoff and metering;
- cooling interface;
- heat-export interface;
- dual fibre handoff where available;
- physical access control;
- monitoring of host-side infrastructure metrics;
- site security and operating procedures;
- commissioning and decommissioning process.

Possible lease formats:

| Lease format | Description | Best use |
|---|---|---|
| Tenant-owned container on Kristal pad | Tenant provides container and internal IT equipment; Kristal Farms provides physical interfaces | Sophisticated tenant with its own hardware/security stack |
| Kristal-standard container leased to tenant | Kristal Farms or supplier provides a compliant container; tenant leases capacity or installs equipment | Tenants needing faster deployment |
| Dedicated pad block | Several pads reserved for one tenant or partner | Larger compute tenant, government, research consortium |
| Pilot pad | Shorter pilot term with fixed capacity ceiling | First deployment, technical validation, community proof-of-value |

The partner-facing package should emphasize **pad leasing** rather than selling raw electricity. The core product is a prepared, serviced, reversible compute location.

### 4.2 Power and cooling services

Kristal Farms provides power and cooling as part of the pad service. These may be priced as separate line items or embedded in the lease.

Potential commercial structures:

- base pad lease plus pass-through metered power;
- capacity reservation fee plus energy usage charge;
- bundled power/cooling/fibre service fee;
- separate charge for high-temperature heat-recovery compatibility where specialized interfaces are required;
- commissioning fee for tenant-specific integration.

The commercial model should reserve enough local energy margin for community needs before compute expansion. Compute should scale in phases as hydro availability, heat sinks, fibre, and community consent are validated.

### 4.3 Heat value

Heat value is a central differentiator but should not be over-monetized in early partner documents. The first commercial position should be:

> Heat reuse creates community value, political durability, diesel displacement, and ESG value. Direct cash revenue from heat may be secondary during early phases.

Heat value may appear as:

- avoided diesel heating cost for public buildings;
- avoided fuel transport exposure;
- community heating credit;
- public-building energy savings;
- greenhouse operating support;
- local food-security benefit;
- reportable ESG benefit for partners;
- community benefit contribution under a CBA or IBA.

Possible heat commercial models:

| Model | Description | Comment |
|---|---|---|
| Community benefit allocation | Heat delivered to priority public buildings or homes as part of project benefits | Best early model; easy to explain |
| Heat service tariff | Buildings pay a reduced heat tariff below diesel-equivalent cost | Requires metering, tariff approval, customer agreements |
| Greenhouse heat allocation | Greenhouse receives heat under operating agreement | Useful as summer/shoulder sink |
| ESG credit / impact reporting | Heat delivered and diesel avoided are reported to partners | Do not claim saleable credits unless legally verified |

Early documents should avoid claiming carbon credits, guaranteed savings, or fixed heat revenue until verified by counsel, regulators, and the community.

### 4.4 Fibre and connectivity services

Fibre is commercially important because Kristal Farms exports compute results rather than electricity.

Connectivity may create value through:

- tenant network service charges;
- dedicated wavelength or capacity agreements;
- community connectivity upgrades;
- shared NOC services;
- anchor demand for regional fibre expansion;
- optional low-latency service class for approved workloads.

The commercial model should distinguish:

- **tenant fibre service**, which supports compute operations;
- **community fibre benefit**, which may support clinic, school, public services, or local connectivity;
- **backbone/trunk service**, which depends on the telecom/fibre partner and must be confirmed through due diligence.

### 4.5 Optional Kristals / knowledge layer

Kristals should be treated as an optional layer, not the primary commercial engine of the first Labrador coast package.

Potential value streams include:

- use of surplus or best-effort compute for public-interest knowledge work;
- enterprise support for adapting public Kristals to private workflows;
- training, documentation, and knowledge-system services;
- community education and research partnerships;
- structured knowledge outputs where governance approves scope and data sources.

Important boundary:

> Kristals must never use tenant private data, tenant logs, tenant model content, or tenant workload outputs unless the tenant has explicitly authorized that use in writing.

For the first partner package, Kristals should be described as **optional upside** and a community/public-interest layer, not as a core revenue dependency.

---

## 5. Cost structure

The cost structure should be presented as a set of categories for due diligence. Detailed CAPEX/OPEX numbers should remain outside the non-NDA partner brief until validated.

### 5.1 Hydro connection and electrical system

Likely cost categories:

- hydro resource validation and power studies;
- interconnection engineering;
- short medium-voltage feeder from hydro source to village substation;
- village-edge or port substation;
- pad feeders and protective devices;
- metering at hydro output, substation, and pad level;
- power quality monitoring;
- grounding, protection, lockout/tagout systems;
- backup/emergency integration with existing diesel for critical loads where applicable.

Commercial objective:

> Avoid long high-voltage transmission buildout and instead use a shorter, auditable, village-scale electrical interface.

### 5.2 Compute pad yard

Likely cost categories:

- land preparation at port or village edge;
- pad foundations or modular supports;
- fencing, lighting, access control, cameras;
- crane/lift coordination and container placement;
- fire safety systems and emergency access;
- internal site roads or short-haul logistics;
- snow, ice, and drainage management;
- pad-specific electrical, cooling, and fibre interfaces.

The pad yard should be designed for reversibility. It should be possible to remove containers and restore the pad area with limited lasting impact.

### 5.3 Cooling and heat-recovery system

Likely cost categories:

- IT cooling interface;
- plate heat exchangers;
- titanium heat exchanger for seawater/bay interface where required;
- pumps, valves, sensors, and controls;
- dry cooler backup;
- pre-insulated heat-loop pipes;
- building substations with heat meters;
- optional heat pump booster for legacy radiator systems;
- thermal storage tanks;
- greenhouse heat interface;
- commissioning, pressure testing, and environmental ΔT monitoring.

Commercial objective:

> Turn server heat into useful community heat before storage or rejection.

### 5.4 Fibre and NOC

Likely cost categories:

- fibre route studies and rights-of-way;
- trunk fibre connection to regional hub;
- diverse path or ring design where feasible;
- NOC shelter or room;
- DWDM or equivalent transport equipment;
- ODF, patching, switches, routers, firewalls;
- A/B power for NOC equipment;
- tenant separation and monitoring tools;
- network operations staff or managed service agreement.

Fibre costs should be treated as a major due-diligence item. The business model depends on reliable data export.

### 5.5 Port logistics and sealift

Likely cost categories:

- marine freight;
- seasonal shipping window planning;
- port handling;
- crane/lift operations;
- local short-haul transport;
- storage and staging;
- winterization and weather protection;
- spare parts inventory strategy.

The commercial model should not overpromise year-round marine access. Logistics assumptions must be validated site by site.

### 5.6 Operations and maintenance

Likely cost categories:

- site operator team;
- NOC monitoring;
- electrical maintenance;
- cooling/heat-loop maintenance;
- fibre maintenance coordination;
- snow/ice/site access operations;
- security;
- compliance reporting;
- environmental monitoring;
- community dashboard preparation;
- training and local workforce development;
- insurance, legal, audit, and administration.

---

## 6. SLA framework

The SLA should be simple in the first package. Kristal Farms should not offer multiple service tiers at this stage.

### 6.1 SLA principle

The proposed initial SLA posture is:

> One guaranteed service level per tenant up to that tenant’s contractual consumption ceiling. Surplus or opportunistic compute remains best-effort unless separately contracted.

This avoids overcomplicating the first partner offer and keeps the project focused on reliable physical infrastructure.

### 6.2 SLA scope

The SLA should cover the services the host actually controls:

| SLA area | Host commitment | Notes |
|---|---|---|
| Power handoff | Provide contracted power capacity up to agreed ceiling, subject to site limits and force majeure | Exact availability target to be defined after electrical studies |
| Cooling interface | Provide cooling/heat-export interface within agreed operating envelope | Tenant must provide compatible internal cooling system |
| Heat export | Require cooperation with heat-recovery interface where technically feasible | No guaranteed heat quota in early version unless later agreed |
| Fibre handoff | Provide site-side fibre handoff and monitored link status | Exact latency/availability targets belong in Connectivity document |
| Physical access | Controlled access, maintenance windows, emergency procedure | Tenant access rules defined in lease |
| Monitoring | Host-side physical metrics only | No tenant data access |
| Incident response | Notification, RCA, corrective action process | Privacy and environmental incidents require defined protocols |

### 6.3 What is outside the host SLA

The host should not accept responsibility for tenant-controlled systems.

Out of host SLA:

- tenant servers;
- tenant operating systems;
- tenant applications;
- tenant AI models;
- tenant data pipelines;
- tenant cybersecurity inside the container;
- tenant-side cooling failures after the host handoff;
- tenant network configuration after host demarcation;
- workload performance or model-training completion time;
- business interruption caused by tenant hardware/software failure.

### 6.4 Planned maintenance

The SLA should include planned maintenance procedures for:

- electrical work;
- cooling and heat-loop service;
- fibre patching or network changes;
- winterization inspections;
- environmental monitoring calibration;
- safety tests and emergency drills.

Recommended commercial position:

- advance notice for planned maintenance;
- maintenance windows scheduled for lowest practical tenant and community impact;
- emergency work allowed without full notice where needed to protect safety, public heat, environmental compliance, or equipment integrity;
- maintenance records logged and made available to affected partners where appropriate.

### 6.5 Incident handling

Incident categories should include:

- power event;
- cooling event;
- heat-loop event;
- fibre/network event;
- environmental ΔT event;
- physical security event;
- privacy or black-box boundary concern;
- tenant-caused event;
- force majeure / weather / logistics event.

For major incidents, the operating protocol should include:

1. initial notification to affected parties;
2. operational containment;
3. root-cause analysis;
4. corrective action plan;
5. reporting to relevant committees, regulators, or tenants where required;
6. public dashboard note where appropriate and legally permitted.

---

## 7. Metering and reporting

Metering is central to commercial trust. Every major interface should be measured.

### 7.1 Required meters and monitored interfaces

| Interface | Meter / metric | Commercial use |
|---|---|---|
| Hydro output | kW, kWh, availability | Energy accounting, power capacity planning |
| Village substation | kW, kWh, power quality | Losses, reliability, operating limits |
| Each compute pad | kW, kWh, peak demand | Tenant billing, capacity ceiling, SLA verification |
| Cooling loop | flow, supply/return temperature, ΔT | Cooling service verification, heat accounting |
| Heat delivered | MWh_th by sink | Community benefit reporting, heat allocation |
| Fibre links | uptime, bandwidth utilization, errors, latency p95 where available | SLA and network performance reporting |
| Pad uptime | host-side availability | Lease performance and reliability tracking |
| Diesel avoided | litres, MWh equivalent, CO₂e estimate where validated | Community and ESG reporting |

### 7.2 Black-box monitoring boundary

The host may monitor physical infrastructure metrics, including:

- energy consumed;
- instantaneous power;
- cooling loop flow;
- cooling ΔT;
- heat exported;
- pad heartbeat / availability;
- link status;
- aggregate bandwidth volume;
- technical alarms.

The host must not access:

- tenant application logs;
- tenant datasets;
- tenant model content;
- tenant prompts or outputs;
- packet payloads;
- sensitive network metadata beyond aggregate operational metrics;
- internal tenant operating systems or software.

### 7.3 Reporting cadence

Recommended reporting model:

| Report | Audience | Cadence | Content |
|---|---|---|---|
| Tenant operations report | Tenant | Monthly or contract-defined | Power, cooling, uptime, fibre status, incidents |
| Community dashboard | Community / governance bodies | Monthly | Heat delivered, diesel avoided, uptime, jobs/training, greenhouse indicators |
| Partner performance review | Investors / partners / project council | Quarterly | SLA trends, pad occupancy, risks, decision items |
| Annual audit pack | Partners, community, auditors | Annual | Metering review, environmental compliance, benefits, corrective actions |

Long-term physical logs may be retained for history and statistics, subject to the final privacy, legal, and data-retention policy. Tenant data remains outside host logs.

---

## 8. Tenant eligibility

Tenant eligibility protects the community, host, utility partner, and other tenants.

### 8.1 Eligible tenant categories

Potential eligible tenants:

- AI research labs;
- universities and public research institutions;
- cloud or compute operators;
- enterprise AI teams;
- Indigenous/community-approved technology partners;
- government or public-interest compute users;
- scientific computing users;
- approved batch AI training or inference workloads;
- approved Kristals-related surplus compute programs.

### 8.2 Screening criteria

A tenant should be screened for:

- legal identity and beneficial ownership;
- sanctions and export-control compliance;
- cybersecurity posture;
- physical equipment compatibility;
- power and cooling requirements;
- heat-recovery compatibility;
- fibre and latency needs;
- environmental and noise profile;
- ability to comply with site access rules;
- ability to comply with black-box and community protocols;
- reputational or geopolitical risk;
- alignment with community and governance requirements.

### 8.3 Excluded or restricted uses

The project should reserve the right to exclude tenants or workloads that create unacceptable legal, environmental, security, or community risk.

Potentially restricted categories:

- unlawful activity;
- sanctioned entities;
- workloads prohibited by Canadian law or applicable export controls;
- activity that would require host inspection of tenant data;
- activity that threatens community safety or consent;
- workloads that cannot meet cooling/heat-interface requirements;
- workloads that would materially compromise local power margin or public heat commitments;
- activity inconsistent with project governance or community benefit commitments.

### 8.4 Tenant transfer

Lease transfer may be allowed only with prior approval.

Conditions should include:

- new tenant due diligence;
- compliance with security and eligibility standards;
- assumption of all lease obligations;
- continuity of heat connection where feasible;
- no interruption to site safety or public heat commitments;
- operator approval and, where required, project council or community governance review.

---

## 9. Contract structure

A complete commercial package may include several linked agreements.

| Agreement | Parties | Purpose |
|---|---|---|
| Pad lease agreement | Kristal Farms / tenant | Rights and obligations for pad use |
| SLA schedule | Kristal Farms / tenant | Power, cooling, fibre, access, maintenance, incident response |
| Power service schedule | Kristal Farms / utility / tenant as applicable | Power capacity, metering, power quality, tariffs/pass-throughs |
| Cooling and heat schedule | Kristal Farms / tenant / community heat entity | Cooling envelope, heat export, metering, cooperation obligations |
| Fibre service schedule | Kristal Farms / telecom / tenant | Connectivity scope, demarcation, availability, reporting |
| Community Benefits Agreement / IBA | Project company / community / government partners | Benefits, jobs, training, heat allocation, governance |
| Environmental and monitoring protocol | Project company / regulators / community bodies | ΔT limits, reporting, response procedures |
| End-of-lease annex | Kristal Farms / tenant | Removal, restoration, transfer, decommissioning |

---

## 10. Allocation of commercial value

The model should make clear that value is not captured only through tenant leases.

### 10.1 Tenant value

Tenants receive:

- serviced compute pad;
- renewable-energy positioning;
- cold-climate cooling advantage;
- heat-recovery / ESG story;
- physical isolation and black-box tenancy;
- fibre access;
- modular expansion option;
- reversibility.

### 10.2 Community value

The community receives potential value through:

- useful heat delivered;
- diesel displacement;
- public-building heating support;
- greenhouse heat;
- training and jobs;
- improved fibre connectivity;
- community benefit payments or equivalent allocations;
- role in governance and decision-making;
- local participation in operations where feasible.

### 10.3 Utility / hydro partner value

Hydro or utility partners may receive:

- stable local demand;
- infrastructure partnership opportunity;
- reduced diesel reliance in isolated systems;
- improved local energy utilization;
- data for planning and grid/hydro operation;
- public benefit story tied to clean power.

### 10.4 Investor value

Investors may receive exposure to:

- contracted infrastructure revenue;
- modular/phased deployment;
- diversified tenant base;
- ESG infrastructure;
- replicable Labrador coastal expansion model;
- community-supported asset base.

---

## 11. Reversibility and end-of-lease model

Reversibility is part of the commercial design. The project should not lock the community into abandoned equipment or stranded infrastructure.

### 11.1 End-of-lease process

At the end of a lease, the tenant should:

1. provide notice according to lease terms;
2. coordinate safe shutdown with the operator;
3. disconnect from power, cooling, heat, and fibre interfaces under operator supervision;
4. remove tenant-owned equipment and container within the agreed removal window;
5. coordinate port handling, crane/lift, and shipping logistics;
6. restore the pad to defined return condition;
7. complete joint inspection;
8. settle final metering and incident adjustments.

A standard removal window of **30 to 90 days** may be used as a planning assumption, subject to final lease terms, weather, sealift windows, and site safety requirements.

### 11.2 Restoration standard

The tenant should return the pad:

- clean;
- free of tenant-specific debris;
- without damage beyond normal wear;
- with tenant modifications removed unless accepted by the operator;
- with no hazardous materials left on site;
- with all security credentials and access permissions terminated.

### 11.3 Security and data handling at exit

Because the host does not access tenant systems, the tenant remains responsible for:

- data deletion or migration;
- hardware sanitization;
- credential revocation;
- export-control compliance;
- removal of storage media;
- tenant software and model handling.

Host responsibility is limited to physical disconnection, access control, metering closure, and site restoration verification.

---

## 12. Open commercial items for partner diligence

The following items should be resolved during partner alignment and due diligence.

| Open item | Why it matters | Needed next evidence |
|---|---|---|
| Power tariff / cost allocation | Drives tenant pricing and community benefit model | Utility discussion, hydro study, regulatory review |
| Pad lease pricing | Defines investor and tenant economics | Market comparison, tenant interviews, financial model |
| Fibre cost and SLA | Determines tenant viability | Fibre route study, telecom quotes, latency testing |
| Heat tariff or benefit allocation | Determines how heat value is shared | Community consultation, public-building heat audit |
| Tenant eligibility policy | Protects community and project reputation | Legal review, governance input, sanctions/export-control review |
| SLA targets | Must be technically achievable | Electrical, cooling, fibre, and O&M validation |
| Insurance and liability | Required for financeability | Insurance broker review, legal drafting |
| End-of-lease annex | Prevents abandoned containers or site damage | Logistics plan, lease drafting, operator procedure |
| Community benefit mechanism | Central to consent and legitimacy | FPIC/CBA process, community governance design |
| NDA financial model | Required for serious investors | CAPEX/OPEX estimates, sensitivities, partner terms |

---

## 13. Partner decision ask

For this commercial model, the immediate partner ask is not to approve a final investment decision. The first ask is to validate the structure and identify which partner role applies.

Partners should be asked to confirm:

1. Which role they may play: power, fibre, investment, tenant, modular supply, governance, or heat offtake.
2. Whether the pad-lease model is commercially understandable.
3. Whether the black-box tenancy boundary is acceptable.
4. Which SLA areas they require quantified first.
5. Which diligence data they need before moving to an NDA financial model.
6. Whether they support a phased pilot-pad approach before larger expansion.

---

## 14. Partner-facing conclusion

Kristal Farms should be commercialized as a **phased infrastructure platform**. The first project does not need to prove every future revenue stream. It needs to prove that a Labrador coastal community can host a small number of serviced compute pads that are powered by local hydro, connected by fibre, cooled efficiently, and integrated into a useful heat loop.

The commercial strength of the model is its combination of:

- pad lease revenue;
- metered power/cooling/fibre service;
- modular expansion;
- heat-first community value;
- black-box tenant privacy;
- visible local benefits;
- reversibility;
- replication across Labrador coastal communities.

The next commercial step is a partner-alignment package: confirm roles, define the pilot pad, validate power/fibre/heat interfaces, establish the first tenant requirements, and move detailed pricing into an NDA-backed financial model.
