# Tenant Confidentiality and Content-Blind Operations Boundary

**Status:** Normative security/commercial boundary  
**Effective:** 2026-08-31

## Purpose

Kristal Farms is designed to operate shared physical infrastructure while tenants retain control of their private digital systems. The intended model is a **tenant-controlled encrypted environment**: the operator can run power, cooling, fibre, physical security and service telemetry without requiring routine access to tenant application content.

The commercial shorthand **black-box tenancy** refers to this boundary. It does not mean an ungoverned facility, immunity from law, or absence of infrastructure telemetry.

## Trust boundary

### Kristal Farms-controlled plane

Kristal Farms may control or operate, according to the service contract:

- electrical service and metering;
- curtailment interface;
- cooling/service-water interfaces;
- fibre handoff and shared network transport;
- shared facility and perimeter security;
- physical access coordination;
- environmental, power and facility telemetry;
- shared-infrastructure maintenance and incident response.

### Tenant-controlled plane

The tenant controls, unless a separate managed-service agreement explicitly states otherwise:

- server/accelerator configuration;
- operating systems and hypervisors;
- models and model weights;
- datasets and databases;
- prompts, application payloads and outputs;
- tenant identities and application authorization;
- encryption keys and secrets;
- internal application logs and private workload telemetry.

## Content-blind-by-design controls

Normal Kristal Farms operations **MUST NOT** require:

- disclosure or escrow of tenant decryption keys;
- routine access to plaintext application traffic;
- routine inspection of tenant files, datasets, prompts, model weights or outputs;
- installation of operator agents whose purpose is to inspect private application content;
- covert content-monitoring or a standing decryption backdoor;
- content inspection as the mechanism for enforcing commercial counterparty policy.

If a tenant voluntarily shares content for support, that content becomes a separately controlled support artifact and must not be generalized into routine access rights.

## Operational telemetry that remains permitted

Kristal Farms **MAY** process minimum necessary service telemetry, including:

- power draw, voltage/current quality and energy state;
- temperature, cooling demand, flow/pressure where applicable and environmental alarms;
- physical-entry events and security-system alerts;
- link state, aggregate bandwidth, routing/fault data and DDoS/security signals needed to protect shared infrastructure;
- service availability, maintenance, billing and SLA records.

Where network security controls are required, they SHOULD operate without decrypting tenant application payloads unless the tenant separately opts into a managed security service.

## Physical access

A black-box tenancy may still require lawful and contractually defined physical access for life safety, fire response, electrical isolation, cooling failure, facility protection or agreed maintenance.

Emergency physical intervention does not create a general right to access tenant logical systems or private content.

Physical custody and logical access should be separated where practical. Access events should be logged and subject to role-based authorization.

## Cryptographic boundary

Preferred design principles are:

- tenant-generated or tenant-controlled keys;
- no default Kristal Farms key escrow;
- encryption in transit across shared networks;
- encryption at rest for tenant-controlled storage where the tenant architecture supports it;
- hardware-backed isolation/confidential-computing features where commercially appropriate;
- documented key-recovery responsibility resting with the tenant unless a separate service explicitly changes that boundary.

Kristal Farms must not market "zero knowledge" or "confidential computing" unless the actual implementation satisfies the technical meaning of those terms. The safer general description is **content-blind operations with tenant-controlled encryption**.

## Compliance boundary

Kristal Farms performs **counterparty and jurisdictional due diligence** before and during the commercial relationship. It does not claim to validate the private substance of every computation.

Compliance controls therefore rely on:

- know-your-counterparty / beneficial-ownership review;
- sanctions and trade-control screening;
- contractual representations and covenants;
- externally verifiable events and lawful notices;
- facility/network abuse signals that do not require application-content decryption;
- suspension/termination rights where contract or law permits.

See `docs/00-control/INTERNATIONAL_TENANT_GOVERNANCE.md`.

## Legal requests

When a valid legal request is received, Kristal Farms should:

1. validate authority and scope with legal counsel where appropriate;
2. identify what data Kristal Farms actually possesses or controls;
3. minimize disclosure to the legally required scope;
4. notify the tenant where legally permitted;
5. document the response;
6. avoid creating a persistent decryption capability that did not previously exist.

This policy does not promise that a court, regulator or other lawful authority can never compel action. It promises that routine commercial operation does not depend on operator access to private tenant content.

## Incident response

Tenant incidents and shared-infrastructure incidents must be distinguished.

Kristal Farms is responsible for incidents within the shared-service boundary. A tenant remains responsible for incidents within its own systems unless a separate managed-service agreement says otherwise.

Cross-boundary incident support should use the least access necessary and should be tenant-authorized except where immediate physical safety or binding law requires otherwise.

## Public wording

Approved concise description:

> **Kristal Farms operates the infrastructure. The tenant controls the compute.**

Approved expanded description:

> **Tenant environments are designed to remain encrypted and content-blind to routine Kristal Farms operations. Kristal Farms governs access to its infrastructure through counterparty due diligence and contract, not by inspecting private models, datasets or application content.**
