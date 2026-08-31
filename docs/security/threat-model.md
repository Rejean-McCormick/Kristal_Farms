# Threat model

## Assets to protect

- restricted coordinates and infrastructure details;
- partner/internal research sources;
- user scenarios and annotations;
- credentials/tokens;
- data integrity/provenance;
- public technical credibility.

## Representative threats

### Publication leakage

Restricted fields/geometries accidentally included in public PMTiles or exports.

Mitigation: explicit publish views, classification filters, release QA, artifact inspection.

### Authorization bypass

User requests internal entity or export directly through API/tile endpoint.

Mitigation: server-side authorization at every non-public service boundary.

### Data poisoning / incorrect import

Automated research/import modifies canonical values incorrectly.

Mitigation: raw/staging separation, provenance, review states, QA, immutable release history.

### Semantic misrepresentation

A visualization turns planning margin into apparent compute capacity or hypotheses into facts.

Mitigation: domain-policy tests, catalog semantics, inspector labels, ADR/policy enforcement.

### Credential exposure

Secrets committed or exposed client-side.

Mitigation: secret management, scanning, least-privilege roles, rotation procedures.

### Tenant confidentiality boundary failure

Operator tooling, support access or incident response creates unnecessary access to private tenant models, datasets, payloads or keys.

Mitigation: content-blind-by-design architecture, tenant-controlled keys, least-access support, physical/logical separation, access logging and no default key escrow.

### Counterparty-policy bypass

A prohibited or unreviewed party obtains capacity through nominee ownership, undisclosed control, reseller/subtenant chains or material ownership changes.

Mitigation: beneficial-ownership/effective-control review, sanctions/trade screening, contractual disclosure obligations, downstream eligibility controls and periodic re-review.

### False compliance assurance

Kristal Farms marketing implies that private encrypted workloads have been inspected or certified as ethically compliant even though the service is intentionally content-blind.

Mitigation: precise public wording, counterparty-based governance, explicit documentation of the visibility boundary and prohibition on unsupported workload-content claims.
