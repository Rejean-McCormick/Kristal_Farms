# 06_Technical_Architecture.md

# Kristal Farms — Technical Architecture

**Document status:** Partner-facing draft  
**Package:** Kristal Farms Partner Documentation  
**Document number:** 06  
**Primary site logic:** Nain first; Labrador coastal replication  
**Audience:** Infrastructure partners, utility partners, modular data center suppliers, fibre partners, compute tenants, community/government technical reviewers  
**Purpose:** Explain the technical architecture of the Kristal Farms Labrador coast model clearly enough for partner diligence, without presenting a full engineering specification.

---

## 1. Executive Technical Summary

Kristal Farms is a village-first, heat-first infrastructure model for modular AI compute on the Labrador coast. The project places containerized compute pads near the village, close to public buildings, homes, greenhouse heat users, port logistics, fibre termination, and local operations. A short medium-voltage connection links a local hydro source to a village substation. Compute is exported by fibre, not by long-distance electricity transmission. Server heat is captured and reused locally before any surplus heat is rejected.

The technical model is built around five interfaces:

1. **Power interface** — metered hydro-backed electrical service from the village substation to each compute pad.
2. **Cooling interface** — closed-loop heat capture from tenant containers through non-contact plate heat exchangers.
3. **Heat interface** — village heat loop serving public buildings, homes, domestic hot water preheat, storage, and greenhouse demand.
4. **Fibre interface** — protected fibre service from a local Network Operations Center to tenant pads and regional connectivity.
5. **Operations interface** — host-side monitoring of physical infrastructure metrics only, while tenants retain control and confidentiality inside black-box containers.

The model is not a remote dam-campus model. The core architecture is to bring power from the hydro source to the village and place the containers where heat can be used. The value of the project depends on the integration of compute, heat, fibre, and community infrastructure.

---

## 2. Design Principles

### 2.1 Village-first siting

The compute yard should be located at the port, village edge, or another suitable village-adjacent site rather than at a remote hydro intake or powerhouse. This reduces the distance between server heat and heat users. It also improves access for sealift, operations, emergency response, fibre termination, and community visibility.

### 2.2 Short power path, not long transmission

The project should avoid new long high-voltage transmission corridors. Power should be delivered through a short medium-voltage feed from the local hydro source to a village substation. This reduces capital cost, permitting complexity, line losses, and schedule risk.

### 2.3 Export compute, not electrons

The output of the site is data service, compute capacity, and knowledge work. The project should prioritize fibre export of compute results rather than long-distance transmission of electricity. This is central to the Labrador coast model: use energy locally, move value digitally.

### 2.4 Reuse → Store → Reject

Server heat is treated as a useful product. The operating hierarchy is:

```text
1. Reuse heat locally
2. Store heat when immediate demand is lower than supply
3. Reject only the remaining surplus
```

The system should reject heat only after priority building loads, greenhouse loads, and available thermal storage have been served.

### 2.5 Two sealed circuits

The IT cooling loop and the village/building heat loop remain hydraulically separate. Heat is transferred through plate heat exchangers. There is no fluid mixing between tenant equipment, village buildings, and environmental water.

### 2.6 Black-box tenancy

The host provides power, cooling, fibre, site security, metering, and physical operations. The tenant controls the inside of the container, including servers, applications, data, logs, models, and internal security. Host monitoring is limited to physical infrastructure metrics.

### 2.7 Modular expansion

Capacity should scale by adding pads, not by committing to one large campus. Each pad should be a separable module with standardized civil, power, cooling, fibre, metering, and lease interfaces.

### 2.8 Reversibility

Pad infrastructure should be removable where practical. When a lease ends, a container can be disconnected and removed, leaving a controlled site restoration path. This is important for community consent, financing risk, and phased deployment.

---

## 3. System Overview

### 3.1 High-level architecture

```text
Local Hydro Source
      |
      | short MV feeder
      v
Village Substation / Energy Center
      |
      | metered feeders
      v
Compute Pad Yard near port / village edge
      |
      | heat capture through sealed IT loops
      v
Central Heat Exchange Station
      |
      | village heat loop
      v
Public buildings / homes / DHW / greenhouse / storage
      |
      | data export
      v
Local NOC -> regional fibre hub -> tenant networks
```

### 3.2 Core physical components

| Component | Role |
|---|---|
| Local hydro source | Provides renewable electricity for village loads and compute pads, subject to validated resource and grid studies. |
| Short MV feeder | Connects hydro source to village substation without long high-voltage transmission build-out. |
| Village substation | Central electrical handoff, protection, metering, and distribution point. |
| Compute pad yard | Fenced modular yard for tenant containers, preferably near the port or village edge. |
| Pad-mounted interface equipment | Provides power handoff, fibre ports, cooling connection, heat metering, and alarm interfaces. |
| Central heat exchange station | Transfers server heat into the village heat loop and manages reuse, storage, and rejection priority. |
| Village heat loop | Distributes useful heat to public buildings, homes, domestic hot water preheat, storage, and greenhouse uses. |
| Cold-source interface | Provides final heat rejection through non-contact exchange to seawater/bay water or dry coolers. |
| Network Operations Center | Houses fibre, routing, patching, monitoring, and site communications systems. |
| Operations dashboard | Tracks power, heat, cooling, fibre, pad uptime, heat utilization, and safety metrics. |

### 3.3 Functional boundaries

The architecture separates responsibility into three zones:

| Zone | Controlled by | Scope |
|---|---|---|
| Host infrastructure zone | Kristal Farms / local operating entity | Power, cooling interfaces, heat loop, site security, fibre handoff, external monitoring. |
| Tenant container zone | Compute tenant | Servers, storage, operating systems, applications, model workloads, encryption, internal telemetry. |
| Community heat zone | Project/community heat operator | Heat allocation, building interface units, greenhouse heat use, thermal storage, public reporting. |

---

## 4. Site Architecture

### 4.1 Preferred site location

The preferred compute pad yard is a village-adjacent location with:

- practical sealift or port access;
- short distance to the substation;
- short distance to heat users;
- feasible fibre termination;
- manageable civil works;
- room for phased pad expansion;
- acceptable noise, access, drainage, snow, and safety separation;
- community visibility without creating nuisance impacts.

The site does not need to be directly beside the hydro plant. The hydro plant supplies power; the village supplies the heat sink, operating base, logistics base, and community benefit context.

### 4.2 Site zones

The site should be planned as a set of controlled zones:

```text
A. Port / logistics interface
B. Compute pad yard
C. Electrical substation and switchgear area
D. Heat exchange and pumping station
E. Thermal storage area
F. Greenhouse / seasonal heat sink
G. Network Operations Center
H. Maintenance and spare parts area
I. Security gate and access control
J. Snow storage / drainage / fire access corridors
```

### 4.3 Site access and logistics

The pad yard should support seasonal marine delivery of containers and major equipment. Design assumptions should include:

- standard container handling and lifting plans;
- laydown space for delivery windows;
- defined winter access routes;
- spare parts storage for critical pumps, valves, sensors, filters, fibre components, and electrical protection devices;
- heavy-equipment access for container replacement;
- emergency access for fire, electrical, and mechanical response.

### 4.4 Civil works

Civil works should be kept simple and modular:

- compacted pad foundations or elevated steel skids suited to local ground conditions;
- drainage designed for freeze/thaw and heavy precipitation;
- snow management routes;
- containment around glycol or treated-water equipment;
- fenced perimeter and controlled gates;
- service corridors for power, fibre, and heat piping;
- clear separation between public areas and tenant infrastructure.

---

## 5. Local Hydro Integration

### 5.1 Purpose

The hydro integration is designed to serve local compute loads without requiring a long new high-voltage export corridor. The hydro source must be validated through hydrology, grid, environmental, and community studies before project commitments are made.

### 5.2 Energy flow

```text
Hydro source
  -> local generation / interconnection
  -> short MV feeder
  -> village substation
  -> pad feeders, pumps, heat station, NOC, auxiliary systems
```

### 5.3 Operating priority

The operating model should preserve community energy security. Compute pads should be added only when there is sufficient power headroom and heat offtake value. Local critical loads must remain protected.

Suggested operating priority:

1. Critical community loads.
2. Heat system pumps, controls, and safety equipment.
3. NOC and communications.
4. Contracted tenant pad loads.
5. Flexible/batch compute or surplus compute activity.
6. Optional Kristals/public-interest compute layer where surplus energy and governance approval exist.

### 5.4 Existing diesel generation

Existing diesel generation may remain as emergency backup for critical community loads and rare outage events. The project should not depend on diesel for normal compute operations. Diesel runtime reduction is a community and environmental value metric, not a replacement for hydro validation.

### 5.5 Required validation

Before final design, the project needs:

- hydro resource validation;
- seasonal generation profile;
- firm versus non-firm power assessment;
- protection and interconnection study;
- power quality assessment;
- islanded-grid and load-step analysis if applicable;
- emergency load priority plan;
- environmental and permitting review;
- community/FPIC process alignment.

---

## 6. Short MV Connection and Village Substation

### 6.1 Medium-voltage feeder

The MV feeder should be short, protected, and designed for staged expansion. It should avoid unnecessary right-of-way clearing and avoid overbuilding for speculative future load.

Key design features:

- metered hydro source output;
- feeder protection and sectionalizing;
- fault isolation;
- grounding and bonding;
- winter-accessible route;
- allowance for staged pad additions;
- coordination with existing village electrical infrastructure.

### 6.2 Village substation

The village substation is the electrical center of the project. It should support:

- incoming MV feeder from hydro source;
- step-down transformers as needed;
- pad feeders;
- heat station feeders;
- NOC feeders;
- building heat-loop auxiliary loads;
- metering at each major interface;
- protective relays;
- power quality monitoring;
- safety isolation;
- lockout/tagout procedures;
- physical security and weather protection.

### 6.3 Metering points

Minimum metering should include:

| Metering point | Purpose |
|---|---|
| Hydro source output | Establish total generation and availability. |
| MV feeder input/output | Track feeder losses and power quality. |
| Substation bus | Track site-level power balance. |
| Each pad feeder | Bill tenant power and monitor load behavior. |
| Heat station auxiliary loads | Track pumps, controls, booster heat pump, and dry coolers. |
| NOC load | Track communications infrastructure load. |
| Village heat delivery meters | Track useful heat delivered by building or heat sink. |

### 6.4 Power quality

Tenant compute equipment is sensitive to voltage events, harmonics, and outages. The substation and pad handoffs should include:

- voltage monitoring;
- event recording;
- harmonic monitoring where needed;
- surge protection;
- selective coordination;
- staged start-up and shut-down sequencing;
- clear trip responsibility for faults by pad.

---

## 7. Compute Pad Yard

### 7.1 Pad concept

Each compute pad is a prepared physical position that can accept a modular data center container. The pad is not just a parking location; it is an infrastructure interface.

A standard pad should provide:

- structural support;
- power handoff;
- cooling handoff;
- heat metering;
- fibre handoff;
- grounding/bonding;
- leak detection where applicable;
- alarm interface;
- physical access control;
- fire response access;
- snow clearance access.

### 7.2 Container type

The baseline assumption is a standard 40-foot modular data center container or equivalent modular unit. Suppliers may provide different form factors, but each must comply with the project interface requirements.

### 7.3 Yard layout

The yard should be arranged for:

- modular expansion;
- safe crane/forklift access;
- separation between containers;
- power and pipe corridor clarity;
- service access to both sides of each container;
- emergency access;
- noise management;
- snow and drainage management;
- easy pad removal or replacement.

### 7.4 Pad expansion logic

Expansion should be controlled by three conditions:

1. **Power capacity confirmed.** Hydro and substation capacity are validated for the next pad.
2. **Heat sink confirmed.** Public building, housing, storage, or greenhouse heat demand can productively use the added heat.
3. **Fibre capacity confirmed.** The NOC and trunk capacity can support the tenant SLA.

Compute should not expand faster than heat and fibre can support.

---

## 8. Container Interface Standard

### 8.1 Interface philosophy

The host provides external services. The tenant owns the internal compute environment. The interface must be standardized enough to let multiple compliant vendors or tenants use the site without redesigning the full yard.

### 8.2 Electrical interface

The host should provide:

- metered power handoff;
- pad feeder protection;
- grounding and bonding point;
- emergency disconnect;
- power quality monitoring;
- start-up/shutdown coordination;
- maximum contracted load limit.

The tenant should provide:

- internal power distribution;
- UPS or rack-level backup if required by tenant workload;
- internal redundancy design;
- internal equipment protection beyond the host handoff.

### 8.3 Cooling interface

The host should provide:

- external cooling supply/return connections;
- plate heat exchanger or approved non-contact interface;
- flow and temperature metering;
- pressure and leak monitoring;
- isolation valves;
- bypass/curtailment path;
- alarm connection for high temperature, low flow, and ΔT excursions.

The tenant should provide:

- internal rack cooling system;
- coolant chemistry management on the tenant side where applicable;
- internal pump/valve design if inside the container;
- safe operating envelope and heat rejection profile.

### 8.4 Fibre interface

The host should provide:

- dual fibre ports or equivalent A/B links;
- structured patching through the NOC;
- link status monitoring;
- agreed demarcation point;
- physical port labeling;
- path protection where feasible.

The tenant should provide:

- internal network equipment;
- encryption;
- workload routing;
- tenant-side cybersecurity;
- internal telemetry;
- application-level availability.

### 8.5 Controls and alarms

The host sees and records physical infrastructure metrics, including:

- power draw;
- power quality events;
- cooling supply/return temperature;
- coolant flow;
- pressure;
- heat delivered;
- pad link status;
- bandwidth volume;
- environmental alarms;
- access alarms;
- fire/smoke alarm state;
- container external status.

The host does not see:

- tenant application logs;
- tenant data;
- model weights;
- model prompts or outputs;
- packet payloads;
- internal user identities;
- proprietary workload details;
- tenant security logs unless explicitly shared by contract.

### 8.6 Physical security interface

The host controls site perimeter, yard access, camera coverage of external areas, badge/access logs, and emergency access. Tenant-specific container access should be defined in the lease, including who may enter the container and under what procedure.

---

## 9. Cooling Architecture

### 9.1 Cooling goal

The cooling architecture captures high-quality server heat, transfers useful heat to the village loop, and protects IT equipment when local heat demand is lower than server heat output.

### 9.2 IT loop

The IT loop may use direct liquid cooling, rear-door heat exchangers, or another approved closed-loop rack cooling approach.

Baseline temperature concept:

```text
IT supply: approximately 30–45 °C
IT return: approximately 45–60 °C
```

The final values must be confirmed with tenant equipment, rack density, server cooling technology, and heat offtake needs.

### 9.3 Heat capture options

| Option | Use case | Notes |
|---|---|---|
| Direct Liquid Cooling | High-density CPU/GPU workloads | Highest heat quality and best fit for useful heat recovery. |
| Rear-Door Heat Exchangers | Faster retrofit or lower integration complexity | Useful where tenant equipment is not fully DLC-ready. |
| Immersion cooling | Potential high-density option | Requires supplier-specific maintenance, fluid handling, and safety procedures. |

The project should prefer the option that provides stable, useful heat while preserving tenant modularity.

### 9.4 Plate heat exchangers

Heat exchange should be non-contact. Plate heat exchangers separate:

- tenant/IT fluid from host heat-loop fluid;
- host heat-loop fluid from building-side systems;
- host rejection loop from seawater/bay water.

Titanium or other corrosion-suitable materials may be required at seawater interfaces, subject to engineering review.

### 9.5 Cold source

The preferred final cold source is seawater or bay water near the port, using non-contact heat exchange. Dry coolers provide backup or shoulder-season capacity. The architecture should not depend on a small river as the main heat sink.

### 9.6 Dry coolers

Dry coolers are used for:

- backup heat rejection;
- shoulder-season operation;
- maintenance periods;
- protection when heat storage is full;
- controlled curtailment support.

Dry coolers should not replace the heat-first objective. They are a resilience and safety layer.

### 9.7 Controls

The cooling control system should enforce:

1. building heat demand first;
2. domestic hot water preheat where applicable;
3. thermal storage charging;
4. greenhouse heat supply;
5. dry cooler or bay rejection for remaining surplus;
6. load curtailment if heat rejection capacity becomes constrained.

### 9.8 Commissioning tests

Before tenant operation, cooling acceptance should include:

- pressure test;
- leak test;
- controls test;
- flow balancing;
- ΔT verification;
- failover to dry cooler;
- high-temperature alarm;
- low-flow alarm;
- safe curtailment test;
- no-cross-contamination confirmation.

---

## 10. Heat Loop Architecture

### 10.1 Purpose

The heat loop is a community-value system, not a waste-disposal system. It delivers server heat to public buildings, homes, domestic hot water preheat, greenhouse use, and thermal storage.

### 10.2 Heat users

Priority users should be defined with the community and project governance process. A likely priority order is:

1. clinic and emergency services;
2. school;
3. community buildings;
4. municipal facilities;
5. nearby homes;
6. domestic hot water preheat;
7. greenhouse;
8. optional industrial or workshop heat loads;
9. storage;
10. rejection.

### 10.3 Building interface units

Each building connection should include:

- local plate heat exchanger;
- isolation valves;
- heat meter;
- control valve;
- differential pressure control where needed;
- freeze protection strategy;
- backflow and contamination safeguards;
- bypass for maintenance;
- clear ownership boundary.

### 10.4 Domestic hot water

Server heat may preheat domestic hot water through building substations. Final temperature lift and Legionella protection remain building-specific design responsibilities. The project should not claim final DHW compliance until building audits are complete.

### 10.5 Greenhouse heat

The greenhouse is a flexible seasonal heat sink. It is valuable in shoulder and warm months when building heating demand is lower. In deep winter, homes and priority public buildings should take precedence.

### 10.6 Thermal storage

Thermal storage smooths daily heat mismatch. It can:

- capture surplus heat during compute peaks;
- cover morning/evening building peaks;
- reduce rejection;
- improve Heat Utilization Factor;
- provide time for controlled pad throttling when demand shifts.

Storage should be sized after measured building load profiles and pilot pad heat profiles are known.

### 10.7 Heat loop metrics

The heat loop should be measured by:

- MWh_th delivered;
- Heat Utilization Factor;
- supply and return temperatures;
- flow;
- storage state of charge;
- diesel displaced;
- heat delivered by building category;
- greenhouse heat delivered;
- heat rejected.

---

## 11. Fibre and Network Operations Center

### 11.1 Purpose

Fibre is the export corridor for the project. The site does not primarily export electricity; it exports compute results, hosted workloads, and data services.

### 11.2 NOC function

The Network Operations Center should house:

- fibre termination;
- optical distribution frame;
- core switching/routing;
- monitoring systems;
- out-of-band management;
- redundant power supplies;
- communications equipment;
- physical access control;
- environmental controls;
- patch documentation.

### 11.3 Fibre architecture

The preferred architecture includes:

```text
Tenant container
  -> dual pad fibre links
  -> NOC switching/patching
  -> protected trunk
  -> regional hub
  -> tenant/cloud networks
```

The design should use A/B pad links where feasible and trunk path protection where feasible. Actual routes and redundancy depend on available regional fibre infrastructure and partner participation.

### 11.4 Network metrics

The NOC should monitor:

- link availability;
- latency p95 to defined hub;
- jitter;
- packet loss;
- error rates;
- bandwidth utilization;
- failover events;
- outage duration;
- repair time;
- port status;
- optical signal quality.

### 11.5 Network security boundary

The host may monitor availability, link health, bandwidth volume, and routing status. The host should not inspect packet payloads or tenant application traffic. Tenant data security remains the tenant’s responsibility unless a separate managed-services contract is executed.

---

## 12. Black-Box Tenancy Model

### 12.1 Host responsibility

The host is responsible for:

- pad site readiness;
- power delivery to the demarcation point;
- cooling interface availability;
- heat loop operation;
- fibre handoff availability;
- external site security;
- physical alarms;
- metering;
- maintenance of host infrastructure;
- dashboard reporting for physical and community metrics.

### 12.2 Tenant responsibility

The tenant is responsible for:

- server hardware;
- storage;
- internal networking;
- operating systems;
- software;
- application data;
- model data;
- workload scheduling;
- encryption;
- internal monitoring;
- tenant compliance obligations;
- equipment removal at lease end unless otherwise agreed.

### 12.3 What the host sees

The host may see:

- kW and kWh;
- voltage and power quality events;
- coolant flow;
- coolant temperatures;
- ΔT;
- heat delivered;
- external alarms;
- link status;
- bandwidth volume;
- uptime;
- pad occupancy;
- physical access events.

### 12.4 What the host does not see

The host does not see:

- tenant files;
- tenant databases;
- model prompts;
- model outputs;
- application logs;
- packet contents;
- internal metadata that could expose confidential operations;
- tenant customer information;
- proprietary algorithms.

### 12.5 Optional hardware attestation

Hardware attestation or trusted execution environments may be offered where a tenant requires additional integrity assurance. This should be contract-specific, not a default requirement for every tenant.

---

## 13. Operations and Monitoring

### 13.1 Operations model

Kristal Farms requires a local operations function supported by remote technical expertise. The operating model should combine:

- local site technicians;
- remote NOC support;
- utility partner support;
- heat-system operator;
- tenant support escalation;
- emergency response coordination;
- community reporting.

### 13.2 Monitoring stack

The host monitoring stack should integrate:

- substation monitoring;
- pad meter data;
- power quality logs;
- heat loop SCADA;
- cooling alarms;
- NOC telemetry;
- access control;
- camera coverage of external areas;
- environmental sensors;
- dashboard reporting.

### 13.3 Core operating metrics

| Metric | Purpose |
|---|---|
| PUE | Track facility energy overhead. |
| WUE | Confirm low/no evaporative water consumption. |
| HUF | Track useful heat reuse share. |
| MWh_th delivered | Show actual community heat value. |
| Diesel avoided | Connect heat/power value to fuel reduction. |
| Pad uptime | Track reliability. |
| Pad occupancy | Track utilization. |
| Fibre availability | Track data export reliability. |
| Latency p95 | Track service quality to hub. |
| Heat rejected | Track remaining waste and improvement opportunities. |
| Safety alarms | Track system integrity and response quality. |

### 13.4 Public dashboard

A public or partner-facing dashboard can report community-value metrics, excluding tenant confidential data. Candidate dashboard items:

- total heat delivered;
- diesel avoided;
- greenhouse heat supplied;
- pad uptime;
- fibre availability;
- PUE/WUE;
- local jobs/training hours;
- service incidents;
- maintenance windows;
- annual audit status.

### 13.5 Maintenance

Maintenance procedures should include:

- seasonal inspection before winter;
- heat exchanger cleaning/inspection;
- pump testing;
- valve exercise;
- dry cooler test;
- substation inspection;
- generator emergency test where applicable;
- fibre failover test;
- pad start/stop sequencing test;
- leak detection test;
- controls and alarm simulation.

---

## 14. Safety and Environmental Controls

### 14.1 Non-contact water protection

All environmental exchange should be non-contact. Seawater or bay water should not mix with IT coolant or building loop water. Plate heat exchangers and monitoring reduce contamination risk.

### 14.2 Fluid containment

Where glycol or treated water is used, the system should include:

- secondary containment where practical;
- leak detection;
- isolation valves;
- spill response materials;
- maintenance procedures;
- inventory tracking;
- environmental reporting process.

### 14.3 Thermal discharge control

Any final heat rejection to seawater/bay water must comply with applicable permits and temperature limits. The design should monitor intake and discharge temperature and include alarms for ΔT excursions.

### 14.4 Fire and life safety

Each container and pad should include or interface with:

- fire detection;
- appropriate suppression strategy;
- emergency disconnect;
- access route for responders;
- clear signage;
- hazardous materials inventory;
- tenant emergency contact procedure.

### 14.5 Noise

Noise sources include dry coolers, pumps, transformers, generators during testing, and container fans if present. The yard layout should include setbacks, enclosure choices, operating limits, and seasonal sound checks where necessary.

### 14.6 Cold climate and coastal conditions

Design must account for:

- snow loading;
- wind exposure;
- salt corrosion;
- icing;
- freeze protection;
- thaw settlement;
- seasonal access;
- spares availability;
- sealift timing.

---

## 15. Phasing

### Phase 0 — Technical alignment

- Confirm partner roles.
- Confirm source documents.
- Confirm site-selection basis.
- Identify utility, fibre, modular supplier, and community counterparts.
- Establish technical decision register.

### Phase 1 — Site confirmation

- Validate candidate village-adjacent pad location.
- Confirm port/logistics route.
- Confirm substation location.
- Identify heat users.
- Confirm preliminary fibre path.
- Start environmental and community review.

### Phase 2 — Power and heat pre-feasibility

- Hydro resource validation.
- MV feeder concept.
- Substation one-line concept.
- Load study.
- Heat demand survey.
- Initial pipe route.
- Cold-source assessment.
- Controls concept.

### Phase 3 — Pilot pad engineering

- Select pilot pad size.
- Define standard pad interface.
- Choose cooling approach.
- Define tenant SLA boundary.
- Define metering plan.
- Confirm NOC requirements.
- Confirm operations staffing.
- Develop commissioning tests.

### Phase 4 — Pilot deployment

- Build substation/pad infrastructure.
- Install first container.
- Commission power, cooling, fibre, controls, and heat loop.
- Operate through first seasonal test period.
- Report metrics publicly or to partners.

### Phase 5 — Heat loop expansion

- Add priority buildings.
- Add domestic hot water preheat where feasible.
- Add storage.
- Add greenhouse interface.
- Tune heat allocation rules.
- Improve HUF.

### Phase 6 — Additional pads

- Add pads only after power, fibre, and heat sink capacity are confirmed.
- Standardize interfaces.
- Add redundancy where demand justifies it.
- Replicate lessons to next Labrador coastal community.

---

## 16. Partner Interface Matrix

| Partner type | Technical role | Key decision points |
|---|---|---|
| Utility / hydro partner | Hydro availability, feeder, substation, protection, metering | Firm power, interconnection, ownership boundary, outage procedures. |
| Community / government partner | Site consent, heat priorities, public buildings, governance | Site access, FPIC process, heat allocation, training. |
| Modular data center supplier | Container design, rack cooling, electrical integration | Container standard, cooling temperature range, maintenance access. |
| Fibre / telecom partner | Trunk route, NOC integration, redundancy, SLA | Bandwidth, path protection, latency, repair model. |
| Compute tenant | Workload, internal hardware, security, lease load | Load profile, black-box boundary, uptime needs, data isolation. |
| Infrastructure investor | Phasing, risk allocation, financeability | Capex sequence, revenue dependencies, technical gates. |
| Heat system partner | Building loop, exchangers, storage, greenhouse | Heat demand, building retrofits, DHW safety, storage sizing. |

---

## 17. Technical Data Gaps

The following items must be resolved before final engineering:

1. Confirmed hydro generation profile.
2. Firm power available to compute after community priority loads.
3. MV feeder route and cost.
4. Substation capacity and ownership model.
5. Pad yard location and geotechnical conditions.
6. Port handling and seasonal sealift constraints.
7. Fibre route, redundancy, latency, and repair obligations.
8. Heat demand by building and season.
9. Building radiator/DHW retrofit requirements.
10. Greenhouse heat absorption profile.
11. Thermal storage sizing.
12. Environmental permissions for bay/seawater heat rejection.
13. Tenant cooling technology and temperature envelope.
14. Tenant load profile and ramp behavior.
15. Site operations staffing and training plan.
16. Fire, safety, and emergency response procedures.
17. Community governance and heat allocation process.
18. Final SLA and lease boundaries.

---

## 18. Engineering Deliverables Required Next

The next technical work package should produce:

- site layout concept drawing;
- single-line electrical diagram;
- MV feeder concept;
- substation sizing note;
- pad interface standard;
- cooling and heat process flow diagram;
- heat-loop route map;
- cold-source intake/rejection concept;
- NOC block diagram;
- metering and instrumentation list;
- controls sequence narrative;
- commissioning checklist;
- failure-mode review;
- operations staffing plan;
- preliminary capex class estimate;
- risk register update.

---

## 19. Technical Positioning Statement

Kristal Farms is a coastal Labrador infrastructure model that combines local hydro, modular compute, heat reuse, fibre export, and community benefit. The architecture is strongest when it stays simple:

```text
Short power path.
Village-first containers.
Useful heat first.
Fibre export.
Black-box tenancy.
Phased pads.
Community-visible metrics.
```

This is the technical basis for Nain as the first target and Labrador coastal communities as the replication logic.

---

## Internal Source Basis

This draft was prepared from the current Kristal Farms source corpus, especially:

- `Kristal Farms Internal Reference Document`
- `Kristal Farms — Heat Recycling Plan`
- `Kristal Farms — Cost Advantage & Strategic Rationale`
- `Documentation Kristal Farms`
- `Kristal Farms: A Perspective on Modular AI Compute at Cold-Climate Hydropower Sites`

This section is for drafting control and can be removed from external partner versions.
