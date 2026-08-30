# Application release runbook

## Before release

1. CI green.
2. Database migrations reviewed and tested in staging.
3. Catalog schema validation passes.
4. Security-sensitive changes reviewed.
5. Visual regression checked for Showcase-critical scenes.
6. API contract changes documented.
7. Release notes prepared.

## Deploy

1. Apply compatible DB migrations according to migration plan.
2. Deploy backend services.
3. Verify health/readiness.
4. Deploy Web application.
5. Run smoke tests.
6. Verify public release artifact references.

## Rollback

Application rollback must account for database compatibility. Never assume reverting the Web container is sufficient after a destructive schema migration.
