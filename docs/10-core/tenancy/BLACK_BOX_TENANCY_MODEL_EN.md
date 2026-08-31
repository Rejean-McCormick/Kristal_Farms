# Kristal Farms — Tenant-Controlled Encrypted Environment

**Status:** Current reference commercial/security model (C1)  
**Commercial shorthand:** Black-box tenancy

## Model

Kristal Farms may lease serviced compute sites or pads while the tenant retains digital sovereignty over the systems placed behind the service boundary.

Kristal Farms can provide:

- power and metering;
- cooling interface;
- fibre/network handoff;
- physical security and controlled access;
- logistics and maintenance access;
- facility/service telemetry and SLA measurement.

The tenant can retain control of:

- hardware and accelerator configuration;
- operating systems and orchestration;
- models, datasets and applications;
- identities, credentials and internal logs;
- cryptographic keys and secrets.

## Confidentiality promise

The normal operating model is **content-blind by design**. Kristal Farms does not require routine access to private models, datasets, prompts, outputs or decrypted application traffic in order to lease the infrastructure.

Counterparty eligibility is established before access through jurisdictional and organizational due diligence. Compliance during tenancy relies on contract, externally verifiable information and lawful process, not hidden inspection of encrypted workloads.

## Boundary

Black-box tenancy does not eliminate:

- metering;
- facility telemetry;
- physical safety controls;
- shared-network protection;
- sanctions/export-control obligations;
- valid legal process;
- tenant responsibility for its own systems.

The governing phrase is:

> **Kristal Farms operates the infrastructure. The tenant controls the compute.**

See:

- `docs/00-control/INTERNATIONAL_TENANT_GOVERNANCE.md`
- `docs/security/TENANT_CONFIDENTIALITY_BOUNDARY.md`
- ADR-0021 and ADR-0022
