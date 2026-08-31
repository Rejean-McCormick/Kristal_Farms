# ADR-0021 — Tenant environments are content-blind by design

**Status:** accepted  
**Date:** 2026-08-31

## Context

Kristal Farms may lease serviced compute sites/pads while tenants retain control of hardware/software, models, data and keys. The project also intends to select commercial counterparties according to jurisdictional and responsible-business criteria.

A design that attempted to enforce commercial values through routine inspection of encrypted tenant content would conflict with the tenant-sovereignty proposition, create additional security/privacy risk and make the stated black-box model misleading.

## Decision

Normal Kristal Farms operations will be **content-blind by design**.

Kristal Farms will operate shared physical services and minimum necessary service telemetry without requiring routine access to tenant application content, private models/datasets or decryption keys.

No default operator key escrow, covert content monitoring or standing decryption backdoor will be required as a condition of tenancy.

Counterparty policy is enforced through admission/due diligence, contract, externally verifiable information and lawful process rather than hidden workload inspection.

## Consequences

- Tenant confidentiality becomes a core commercial/security boundary.
- Kristal Farms cannot claim to verify private encrypted workload content.
- Infrastructure telemetry remains available for power, cooling, physical security, networking, billing and SLA operation.
- Managed services that require logical access must be separately contracted and explicitly scoped.
- Legal requests are handled according to what Kristal Farms actually possesses or controls; the architecture should not create unnecessary standing access.
