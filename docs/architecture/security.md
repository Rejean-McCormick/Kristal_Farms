# Security architecture

## Data classifications

```text
PUBLIC
PARTNER
INTERNAL
RESTRICTED
```

Every dataset/layer must have a classification.

## Publication boundary

The public artifact generator must filter restricted content before writing PMTiles, GeoJSON, GeoParquet, COG, or metadata bundles. Frontend hiding is not access control.

## Authentication

Use standards-based OIDC for authenticated modes. Avoid building a custom identity system.

## Authorization

Permissions may apply to:

- collections;
- attributes;
- downloads;
- scenarios;
- annotations;
- write operations;
- administrative configuration.

## Database roles

At minimum separate:

- migration/admin role;
- service read/write role;
- tile read role;
- OGC read role;
- analyst/QGIS roles;
- publication pipeline role.

## Secrets

No secrets in Git. Environment-specific credentials belong in a secret manager or protected CI environment.

## Sensitive spatial data

Where community, cultural, environmental, infrastructure, or partner data requires reduced spatial precision, create an explicitly generalized/redacted publish representation rather than simply removing fields in the UI.

## Tenant-controlled encrypted environments

Tenant operation is content-blind by design unless a separately contracted managed service explicitly changes the logical-access boundary. Kristal Farms should not require routine application-content access, private model/dataset inspection, operator key escrow or a standing decryption backdoor.

The provider may retain purpose-limited telemetry needed for power, cooling, physical security, shared network availability/security, metering and SLA operation. See `../security/TENANT_CONFIDENTIALITY_BOUNDARY.md`.

## Counterparty security boundary

Responsible-tenancy controls are performed through legal-counterparty identification, beneficial ownership/effective control, sanctions/trade screening, contract and periodic re-review. They are not implemented by defeating tenant encryption.
