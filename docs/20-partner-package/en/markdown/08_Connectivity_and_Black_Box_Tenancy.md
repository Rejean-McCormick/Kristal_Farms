# 08_Connectivity_and_Black_Box_Tenancy.md

# Kristal Farms — Connectivity and Black-Box Tenancy

**Document status:** Partner-facing draft  
**Package:** Kristal Farms Partner Documentation  
**Primary geography:** Labrador coast, with Nain as first target community  
**Version:** v0.1  
**Date:** 2026-05-02  

---

## 1. Purpose

This document explains how Kristal Farms exports compute results by fibre while protecting tenant confidentiality through a black-box tenancy model.

The project is designed around a simple operating boundary:

> Kristal Farms provides the physical infrastructure: power, cooling, heat export, fibre connectivity, pad access, metering, safety systems, and site operations.  
> The tenant controls the compute environment: hardware, operating system, software stack, models, application data, logs, and workload operations.

The host does not need access to tenant data to operate the site. The host only needs physical and network-health metrics required to keep power, cooling, heat recovery, fibre, safety, and community reporting systems working.

This document is intended for compute tenants, telecom/fibre partners, infrastructure investors, community/government partners, and technical diligence reviewers.

---

## 2. Core position

Kristal Farms is not primarily an electricity-export project. It is a compute-export project.

The Labrador coast model is based on:

1. Local hydro or renewable electricity serving compute pads near the village.
2. Data containers located close to heat users rather than at a remote dam.
3. Waste heat recovered for public buildings, homes, domestic hot water, and seasonal greenhouse use.
4. Compute results exported by fibre rather than electricity exported over long high-voltage transmission.
5. Tenant workloads operated under a black-box model.
6. Community and host operations limited to physical infrastructure monitoring.

This approach allows the project to keep heat value local while sending only data and compute output to external customers.

---

## 3. Why connectivity matters

Connectivity is a critical enabling system for Kristal Farms because the business model depends on exporting digital work rather than moving bulk electricity.

The project avoids the conventional pattern of building long high-voltage lines from a remote generation site to southern load centres. Instead, it uses a shorter local electrical connection to serve compute pads in or near the village, then connects those pads to external markets through fibre.

The connectivity layer therefore has three roles:

1. **Tenant compute export**  
   Moving tenant data, model outputs, batch results, control-plane traffic, monitoring signals, and customer-facing services between the Labrador coast site and external networks.

2. **Site operations**  
   Supporting the Network Operations Center, remote monitoring, maintenance access, alarms, telemetry, change control, and incident response.

3. **Community value**  
   Improving local network resilience and enabling service extensions for community facilities such as the clinic, school, municipal office, emergency services, or project governance offices where appropriate.

The fibre system should be treated as mission-critical infrastructure, not as a secondary utility.

---

## 4. Connectivity architecture

### 4.1 Regional trunk

The preferred architecture is a high-capacity fibre trunk from the site toward a regional network hub, such as Goose Bay or another validated southbound aggregation point.

The regional trunk should be designed for:

- high-capacity data transport;
- physically protected routing where feasible;
- clear ownership and maintenance responsibility;
- defined repair commitments;
- documented splice, patch, and access procedures;
- future capacity expansion;
- compatibility with Dense Wavelength Division Multiplexing, where justified by scale.

The trunk should be validated before a pilot pad is commercially committed. A project can begin with limited capacity, but the expansion pathway must be clear before larger tenant commitments are made.

### 4.2 Network Operations Center

Kristal Farms should include a small Network Operations Center at the port site or village-edge infrastructure yard.

The NOC is the operational control point for:

- fibre termination;
- optical distribution frames;
- patching;
- routing and switching;
- environmental monitoring;
- link monitoring;
- alarm handling;
- secure remote access;
- change control;
- incident coordination;
- physical access logs;
- community dashboard feeds.

The NOC should have redundant power feeds where feasible, backup power for critical network equipment, controlled access, and a documented operating procedure for maintenance windows and emergency interventions.

### 4.3 Local distribution

From the NOC, local fibre feeders connect to:

- compute pads;
- the project operations office;
- the heat plant / heat-exchanger station if separate;
- public dashboard systems;
- relevant community facilities, where part of the agreed benefit package.

Each compute pad should receive a clearly defined network handoff. The preferred design is dual A/B connectivity per pad, with each path terminating on separate switches or logically independent ports. Where practical, routing diversity should be introduced to reduce single-point failure risk.

### 4.4 Pad-level handoff

The standard pad handoff should include:

- labelled fibre ports;
- physical demarcation point;
- tenant-side patch responsibility;
- host-side patch responsibility;
- accepted connector types;
- bandwidth allocation or committed capacity;
- monitoring boundary;
- failover behavior;
- escalation contacts;
- maintenance-window process.

The handoff should be simple enough for modular deployment, but strict enough to support auditability and SLA enforcement.

---

## 5. Black-box tenancy model

### 5.1 Definition

Black-box tenancy means the host operates the site infrastructure around the tenant container without entering the tenant’s data, software, or internal compute environment.

The tenant container is treated as an opaque operational unit. Kristal Farms provides the pad and services up to the agreed interface. The tenant operates everything inside that boundary.

The host may meter power, cooling, heat transfer, link status, and aggregate bandwidth. The host may not inspect tenant content, tenant datasets, model weights, application logs, packet payloads, proprietary code, or business logic.

### 5.2 Why the model is necessary

The model is necessary because Kristal Farms serves multiple stakeholder groups with different interests:

- compute tenants need confidentiality and commercial control;
- communities need transparent infrastructure and benefit reporting;
- investors need metered, auditable operations;
- utilities need safe electrical and thermal interfaces;
- telecom partners need clear network demarcation;
- governments need a credible privacy and accountability framework.

Black-box tenancy allows these interests to coexist. The host can prove that the site is operating safely and delivering community value without requiring access to private tenant workloads.

---

## 6. Boundary of responsibility

### 6.1 Kristal Farms / host responsibilities

Kristal Farms, or the designated site host/operator, is responsible for the physical and utility-side infrastructure, including:

- pad yard operations;
- physical access control;
- perimeter security;
- pad-level power delivery;
- power metering;
- cooling interface;
- heat export interface;
- fibre handoff;
- network availability monitoring;
- environmental alarms;
- fire and safety systems at the site boundary;
- site-level incident response;
- public dashboard data preparation;
- maintenance coordination;
- community-facing infrastructure reporting.

The host also coordinates with the heat system operator, fibre partner, utility partner, community bodies, and emergency services.

### 6.2 Tenant responsibilities

The tenant is responsible for the compute environment inside its black-box boundary, including:

- tenant-owned or tenant-controlled servers;
- operating systems;
- virtualization or orchestration stack;
- AI frameworks;
- model weights;
- application code;
- tenant data;
- access control inside the tenant environment;
- tenant encryption;
- tenant backup practices;
- tenant cybersecurity;
- tenant workload scheduling;
- tenant compliance obligations;
- tenant internal monitoring;
- tenant customer relationships.

If a tenant requires a higher security posture, such as hardware attestation, confidential computing, or additional isolation assurances, those requirements should be specified in the lease or SLA annex.

### 6.3 Shared responsibilities

Certain areas require shared operational coordination:

- maintenance windows;
- emergency shutdowns;
- fibre failover;
- pad turn-up and acceptance testing;
- heat-first operating constraints;
- environmental incidents;
- cybersecurity incident notification;
- physical access to a tenant container;
- lawful access requests, if any;
- decommissioning and end-of-lease removal.

These shared responsibilities must be documented before commercial operation.

---

## 7. What the host sees

The host only sees the infrastructure metrics required to operate the pad safely and reliably.

### 7.1 Power metrics

The host may monitor:

- kWh consumed;
- instantaneous kW;
- power factor;
- voltage;
- current;
- harmonics, where relevant;
- feeder status;
- breaker status;
- power-quality events;
- abnormal draw;
- pad energization status.

These metrics are required for billing, protection, system planning, and safe operation.

### 7.2 Cooling and heat metrics

The host may monitor:

- IT-loop supply temperature at the host interface;
- IT-loop return temperature at the host interface;
- cooling-loop flow;
- pressure;
- ΔT across the heat exchanger;
- heat transferred;
- pump status;
- valve position;
- alarm thresholds;
- thermal rejection status;
- heat delivered to buildings, storage, or greenhouse systems.

These metrics are required because heat recovery is part of the project’s community-value model.

### 7.3 Network health metrics

The host may monitor:

- link up/down status;
- aggregate bandwidth utilization;
- port status;
- optical signal level;
- packet loss at the service level;
- latency to defined test points;
- jitter for service-health purposes;
- failover events;
- routing availability;
- trunk availability;
- pad uplink availability.

The host may monitor aggregate network performance but not tenant content.

### 7.4 Safety and site metrics

The host may monitor:

- temperature alarms at the infrastructure interface;
- smoke/fire alarms;
- water leak alarms;
- door/contact alarms where agreed;
- yard access logs;
- camera coverage of external/shared areas;
- environmental alarms;
- physical tamper indicators;
- emergency stop status;
- maintenance logs.

These systems protect the site and community without giving the host access to tenant data.

---

## 8. What the host never sees

The host must not access, inspect, collect, or publish tenant-confidential data.

The host does not see:

- tenant application logs;
- tenant operating-system logs;
- tenant internal telemetry;
- tenant datasets;
- tenant model weights;
- tenant prompts;
- tenant outputs, except where the tenant deliberately publishes them;
- tenant code;
- tenant customer information;
- packet payloads;
- deep packet inspection results;
- sensitive metadata beyond aggregate service operations;
- contents of storage devices;
- contents of memory;
- tenant authentication systems;
- tenant business logic;
- tenant internal monitoring dashboards.

The host also does not convert tenant workloads into public Kristals or community knowledge outputs unless the tenant has explicitly opted in and the relevant governance body has approved the use of public or consented data.

---

## 9. Network privacy and traffic separation

### 9.1 No deep packet inspection

The network should be operated without deep packet inspection of tenant payloads. The host may perform service-level monitoring needed to verify whether the network is available and performing within agreed ranges, but tenant traffic content remains outside the host boundary.

### 9.2 Traffic segmentation

Tenant traffic should be separated from community, operations, and public-dashboard traffic.

Recommended segmentation includes:

- separate VLANs or equivalent logical segmentation;
- tenant-specific routing domains where required;
- firewall boundary at the agreed demarcation point;
- separate management plane for host infrastructure;
- no shared credentials between tenant and host systems;
- documented access-control lists;
- change-controlled patching and configuration.

### 9.3 Encryption

Tenants should be expected to encrypt their traffic end-to-end. Kristal Farms should not depend on host-side visibility into tenant data to provide network service.

The host’s obligation is to deliver physical and network connectivity to the agreed standard. The tenant’s obligation is to secure its own data and applications inside that network path.

---

## 10. Optional hardware attestation

Hardware attestation should be available as an optional contract feature, not a default requirement for every tenant.

Some tenants may require Trusted Execution Environments, confidential computing features, secure boot evidence, firmware attestation, or other proofs that the hardware environment is in a known state before workloads are deployed.

The recommended position is:

- standard tenancy uses black-box isolation, tenant encryption, and physical/network separation;
- higher-security tenancy may add hardware attestation by contract;
- attestation requirements must be specified before pad turn-up;
- attestation evidence should be visible to the tenant or an agreed auditor, not treated as a host right to inspect tenant data;
- attestation does not weaken the black-box boundary.

This approach keeps the base model simple while allowing high-security tenants to negotiate stronger controls.

---

## 11. SLA concept

### 11.1 Single standard service, with best-effort surplus compute

The preferred initial model is a single standard service level for each tenant up to its contracted power and connectivity limits.

The project should avoid multiple complex service tiers at the first stage. A tenant receives a guaranteed service envelope defined by:

- contracted power ceiling;
- cooling interface range;
- fibre handoff;
- pad access terms;
- safety rules;
- metering method;
- maintenance-window procedure;
- outage notification procedure;
- incident escalation procedure.

Surplus compute, including workloads linked to community Kristals or non-critical batch processing, may be offered on a best-effort basis outside the formal SLA.

### 11.2 SLA areas

A full SLA should cover:

1. **Power service**  
   Contracted capacity, metering, voltage tolerance, outage handling, planned maintenance, emergency curtailment.

2. **Cooling service**  
   Flow, supply/return temperature ranges, heat-exchanger interface, emergency thermal rejection, maintenance windows, alarm thresholds.

3. **Heat export**  
   Host right to recover heat, measurement of thermal energy, priority of community heat sinks, reuse → storage → reject operating rule.

4. **Connectivity**  
   Bandwidth, availability target, failover expectation, latency reporting, repair process, maintenance notices, demarcation point.

5. **Physical access**  
   Access authorization, escort rules, emergency access, tenant maintenance visits, site induction, safety compliance.

6. **Confidentiality**  
   Black-box boundary, prohibited host access, no packet inspection, no tenant-log access, aggregation/anonymization of public metrics.

7. **Reporting**  
   Tenant-facing reports, host operational reports, community dashboard fields, public aggregation rules.

8. **Incident response**  
   Escalation contacts, notification timelines, emergency shutdown rules, cybersecurity notification expectations, environmental incident coordination.

9. **End of lease**  
   Decommissioning, tenant hardware removal, data-bearing equipment responsibility, pad restoration, metering closeout.

### 11.3 Heat-first operating clause

The SLA should acknowledge the project’s heat-first operating principle. Heat recovered from tenant pads is part of the local community-benefit model.

However, this should be written carefully. The project should not promise unlimited compute curtailment or arbitrary host control over tenant operations. Instead:

- contracted tenant service remains protected within agreed limits;
- local heat demand and infrastructure safety are included in operating procedures;
- best-effort surplus workloads can be shaped around heat demand;
- emergency safety conditions may require curtailment;
- community heat reporting is based on aggregate thermal metrics, not tenant workload content.

---

## 12. Public dashboard and data aggregation

Kristal Farms should maintain a public-facing dashboard or scorecard that reports project value without exposing tenant information.

Connectivity and tenancy-related dashboard metrics may include:

- aggregate pad link uptime;
- trunk availability;
- average or p95 latency to defined regional test point;
- number of active pads;
- aggregate pad occupancy;
- total kWh consumed by pads;
- total useful heat delivered;
- heat utilization factor;
- MWh_th delivered by sink type;
- diesel avoided;
- fibre availability;
- number of local facilities connected;
- number of incidents and resolved maintenance events.

The public dashboard should never include tenant-specific workload data, tenant names without consent, tenant packet contents, tenant customer information, tenant model information, or proprietary performance details.

---

## 13. Acceptance testing

Before commercial operation, connectivity and black-box tenancy should pass acceptance tests.

### 13.1 Connectivity acceptance tests

Minimum tests should include:

- trunk link installed and tested;
- pad A/B fibre links validated;
- failover demonstrated;
- latency measured to agreed regional point;
- bandwidth tested to contracted level;
- optical signal levels documented;
- NOC monitoring active;
- alarm escalation tested;
- maintenance procedure tested;
- community/public dashboard feed tested.

### 13.2 Black-box acceptance tests

Minimum tests should include:

- host cannot access tenant application logs;
- host cannot inspect tenant packet payloads;
- tenant and community traffic are separated;
- host monitoring limited to agreed physical/network-health metrics;
- access-control process documented;
- physical access logs active;
- public reporting uses aggregation or anonymization;
- optional attestation workflow tested if required by tenant.

### 13.3 Heat-interface acceptance tests

Because the compute pad connects to the heat system, pad turn-up should also verify:

- cooling flow within range;
- supply/return temperatures within range;
- ΔT measured correctly;
- heat meter commissioned;
- emergency thermal rejection available;
- alarm thresholds configured;
- no hydraulic mixing between IT and building loops.

---

## 14. Security, compliance, and audit

### 14.1 Security posture

The project should use a layered security posture:

- physical security at the yard;
- controlled NOC access;
- labelled and logged fibre patching;
- change control for network configuration;
- tenant-controlled encryption;
- network segmentation;
- host-side monitoring limited to infrastructure;
- audit trail for host actions;
- emergency response procedure.

### 14.2 Annual audit

A yearly independent audit should review:

- black-box boundary compliance;
- no unauthorized access to tenant data;
- host monitoring scope;
- NOC access logs;
- fibre change logs;
- physical access logs;
- public reporting aggregation;
- heat-first operating compliance;
- incident records;
- corrective actions.

The audit should be designed to reassure tenants, community bodies, investors, and public partners.

### 14.3 Lawful access and data requests

Any lawful access request must be handled according to applicable law and the lease framework.

Because Kristal Farms is not the operator of tenant systems, the default position should be:

- the host does not hold tenant data;
- the host cannot disclose data it does not possess;
- requests related to tenant data should be directed to the tenant unless legally required otherwise;
- the host may disclose host-held physical records only where legally required;
- tenants should be notified where legally permitted.

This section should be reviewed by legal counsel before execution.

---

## 15. Community and tenant trust model

The project has two trust obligations:

1. **Tenant trust**  
   Tenants need assurance that their data, models, code, and business operations remain private.

2. **Community trust**  
   The community needs assurance that the project is safe, beneficial, transparent, and not hiding material infrastructure impacts.

The black-box model reconciles these obligations. Tenant details remain private, while community-facing infrastructure performance remains transparent.

The host can publicly report what matters to the community:

- heat delivered;
- diesel avoided;
- uptime;
- fibre reliability;
- jobs and training;
- local benefits;
- environmental performance;
- incident response.

The host does not need to reveal what tenants are computing.

---

## 16. Open design items

The following items should be resolved before final partner execution:

1. Confirm the regional fibre route and ownership structure.
2. Confirm whether the NOC is operated by Kristal Farms, a telecom partner, or a joint operating entity.
3. Confirm repair-time expectations for trunk outages and local fibre faults.
4. Define the initial bandwidth commitment per pilot pad.
5. Define A/B pad link architecture.
6. Define whether any community facilities receive fibre upgrades as part of the first phase.
7. Define public dashboard fields and aggregation rules.
8. Define tenant naming policy.
9. Define optional hardware attestation package.
10. Define annual audit scope and auditor.
11. Define physical access rules for tenant containers.
12. Define lawful-access procedure with counsel.
13. Define end-of-lease hardware removal and site-restoration process.

---

## 17. Partner decision ask

Partners reviewing this document are asked to help confirm:

1. Whether the proposed fibre route can support pilot and expansion phases.
2. Whether a local NOC at the port/village-edge site is feasible.
3. Which party should operate the fibre and NOC layer.
4. What bandwidth and latency profile is realistic for the first Nain deployment.
5. What SLA commitments are commercially supportable.
6. What community connectivity benefits can be included without overpromising.
7. What tenant confidentiality terms are required for bankable compute leases.
8. Whether optional hardware attestation should be offered in the first tenant contract or deferred to later phases.

---

## 18. Summary

Kristal Farms depends on a clear division between infrastructure and compute operations.

The host provides power, cooling, heat export, fibre, physical security, metering, and local transparency. The tenant controls hardware, software, models, data, and workloads inside the compute container.

This boundary makes the Labrador coast model more partnerable. It allows the project to prove community value through heat, fibre, jobs, and transparent metrics while preserving the confidentiality required by serious compute tenants.

The result is a practical operating model:

> export compute by fibre, not electricity;  
> recover heat locally, not waste it;  
> operate tenant containers as black boxes;  
> report infrastructure value transparently;  
> keep tenant data private.

---

## Internal source basis

This draft was prepared from the current Kristal Farms source corpus, especially the internal reference material on fibre/NOC architecture, the black-box tenancy Q&A, the heat-first/cost rationale, and the EC8 synthesis paper. This section can be removed before external distribution.
