# ADR-0022 — Responsible-tenancy controls are counterparty-based, not content-inspection-based

**Status:** accepted  
**Date:** 2026-08-31

## Context

Kristal Farms intends to operate internationally while preserving the right to decline commercial relationships that do not meet project values, governance or risk criteria. Tenant environments are also intended to remain encrypted and content-blind to routine operator access.

## Decision

Responsible international tenancy will be governed primarily through:

1. jurisdictional eligibility;
2. legal-counterparty identification;
3. beneficial-ownership/effective-control review;
4. sanctions/export-control screening;
5. proportionate responsible-business due diligence;
6. contractual representations, covenants and termination rights;
7. periodic re-review based on external evidence and control changes.

The project will use categorical states (`ELIGIBLE`, `ENHANCED_DUE_DILIGENCE`, `SUSPENDED`, `INELIGIBLE`) rather than a numerical ethics score.

United States-based or United States-controlled counterparties are ineligible for tenant, anchor-offtaker and tenant-operator roles under the current owner-directed policy. This decision does not itself create a technology-origin embargo.

## Consequences

- Screening records must identify the specific legal entity, control structure, evidence and date.
- Country-level indicators are inputs, not automatic determinations about organizations or people.
- Reseller/subtenant structures require pass-through eligibility controls.
- Policy enforcement must not depend on defeating tenant encryption.
- A future change to the United States exclusion requires an explicit project-control decision.
