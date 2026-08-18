# Secure Compute and Black-Box Tenancy

Kristal Farms separates **running the physical infrastructure** from **accessing the tenant's computation**.

## The black-box boundary

The host provides and operates:

- power;
- cooling interface;
- heat export;
- fibre handoff;
- physical security;
- metering;
- alarms;
- infrastructure monitoring;
- maintenance coordination.

The tenant controls:

- servers and accelerators;
- operating systems;
- software;
- models and weights;
- datasets;
- application logs;
- encryption;
- workload scheduling;
- internal cybersecurity.

The host may monitor the physical quantities required to operate the infrastructure — such as power, temperatures, flow, heat transfer, link status and aggregate bandwidth — but the model explicitly excludes host access to tenant datasets, proprietary code, model content, application logs or packet payloads.

## Higher-assurance options

The documentation also proposes optional stronger security configurations, including:

- hardware attestation;
- confidential computing;
- stronger physical/network isolation;
- controlled-access brownfield sites;
- possible decommissioned-mine sites.

Mine-based compute is an **exploratory secure-site archetype**, not the baseline village architecture. Mine sites would require dedicated geotechnical, ventilation, fire/life-safety, flooding, remediation, power, fibre and economic studies.
