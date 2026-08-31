# Security policy

## Reporting

Do not disclose security vulnerabilities or restricted-data exposures through public issue content. Use the project's designated private security reporting channel once configured in the GitHub repository.

## Security-sensitive areas

Particular attention is required for:

- restricted geospatial data;
- partner/internal source documents;
- database credentials;
- OIDC configuration;
- public artifact generation;
- export/download authorization;
- scenario privacy;
- tenant confidentiality and cryptographic separation;
- provider/tenant logical-access boundaries;
- due-diligence records containing ownership/control or compliance information.

See [Security architecture](docs/architecture/security.md) and [Tenant Confidentiality Boundary](docs/security/TENANT_CONFIDENTIALITY_BOUNDARY.md).
