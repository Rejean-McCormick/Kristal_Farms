# 07_Heat_Recycling_and_Community_Value

**Project:** Kristal Farms — Labrador Coast Partner Package  
**Document type:** Partner-facing technical/community brief  
**Primary target:** Nain first; Labrador coastal replication model  
**Status:** Draft v1  
**Distribution:** Partner-facing, non-NDA version  
**Related documents:**  
- `00_Kristal_Farms_Partner_Overview.md`  
- `02_Labrador_Coast_Project_Thesis.md`  
- `06_Technical_Architecture.md`  
- `08_Connectivity_and_Black_Box_Tenancy.md`  
- `11_Governance_FPIC_and_Community_Benefits.md`  
- `12_Metrics_Dashboard_and_Audit_Framework.md`  
- `13_Risk_Register.md`

---

## 1. Purpose

This document explains how Kristal Farms turns server waste heat into direct local value for Labrador coastal communities.

The project is not only a compute project. It is a heat, power, connectivity, and community-benefit project. The core design decision is to place modular compute containers close to village heat users, connect them to local hydro through a short medium-voltage feed, export compute results by fibre, and reuse the heat locally before any heat is rejected.

For the first target community, Nain, heat recycling is central to the value proposition. The same logic can later be replicated across other Labrador coastal communities where local hydro potential, marine logistics, fibre, community consent, and heat demand can align.

---

## 2. Executive Summary

Kristal Farms is designed around a simple thermal rule:

> **Reuse → Store → Reject**

Server heat is treated as a local asset, not as a waste product. The system first directs useful heat to public buildings, domestic hot water preheating, nearby housing, and greenhouse use. If immediate heat demand is lower than available heat, the system stores heat in short-duration thermal tanks. Only after useful heat and storage are saturated does the system reject remaining heat through a controlled non-contact cooling path.

This approach creates five partner-relevant advantages:

1. **Community value:** server heat can reduce local reliance on diesel heating and provide a visible public benefit.
2. **Project legitimacy:** heat reuse gives the host community a direct reason to support the infrastructure.
3. **Cost advantage:** natural cold and local heat reuse reduce conventional data-center cooling overhead.
4. **Environmental performance:** closed-loop, non-contact heat exchange reduces water consumption and protects local water bodies.
5. **Replication logic:** the same heat-first architecture can be repeated by adding pads, buildings, storage, and greenhouse capacity in phases.

The first deployment should be sized around validated heat sinks, not only around available compute demand. In practice, compute capacity should expand as the community confirms useful heat demand and infrastructure readiness.

---

## 3. Heat-First Principle

The project follows a heat-first operating principle:

```text
1. Reuse heat locally.
2. Store heat when immediate demand is lower than heat production.
3. Reject heat only when reuse and storage are saturated.
```

This principle affects siting, engineering, contracts, community governance, and operations.

### 3.1 What heat-first means

Heat-first means the compute yard is not treated as an isolated data center. It is treated as a village energy asset. The thermal design is built around nearby users:

- clinic
- school
- municipal or community buildings
- public safety facilities
- nearby homes
- greenhouse or food-production facilities
- future community or light-industrial users, if approved

Heat-first also means the compute system should not be scaled blindly. A site should add compute pads only when the heat loop, public-building connections, greenhouse plan, environmental safeguards, fibre, and community governance can support the next increment.

### 3.2 What heat-first does not mean

Heat-first does not mean the project compromises tenant privacy or compute reliability. Tenants remain inside a black-box boundary. The host manages physical services: power, cooling, metering, heat recovery, alarms, uptime, and fibre availability. The host does not access tenant data, logs, models, or packet payloads.

Heat-first also does not mean the project depends on dumping heat into small rivers. The preferred design uses non-contact heat exchange and avoids reliance on fragile local freshwater bodies as the primary heat sink.

---

## 4. Why Heat Recycling Matters on the Labrador Coast

Many Labrador coastal communities face high energy costs, seasonal logistics constraints, cold winters, imported fuel dependence, and limited local infrastructure options. In that context, compute heat has value only if it is captured where people can use it.

A remote compute site at a hydro source may reduce electrical transmission needs, but it loses most of the community heat value if it is too far from buildings. Kristal Farms therefore uses a village-first architecture:

```text
Local hydro source
    → short medium-voltage connection
    → village substation / port-edge energy node
    → modular compute pad yard
    → heat loop to public buildings, housing, DHW, and greenhouse
    → fibre export of compute results
```

The basic economic idea is that the community should not only host infrastructure. It should receive tangible benefits from the infrastructure: useful heat, local jobs, better connectivity, possible greenhouse production, and transparent performance reporting.

---

## 5. System Architecture

The heat recycling system has four main parts:

1. **IT heat capture**
2. **Heat exchange and temperature management**
3. **Village heat distribution**
4. **Storage and controlled rejection**

### 5.1 Conceptual heat path

```text
AI servers / compute racks
    → Direct liquid cooling or rear-door heat exchangers
    → warm IT loop, typically 45–60°C outlet
    → plate heat exchanger
    → optional heat-pump booster for higher temperature needs
    → building loop / DHW preheat / greenhouse loop
    → thermal storage if immediate demand is low
    → controlled reject loop only when needed
```

### 5.2 Two sealed circuits

The design uses two sealed circuits:

| Circuit | Purpose | Key protection |
|---|---|---|
| IT loop | Removes heat from servers and racks | Treated water or water-glycol; isolated from buildings and environment |
| Building loop | Delivers heat to community users | Water loop; isolated through plate heat exchangers and building substations |

The two circuits transfer heat but do not mix fluids. This protects equipment, buildings, and the environment.

### 5.3 Non-contact environmental interface

Any environmental heat exchange should be non-contact. The system should use plate heat exchangers, with appropriate materials for the local water conditions. Where seawater or bay water is used as a cold source, titanium plate heat exchangers or equivalent corrosion-resistant equipment should be evaluated.

No project document should imply that IT coolant is discharged into the environment. It is not.

---

## 6. Heat Capture at the Container

The preferred capture options are:

### 6.1 Direct Liquid Cooling

Direct liquid cooling captures heat at high-value components such as CPUs and GPUs. It can provide warmer and more useful heat than conventional air cooling.

**Advantages:**

- higher thermal quality
- better fit for AI/HPC hardware
- lower fan energy
- more useful temperature range for heat reuse
- improved ability to deliver predictable heat to buildings

### 6.2 Rear-Door Heat Exchangers

Rear-door heat exchangers can be used where tenant hardware or vendor constraints make direct liquid cooling harder to deploy quickly.

**Advantages:**

- lower integration complexity
- retrofit compatibility
- useful transitional architecture
- easier deployment with some containerized systems

### 6.3 Practical selection rule

Use direct liquid cooling where available and compatible with tenant hardware. Use rear-door heat exchangers where speed, tenant equipment, or supplier availability requires a simpler interface.

The partner-facing position should be flexible: Kristal Farms provides the pad, cooling interface, heat recovery system, and metering; the exact rack-level cooling method can vary by tenant and hardware generation.

---

## 7. Heat Delivery Temperatures

The system should support two heat-delivery modes.

### 7.1 Low-temperature service

If buildings can accept supply temperatures around 50–60°C, heat can be injected directly from the heat exchanger into the building loop.

Best suited for:

- oversized radiators
- fan-coil systems
- new low-temperature emitters
- greenhouse hydronic loops
- preheat applications
- domestic hot water preheat

### 7.2 Boosted service

If legacy heating systems require higher temperatures, a central heat-pump booster can raise supply temperatures to approximately 65–75°C, subject to final engineering validation.

Best suited for:

- older public buildings
- critical buildings with higher temperature requirements
- domestic hot water final lift, where needed
- deep winter support

The booster should be sized around priority heat loads, not around every possible load. Oversizing the booster would add cost and complexity too early.

---

## 8. Priority Heat Users

The heat allocation plan should be confirmed through community process, but the draft priority order is:

```text
1. Critical public buildings
2. Schools and community buildings
3. Domestic hot water preheat
4. Nearby housing
5. Greenhouse and food-production uses
6. Future community or light-industrial uses
7. Storage
8. Environmental rejection
```

### 8.1 Critical public buildings

Initial heat users should be buildings where heat value is obvious and socially defensible:

- clinic or health facility
- school
- community hall
- municipal office
- emergency services
- elder-care or vulnerable-resident facilities, if applicable

These users create a clear public-benefit case and provide stable winter demand.

### 8.2 Nearby housing

Housing connection should follow public-building validation. Homes closest to the thermal spine should be evaluated first because short distribution runs reduce cost, losses, and complexity.

### 8.3 Domestic hot water

DHW should normally be treated as preheat unless final design confirms safe and compliant full-temperature service. Legionella safeguards, final-lift requirements, and building-code requirements must be addressed during engineering.

### 8.4 Greenhouse

The greenhouse is a strategic seasonal heat sink. It can support food security and local economic activity while absorbing heat when public-building demand is lower.

In winter, households and public buildings take priority. In shoulder seasons and summer, the greenhouse becomes more important as a flexible heat sink.

---

## 9. Seasonal Operating Model

### 9.1 Winter

Winter is the strongest season for heat reuse.

Operational priorities:

- serve critical public buildings first
- serve nearby housing where connected
- preheat domestic hot water
- maintain storage for morning and evening peaks
- run more heat-producing compute when heat demand is high, where tenant contracts allow
- minimize rejection

### 9.2 Shoulder seasons

Shoulder seasons require active balancing.

Operational priorities:

- mix public-building and greenhouse heat
- use thermal storage to smooth peaks
- monitor tank state of charge
- shift batch compute toward high-value heat periods where possible
- avoid unnecessary rejection

### 9.3 Summer

Summer heat demand from buildings will be lower. The greenhouse becomes the main useful heat sink, subject to crop plan and ventilation design.

Operational priorities:

- direct heat to greenhouse first
- charge storage where useful
- reject only when greenhouse and storage are saturated
- consider planned compute modulation if thermal constraints are binding
- log all rejection events for the dashboard and Heat Committee

---

## 10. Thermal Storage

Thermal storage allows the system to separate compute heat production from immediate building demand.

### 10.1 Short-duration storage

The first deployment should use stratified thermal tanks. A practical starting design target is approximately 2–12 hours of average thermal load, with around 6 hours as an initial planning assumption until heat loads are validated.

Uses:

- morning and evening peak support
- short-term smoothing
- improved heat utilization factor
- operational flexibility
- reduced need for rejection

### 10.2 Future seasonal or multi-week storage

Longer-duration storage may be considered later if useful and practical:

- borehole thermal energy storage
- pit thermal energy storage
- larger insulated tank systems
- integration with greenhouse thermal mass

These options should not be part of the first partner promise. They are future design options after the first heat loop proves useful.

---

## 11. Environmental Safeguards

The heat system should be designed to avoid contamination, avoid freshwater dependence, and limit ecological disturbance.

### 11.1 Non-contact heat exchange

All heat exchange with buildings and environmental cold sources should occur through plate heat exchangers. IT coolant, building-loop water, and environmental water remain separated.

### 11.2 No small-river dependency

The project should not depend on a small river as the main heat sink. Small rivers may have limited thermal capacity, ecological sensitivity, ice constraints, or seasonal flow limitations.

### 11.3 Controlled rejection

Heat rejection is a fallback, not the business model.

Any rejection system should include:

- temperature monitoring
- flow monitoring
- differential temperature limits
- alarms
- event logs
- environmental review
- operating procedures for curtailment or load shifting

### 11.4 Low water consumption

The preferred cooling design avoids evaporative cooling towers. Water is circulated in closed loops, with only minor makeup water needs. This supports a near-zero water consumption position, subject to final engineering confirmation.

---

## 12. Controls and Operations

The operating system should encode the heat hierarchy directly into controls.

### 12.1 Heat-aware compute scheduling

Where tenant contracts allow, batch or flexible compute can be scheduled to match heat value.

Examples:

- run batch jobs harder when storage is low and public-building demand is high
- reduce or shift flexible jobs when tanks are full and greenhouse demand is low
- preserve guaranteed tenant loads within contractual limits
- never compromise critical community heat needs for low-priority compute

### 12.2 Building-loop controls

The building loop should use:

- outdoor-reset heat curves
- supply and return temperature monitoring
- differential pressure control
- flow meters
- building-level heat meters
- alarms for abnormal ΔT, low flow, freezing risk, or substation faults

### 12.3 Operating responsibility

The site operator should manage:

- central heat exchanger station
- pumps and valves
- thermal storage
- environmental reject system
- public metrics
- maintenance program
- incident response

Building owners or community partners should manage their internal building-side systems unless a separate maintenance agreement is created.

---

## 13. Community Value

Heat recycling is the clearest way the project becomes locally useful.

### 13.1 Diesel displacement

Where diesel is used for heating or backup power, server heat can reduce fuel deliveries and local combustion. The amount of diesel avoided must be measured and reported, not assumed.

A partner-facing claim should use this language:

> The project is designed to displace a portion of diesel heating demand where heat users are connected and loads are validated.

Avoid claiming full diesel elimination unless confirmed by engineering and operations data.

### 13.2 Public-service resilience

Connected public buildings may receive a more stable and locally sourced heat supply. This can support community resilience, especially for critical facilities.

### 13.3 Food security

A greenhouse can convert surplus heat into local food production, especially during periods when building heat demand is lower. The greenhouse should be treated as both a heat sink and a community-development asset.

### 13.4 Local employment and training

Heat-loop operations create local roles beyond ordinary data center security or site maintenance:

- heat-loop technician
- pump and controls maintenance
- building substation maintenance
- greenhouse operations
- monitoring and dashboard support
- environmental sampling support
- emergency response support

Training should be tied to the governance and community-benefits framework.

### 13.5 Local visibility

Unlike abstract compute revenue, heat delivered to a clinic, school, greenhouse, or homes is visible. That visibility is important for trust and long-term political durability.

---

## 14. Governance of Heat Allocation

Heat allocation should be governed transparently.

### 14.1 Heat Committee

A Heat Committee should review:

- seasonal heat priorities
- connected heat users
- heat utilization factor
- rejected heat events
- curtailment events
- storage performance
- greenhouse heat windows
- proposed new heat connections
- social heat quota, if adopted

The committee should include community representation and technical representation. Exact composition should be finalized through the governance and FPIC process.

### 14.2 Confirmed principles

The partner-facing document can treat these as confirmed design principles:

- community heat value is central
- public buildings receive priority
- reuse comes before storage
- storage comes before rejection
- heat allocation is transparent
- heat metrics are reported publicly
- tenant privacy is preserved
- environmental safeguards are mandatory

### 14.3 Open design items

These items require partner and community decisions:

- final list of priority buildings
- greenhouse operator and crop model
- tariff or free-heat structure
- social heat quota
- heat committee composition
- heat interruption rules
- ownership of building substations
- maintenance responsibility for customer-side equipment
- process for adding housing connections

---

## 15. Metrics and Public Dashboard

The heat system should publish a small, stable set of monthly metrics. The goal is transparency without overwhelming partners or exposing sensitive tenant information.

### 15.1 Core heat metrics

| Metric | Definition | Why it matters |
|---|---|---|
| Useful heat delivered | MWh_th delivered to buildings, greenhouse, or storage | Shows real community value |
| Heat Utilization Factor | Useful heat reused divided by total heat available | Shows whether heat-first design is working |
| Diesel avoided | Litres, MWh equivalent, and tCO2e equivalent where validated | Connects heat to cost and emissions benefits |
| Heat by sink | Public buildings, housing, greenhouse, storage | Shows who benefits |
| Rejected heat | MWh_th rejected after reuse and storage | Shows remaining improvement opportunity |

### 15.2 Data-center efficiency metrics

| Metric | Definition | Why it matters |
|---|---|---|
| PUE | Total facility energy divided by IT energy | Tracks data-center efficiency |
| WUE | Water consumed per unit IT energy | Shows low water-consumption cooling performance |
| Pad uptime | Availability of power, cooling, and fibre services | Supports tenant trust |
| Pad occupancy | Share of deployed pad capacity in use | Connects commercial use to heat production |

### 15.3 Community metrics

| Metric | Definition |
|---|---|
| Local jobs | Number of project jobs held locally |
| Training hours | Hours delivered to local workers or trainees |
| Greenhouse output | Food output by category, where applicable |
| Community benefit payments | Reported as allowed by agreement |
| Heat complaints or incidents | Logged and reviewed through governance |

### 15.4 Reporting cadence

Recommended cadence:

```text
Monthly dashboard:
- useful heat delivered
- HUF
- PUE / WUE
- diesel avoided
- rejected heat
- greenhouse heat use
- pad uptime

Quarterly review:
- Heat Committee review
- environment review
- incidents and corrective actions
- heat allocation adjustments

Annual report:
- full performance summary
- diesel and emissions methodology
- community benefits
- local employment and training
- expansion readiness
```

---

## 16. Implementation Path

### Phase 1 — Heat demand inventory

Actions:

- identify public buildings
- collect fuel-use data where available
- identify heating systems and supply-temperature needs
- map candidate housing clusters
- identify greenhouse site and operator options
- estimate preliminary heat loads

Deliverables:

- heat demand register
- candidate heat-user map
- building retrofit priority list
- initial thermal spine route

### Phase 2 — Pilot heat loop

Actions:

- connect one or more priority public buildings
- install central heat exchanger station
- install heat meters and building substations
- install initial thermal storage
- connect pilot compute pad
- establish monthly dashboard

Deliverables:

- validated heat delivery data
- first HUF results
- first diesel-avoided estimate
- operational lessons

### Phase 3 — Greenhouse integration

Actions:

- finalize greenhouse model
- define seasonal heat window
- install greenhouse heat interface
- coordinate food-production plan
- monitor summer heat absorption

Deliverables:

- greenhouse heat-use data
- summer rejection reduction data
- community food-output reporting

### Phase 4 — Housing and expansion pads

Actions:

- expand heat loop to nearby housing where practical
- add additional compute pads only as heat sinks and fibre capacity support growth
- refine storage sizing
- refine heat tariffs and service agreements

Deliverables:

- expanded heat-user base
- improved annual HUF
- stronger commercial and community case

---

## 17. Partner Roles

### Hydro / utility partner

Potential role:

- confirm available hydro capacity
- support short MV connection
- coordinate metering
- confirm protection and interconnection requirements
- support emergency backup planning

### Community / government partner

Potential role:

- identify priority heat users
- participate in governance
- support FPIC and community process
- approve land and heat-corridor access where applicable
- define community-benefit priorities

### Infrastructure investor

Potential role:

- fund pad yard, heat loop, storage, and substations
- support phased capital plan
- review performance metrics and risk controls

### Compute tenant

Potential role:

- bring IT load
- comply with pad and cooling interface requirements
- maintain black-box tenant boundary
- agree to physical metering and SLA conditions
- identify flexible load where applicable

### Modular data center supplier

Potential role:

- provide container systems compatible with heat capture
- support DLC or rear-door heat exchanger options
- confirm interface temperatures, flow rates, and maintenance needs

### Greenhouse / food partner

Potential role:

- operate greenhouse
- define seasonal heat demand
- coordinate crop plan
- report community food output
- support summer heat utilization

---

## 18. Key Diligence Questions

Before investment or construction, the project needs answers to the following:

### Heat demand

- Which public buildings are first priority?
- What are their historical heating loads?
- What heating temperatures do they require?
- Which buildings can accept low-temperature heat directly?
- Which buildings require a booster?

### Distribution

- What is the shortest practical thermal spine?
- Which routes avoid difficult ground, rights-of-way, and sensitive areas?
- What pipe losses are expected?
- Which buildings need substations?

### Cooling and rejection

- What is the preferred cold source?
- What environmental limits apply?
- What ΔT limits are required?
- What seasonal constraints exist?
- What backup cooling capacity is required?

### Greenhouse

- Who operates it?
- What crops are realistic?
- What heat profile does it need?
- How much summer heat can it absorb?
- What is the business and community-benefit model?

### Governance

- Who sits on the Heat Committee?
- Who approves heat priorities?
- How are disputes handled?
- Is there a social heat quota?
- How are dashboard metrics reviewed?

### Contracts

- What is the heat-supply agreement?
- What are interruption rules?
- Who owns customer-side equipment?
- How are heat meters used for billing or benefit tracking?
- How are tenant SLAs coordinated with heat-first operations?

---

## 19. Partner Decision Ask

For the next stage, Kristal Farms should ask partners to support a focused heat-validation package:

```text
1. Confirm priority public buildings.
2. Collect building heat-load and fuel-use data.
3. Confirm village thermal-spine route options.
4. Validate cold-source and environmental constraints.
5. Identify greenhouse operator and site options.
6. Define first-pad heat output assumptions.
7. Agree on monthly public heat metrics.
8. Define Heat Committee setup for the pilot phase.
```

The objective is not to finalize the full district heating system immediately. The objective is to validate a first heat loop that proves useful heat delivery, diesel displacement potential, environmental safeguards, and community reporting.

---

## 20. Positioning Statement

Kristal Farms should position heat recycling as a core project differentiator:

> Kristal Farms does not treat server heat as waste. It treats heat as the first local product of the compute system. The project exports compute by fibre, keeps thermal value in the community, and scales only where useful heat demand, community consent, hydro capacity, and fibre access align.

---

## 21. Internal Source Basis

This document was prepared from the current Kristal Farms source corpus, especially:

- `Kristal Farms — Heat Recycling Plan`
- `Kristal Farms Internal Reference Document`
- `Kristal Farms — Cost Advantage & Strategic Rationale`
- `Documentation Kristal Farms`
- `EC8ADFDE-9E2F-11F0-9303-BF2B70071435.pdf`

For partner distribution, remove this source-basis section or move it to the internal archive if the package is being shared externally.
