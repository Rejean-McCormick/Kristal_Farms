# Environments

## Development

Local developer environment. May use seeded/sample data. Never assumes production credentials.

## Staging

Production-like integration environment used to test migrations, ingest pipelines, publication, authentication, and release candidates.

## Production

Public and authorized professional services.

## Data separation

Development/test fixtures must be clearly marked. Production data should not be copied to lower environments unless policy explicitly permits it and sensitive fields are handled appropriately.

## Configuration

Environment-specific configuration belongs in environment variables, secret/config stores, or deployment manifests. Architecture and catalog defaults remain version-controlled.
