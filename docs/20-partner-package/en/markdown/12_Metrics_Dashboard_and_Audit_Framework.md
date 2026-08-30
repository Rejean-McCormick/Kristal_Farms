# 12_Metrics_Dashboard_and_Audit_Framework

**Project:** Kristal Farms — Labrador Coast Partner Package  
**First target:** Nain, Labrador  
**Expansion logic:** Replicable Labrador coastal communities  
**Document type:** Partner-facing due diligence appendix  
**Status:** Draft for partner review  

---

## 1. Purpose

This document defines the metrics, dashboard structure, reporting cadence, audit process, and data-governance rules for the Kristal Farms Labrador coast project.

The purpose is to make the project measurable from the beginning. Partners, community representatives, technical reviewers, and funders should be able to see whether the project is delivering on its central claims:

1. clean hydro-powered compute;
2. efficient cooling;
3. useful heat delivery to the host community;
4. reduced diesel dependence;
5. reliable fibre-connected compute operations;
6. local jobs and training;
7. transparent community benefit reporting; and
8. privacy-preserving black-box tenancy.

The dashboard is not a marketing tool. It is a project-accountability tool.

---

## 2. Core dashboard principle

Kristal Farms should use a **small, stable, auditable metric set**.

The project should avoid constantly changing metrics, adding speculative indicators, or publishing numbers that cannot be measured consistently. Every public-facing metric should have:

- a clear definition;
- a measurement source;
- a reporting frequency;
- an accountable owner;
- a validation method;
- a status: confirmed, estimated, or under validation.

The project should report enough to prove performance, without exposing tenant data, private community information, or commercially sensitive details.

---

## 3. Dashboard categories

The dashboard should be organized into six categories:

```text
1. Energy and compute efficiency
2. Heat recycling and diesel displacement
3. Water and environmental performance
4. Connectivity and pad operations
5. Community benefits
6. Governance, audit, and incidents
```

Each category should include a small number of headline metrics, supported by more detailed internal logs.

---

## 4. Energy and compute efficiency metrics

### 4.1 Power Usage Effectiveness — PUE

**Definition:**

PUE measures the ratio of total facility power to IT equipment power.

```text
PUE = Total facility energy / IT equipment energy
```

**Purpose:**

PUE shows how much non-IT overhead the site requires. A lower PUE indicates that more energy is going directly into compute rather than cooling, pumping, lighting, auxiliary loads, or site overhead.

**Report as:**

```text
Monthly PUE
Quarterly PUE
Annual average PUE
Winter PUE
Summer PUE
```

**Measurement source:**

- main site energy meter;
- pad-level IT meters;
- auxiliary load meters for pumps, dry coolers, heat pumps, network equipment, site lighting, and control systems.

**Public dashboard status:**

Public, aggregated.

**Notes:**

Do not publish a final target until the site design and seasonal heat/cooling model are validated. The dashboard can show a placeholder target range during pre-feasibility, then a binding target after technical design.

---

### 4.2 IT energy consumed

**Definition:**

Total electrical energy consumed by tenant compute equipment.

**Report as:**

```text
kWh_IT per month
MWh_IT per quarter
MWh_IT per year
```

**Measurement source:**

- pad-level metered power handoff;
- tenant container energy meter;
- site supervisory control system.

**Public dashboard status:**

Public, aggregated across pads. Do not report tenant-specific values unless permitted by contract.

---

### 4.3 Facility overhead energy

**Definition:**

Energy used by non-IT systems required to operate the site.

Examples include:

- pumps;
- heat exchangers and controls;
- heat pump booster, where used;
- dry coolers;
- network and NOC equipment;
- lighting;
- security systems;
- site controls.

**Report as:**

```text
kWh_auxiliary per month
% of total facility energy
```

**Public dashboard status:**

Public, aggregated.

---

### 4.4 Renewable energy share

**Definition:**

Percentage of site energy supplied by local hydro or other confirmed renewable sources.

**Report as:**

```text
% renewable energy share
MWh renewable energy supplied
MWh backup/diesel energy used, if any
```

**Measurement source:**

- hydro plant meter;
- substation meter;
- diesel generator runtime and fuel logs;
- backup energy meter, if applicable.

**Public dashboard status:**

Public.

**Notes:**

This metric should distinguish normal operations from emergency backup events.

---

## 5. Heat recycling and diesel displacement metrics

### 5.1 Useful heat delivered

**Definition:**

Thermal energy delivered to productive local uses.

**Report as:**

```text
MWh_th delivered to public buildings
MWh_th delivered to homes
MWh_th delivered to greenhouse
MWh_th delivered to thermal storage
Total MWh_th useful heat delivered
```

**Measurement source:**

- heat meters at building substations;
- greenhouse heat meter;
- thermal storage charge/discharge meters;
- central heat loop sensors.

**Public dashboard status:**

Public, aggregated. Building-by-building reporting should require community approval.

---

### 5.2 Heat Utilization Factor — HUF

**Definition:**

HUF measures the share of available server waste heat that is productively reused.

```text
HUF = Useful heat reused / Total recoverable server heat
```

**Purpose:**

HUF is the central metric for the heat-first model. It shows whether the project is actually turning compute waste heat into community value.

**Report as:**

```text
Monthly HUF
Winter HUF
Summer HUF
Annual average HUF
HUF by heat sink category
```

**Measurement source:**

- IT loop temperature and flow sensors;
- building loop heat meters;
- greenhouse heat meters;
- thermal storage meters;
- reject-loop meters.

**Public dashboard status:**

Public.

**Notes:**

Seasonal differences should be expected. Winter HUF should normally be higher because heating demand is higher. Summer HUF depends on greenhouse demand, storage capacity, domestic hot water demand, and permitted rejection limits.

---

### 5.3 Heat rejected

**Definition:**

Thermal energy that is not reused or stored and must be rejected to a permitted sink.

**Report as:**

```text
MWh_th rejected to air-side dry coolers
MWh_th rejected to non-contact bay/seawater exchanger
% of available heat rejected
```

**Measurement source:**

- reject-loop heat meters;
- dry cooler control logs;
- cold-source intake/discharge temperature sensors;
- environmental compliance records.

**Public dashboard status:**

Public, aggregated.

**Notes:**

The operating hierarchy is:

```text
Reuse → Store → Reject
```

Rejection should be reported transparently, but it should not be framed as failure if it occurs within permitted limits and after reuse/storage capacity has been exhausted.

---

### 5.4 Diesel avoided

**Definition:**

Estimated diesel fuel not burned because server heat replaced heating fuel and hydro-backed operations reduced diesel use.

**Report as:**

```text
Litres diesel avoided
MWh equivalent avoided
tCO2e avoided, if emission factor is approved
```

**Measurement source:**

- baseline heating fuel records;
- building heat meters;
- diesel generator fuel logs;
- approved diesel-to-energy conversion factor;
- approved emissions factor, if used.

**Public dashboard status:**

Public, aggregated.

**Notes:**

The baseline must be agreed before public claims are made. The metric should distinguish:

```text
1. Heating diesel avoided
2. Electricity-generation diesel avoided
3. Emergency diesel still used
```

---

### 5.5 Heat priority delivery

**Definition:**

Tracks whether heat is delivered according to the agreed community priority order.

Recommended priority order:

```text
1. Critical public buildings
2. Homes / residential heating
3. Domestic hot water
4. Greenhouse and food systems
5. Thermal storage
6. Rejection
```

**Measurement source:**

- heat dispatch logs;
- building substation meters;
- Heat Committee review records;
- incident logs.

**Public dashboard status:**

Public summary only.

---

## 6. Water and environmental performance metrics

### 6.1 Water Usage Effectiveness — WUE

**Definition:**

WUE measures water consumed for cooling per unit of IT energy.

```text
WUE = Litres of water consumed / kWh_IT
```

**Purpose:**

WUE confirms whether the project is avoiding evaporative cooling and large water consumption.

**Expected design logic:**

Kristal Farms uses closed loops and non-contact heat exchange. Therefore, water consumption should be near zero aside from maintenance, treatment, or minor top-up requirements.

**Report as:**

```text
Litres consumed per month
Litres/kWh_IT
Maintenance top-up volume
```

**Public dashboard status:**

Public.

---

### 6.2 Cold-source temperature compliance

**Definition:**

Tracks intake and discharge temperatures at the non-contact cold-source exchanger, where applicable.

**Report as:**

```text
Intake temperature
Discharge temperature
Delta-T
Number of exceedance events
Duration of exceedance events
```

**Measurement source:**

- temperature sensors;
- environmental monitoring logs;
- cold-source pump and exchanger records.

**Public dashboard status:**

Public summary. Detailed raw logs may be provided to regulators or auditors.

---

### 6.3 Environmental incidents

**Definition:**

Any reportable incident related to cooling, spills, wildlife, water temperature, fuel handling, construction, waste, noise, or permit compliance.

**Report as:**

```text
Number of incidents
Severity level
Corrective action status
Days to close
```

**Public dashboard status:**

Public summary, subject to legal and regulatory requirements.

---

## 7. Connectivity and pad operations metrics

### 7.1 Fibre availability

**Definition:**

Percentage of time fibre connectivity is available to support tenant operations.

**Report as:**

```text
Monthly fibre availability %
Quarterly fibre availability %
Number of outage events
Total outage minutes
```

**Measurement source:**

- network monitoring system;
- NOC logs;
- telecom partner reports.

**Public dashboard status:**

Public, aggregated. Do not publish tenant traffic content or sensitive network metadata.

---

### 7.2 Latency p95

**Definition:**

The 95th percentile network latency over a defined measurement path.

**Report as:**

```text
Latency p95 to agreed exchange point
Latency p95 to agreed cloud/tenant handoff point
Monthly average and peak periods
```

**Measurement source:**

- NOC monitoring;
- synthetic network tests;
- telecom partner reports.

**Public dashboard status:**

Public if the path is not commercially sensitive. Otherwise, NDA-only.

---

### 7.3 Pad uptime

**Definition:**

Percentage of time each compute pad has available power, cooling interface, and fibre handoff.

**Report as:**

```text
Pad uptime %
Power availability %
Cooling-interface availability %
Fibre-handoff availability %
```

**Measurement source:**

- pad meter;
- cooling interface sensors;
- NOC logs;
- site control system.

**Public dashboard status:**

Public aggregated. Tenant-specific pad reporting should follow lease terms.

---

### 7.4 Pad occupancy

**Definition:**

Share of available pad capacity that is leased, installed, or actively used.

Recommended sub-metrics:

```text
Leased capacity
Installed capacity
Active IT load
Available expansion capacity
```

**Measurement source:**

- lease records;
- pad meters;
- tenant activation records;
- site capacity register.

**Public dashboard status:**

Public aggregated. Tenant identities and commercial details remain confidential unless disclosed by agreement.

---

## 8. Community benefit metrics

### 8.1 Local jobs

**Definition:**

Number of jobs created or supported by the project, with priority given to local and community-based employment.

**Report as:**

```text
Direct local jobs
Operations jobs
Construction jobs
Training placements
Seasonal jobs
```

**Measurement source:**

- payroll records;
- contractor reports;
- community employment reporting;
- training program records.

**Public dashboard status:**

Public aggregated. No personal employee information.

---

### 8.2 Training hours

**Definition:**

Total project-funded or project-supported training hours delivered to local participants.

**Report as:**

```text
Training hours completed
Number of participants
Certifications achieved
Apprenticeships or placements created
```

**Measurement source:**

- training provider records;
- attendance logs;
- certification records;
- project workforce reports.

**Public dashboard status:**

Public aggregated.

---

### 8.3 Local procurement

**Definition:**

Share of project purchasing directed to local or regional suppliers where feasible.

**Report as:**

```text
Local procurement spend
Regional procurement spend
Total procurement spend
% local/regional procurement
```

**Measurement source:**

- procurement records;
- contractor reporting;
- invoice records.

**Public dashboard status:**

Public aggregated. Supplier-level details may be NDA-only.

---

### 8.4 Greenhouse output

**Definition:**

Food or plant output from heat-supported greenhouse operations.

**Report as:**

```text
kg produce grown
kg produce distributed locally
greenhouse operating days
MWh_th used by greenhouse
```

**Measurement source:**

- greenhouse records;
- heat meters;
- distribution records;
- community food program records.

**Public dashboard status:**

Public.

**Notes:**

The greenhouse metric should be treated as a community-value metric, not as a guaranteed commercial agriculture claim until greenhouse design, operator, and growing plan are confirmed.

---

### 8.5 Community benefits delivered

**Definition:**

Tracks benefits delivered under any Community Benefits Agreement, Impact Benefit Agreement, or equivalent project agreement.

Possible categories:

```text
heat credits
training commitments
local hiring commitments
community fund contributions
public building heat support
connectivity improvements
education or knowledge access programs
```

**Measurement source:**

- agreement obligations register;
- project council minutes;
- community benefit reports;
- finance records.

**Public dashboard status:**

Public summary, subject to agreement terms.

---

## 9. Governance and trust metrics

### 9.1 Dashboard publication cadence

**Minimum cadence:**

```text
Monthly dashboard update
Quarterly performance review
Annual public report
Annual independent audit
```

The monthly dashboard should be short and readable. The quarterly review should be detailed enough for committees and partners. The annual report should summarize technical, environmental, community, and governance performance.

---

### 9.2 Committee review status

**Definition:**

Tracks whether required reviews occurred.

**Report as:**

```text
Project Council review completed: yes/no
Heat Committee review completed: yes/no
Environment Committee review completed: yes/no
Community reporting session completed: yes/no
```

**Public dashboard status:**

Public.

**Notes:**

Committee names and final structure may change after community process. The dashboard should adapt to the governance structure agreed with the community.

---

### 9.3 Grievances and dispute resolution

**Definition:**

Tracks formal grievances submitted, reviewed, resolved, or escalated.

**Report as:**

```text
Number of grievances received
Number resolved
Number open
Average days to resolution
Escalated cases
```

**Public dashboard status:**

Public aggregated. No personal or confidential details.

---

### 9.4 Corrective action closure

**Definition:**

Tracks whether corrective actions from audits, incidents, or committee reviews are closed on time.

**Report as:**

```text
Corrective actions opened
Corrective actions closed
Corrective actions overdue
Average closure time
```

**Public dashboard status:**

Public summary.

---

## 10. Black-box tenancy and data boundaries

The dashboard must respect the black-box tenancy model.

### 10.1 Host-visible data

The host may monitor and report physical infrastructure metrics, including:

```text
energy use
power availability
cooling loop temperature
cooling loop flow
cooling delta-T
pad uptime
bandwidth volume
fibre availability
technical alarms
heat delivery
water and environmental compliance metrics
```

### 10.2 Host-excluded data

The host must not access or publish:

```text
tenant application logs
tenant data
tenant model content
tenant prompts or outputs
tenant packet payloads
sensitive tenant metadata
user-level traffic details
proprietary workload details
```

### 10.3 Reporting rule

All public dashboard information should be aggregated unless a tenant, community body, or partner has explicitly agreed to disclose more detail.

---

## 11. Data architecture

### 11.1 Measurement layers

The monitoring system should use four layers:

```text
1. Sensor layer
   - meters, flow sensors, temperature sensors, network monitors, environmental sensors

2. Site control layer
   - SCADA or equivalent system for power, cooling, heat, and alarms

3. Dashboard data layer
   - cleaned, aggregated, non-sensitive data for public and partner reporting

4. Audit archive
   - tamper-evident logs, raw meter data, incident records, and signed reports
```

### 11.2 Raw data retention

Physical infrastructure logs may be retained long term for trend analysis, auditability, and replication learning. Retention should be documented in the Data Room and should exclude tenant data.

### 11.3 Data quality status labels

Every metric should be labeled as one of the following:

```text
Measured
Estimated
Modeled
Under validation
Not yet available
```

This avoids presenting early estimates as final performance.

---

## 12. Reporting cadence

### 12.1 Monthly dashboard

The monthly dashboard should include:

```text
PUE
WUE
MWh_th useful heat delivered
HUF
diesel avoided
fibre availability
pad uptime
pad occupancy
local jobs
training hours
greenhouse output
open incidents
open corrective actions
```

### 12.2 Quarterly review

The quarterly review should include:

```text
dashboard trend analysis
seasonal heat performance
fibre and uptime review
incident review
community benefit tracking
risk updates
committee recommendations
corrective action status
```

### 12.3 Annual public report

The annual report should include:

```text
annual metric summary
comparison with agreed targets
community benefit summary
environmental performance summary
financial categories without sensitive details
governance and grievance summary
auditor statement
next-year improvement plan
```

### 12.4 Independent audit

The independent audit should review:

```text
meter accuracy
PUE/WUE calculation method
heat metering and HUF calculation
fuel displacement baseline
fibre and uptime records
environmental compliance logs
community benefit commitments
privacy/data-boundary compliance
corrective action closure
```

---

## 13. Target-setting approach

Targets should be set in phases.

### Phase 0 — Concept and partner alignment

Use provisional metrics only.

```text
Status: modeled / under validation
No binding public performance claims
```

### Phase 1 — Site confirmation

Confirm what can be measured.

```text
Metering plan
baseline fuel data request
tenant privacy boundary
heat sink inventory
fibre baseline
```

### Phase 2 — Pre-feasibility

Define draft targets.

```text
draft PUE target
draft WUE target
draft HUF seasonal range
draft uptime target
draft diesel-avoidance baseline
```

### Phase 3 — Pilot pad

Switch from modeled to measured values.

```text
measured pad energy
measured heat delivery
measured reject-loop behavior
measured fibre performance
measured auxiliary load
```

### Phase 4 — Expansion pads

Set binding operational targets.

```text
annual performance target
heat allocation target
community benefit target
fibre SLA target
audit requirements
```

---

## 14. Example dashboard layout

```text
Kristal Farms Labrador Coast Dashboard
Reporting month: [Month Year]
Site: Nain pilot / Labrador coast replication
Status: Concept / Pre-feasibility / Pilot / Operating

Energy and compute
- PUE: [value/status]
- IT energy: [MWh_IT]
- Renewable energy share: [%]

Heat and diesel displacement
- Useful heat delivered: [MWh_th]
- HUF: [%]
- Heat rejected: [MWh_th]
- Diesel avoided: [litres / MWh / tCO2e]

Water and environment
- WUE: [L/kWh_IT]
- Cold-source delta-T: [°C]
- Environmental incidents: [number/status]

Connectivity and operations
- Fibre availability: [%]
- Latency p95: [ms]
- Pad uptime: [%]
- Pad occupancy: [%]

Community benefits
- Local jobs: [number]
- Training hours: [hours]
- Greenhouse output: [kg]
- Community benefits delivered: [summary]

Governance and audit
- Committee reviews completed: [status]
- Open grievances: [number]
- Open corrective actions: [number]
- Next public report: [date]
```

---

## 15. Partner decision points

Partners should confirm the following before pilot deployment:

```text
1. Which metrics are public, NDA-only, or internal.
2. Which entity owns each data source.
3. Which meters and sensors are revenue-grade versus operational-grade.
4. Which baselines are accepted for diesel avoided.
5. Which latency/fibre paths are used for SLA reporting.
6. Which community benefits are binding commitments.
7. Which committee or council reviews the dashboard each quarter.
8. Which independent auditor or technical reviewer validates annual results.
```

---

## 16. Metrics register

| Category | Metric | Unit | Public? | Status before pilot | Primary owner |
|---|---:|---:|---|---|---|
| Energy | PUE | ratio | Yes | Modeled | Site operator |
| Energy | IT energy | MWh_IT | Aggregated | Metering plan | Site operator / tenant interface |
| Energy | Renewable share | % | Yes | Under validation | Utility / site operator |
| Heat | Useful heat delivered | MWh_th | Yes | Heat-sink inventory | Heat operator |
| Heat | HUF | % | Yes | Modeled | Heat operator |
| Heat | Heat rejected | MWh_th | Yes | Modeled | Heat operator |
| Diesel | Diesel avoided | L / MWh / tCO2e | Yes | Baseline needed | Site operator / community |
| Water | WUE | L/kWh_IT | Yes | Design estimate | Site operator |
| Environment | Cold-source delta-T | °C | Yes summary | Permitting needed | Environment lead |
| Fibre | Fibre availability | % | Yes aggregate | Telecom design | Telecom/NOC |
| Fibre | Latency p95 | ms | Conditional | Telecom design | Telecom/NOC |
| Operations | Pad uptime | % | Yes aggregate | SLA draft | Site operator |
| Operations | Pad occupancy | % | Yes aggregate | Commercial pipeline | Site operator |
| Community | Local jobs | count | Yes aggregate | Workforce plan | Project council / operator |
| Community | Training hours | hours | Yes aggregate | Training plan | Project council / operator |
| Food | Greenhouse output | kg | Yes | Greenhouse plan | Greenhouse operator |
| Governance | Grievances | count/status | Yes aggregate | Process needed | Project council |
| Audit | Corrective actions | count/status | Yes summary | Audit plan | Site operator / auditor |

---

## 17. What should not be reported publicly

The public dashboard should not include:

```text
tenant names without consent
tenant application data
tenant logs
tenant model information
packet payloads
sensitive network metadata
employee names or personal records
household-level heat consumption without consent
commercial pricing
unvalidated financial projections
security-sensitive site details
```

---

## 18. Open design items

The following items should be finalized during partner alignment and community process:

```text
1. Final metric list for the first public dashboard.
2. Exact PUE, WUE, HUF, uptime, and fibre targets.
3. Diesel baseline method and emissions factor.
4. Heat allocation priority order.
5. Greenhouse measurement method and operator responsibility.
6. Committee review structure.
7. Auditor selection and audit scope.
8. Data retention policy for physical infrastructure logs.
9. Public/NDA/internal classification for each metric.
10. Dashboard publication platform and update workflow.
```

---

## 19. Summary

The Metrics Dashboard and Audit Framework makes Kristal Farms measurable and accountable.

The most important metrics are:

```text
PUE
WUE
Heat Utilization Factor
MWh_th delivered
Diesel avoided
Fibre availability
Latency p95
Pad uptime
Pad occupancy
Local jobs
Training hours
Greenhouse output
Community benefits delivered
Incident and corrective-action closure
```

The dashboard should prove the central project thesis: Labrador coast compute infrastructure should not only consume clean power; it should also deliver local heat, reduce diesel dependence, improve connectivity, create skills, and maintain transparent governance while protecting tenant confidentiality.

