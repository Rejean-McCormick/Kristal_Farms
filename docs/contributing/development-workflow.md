# Development workflow

## Branching

Use short-lived feature branches and pull requests. Keep architecture and data migrations reviewable.

## Typical change sequence

1. Read relevant docs/ADRs.
2. Update or create contract/schema if needed.
3. Implement migration/domain logic.
4. Implement API/frontend behavior.
5. Add tests.
6. Update docs.
7. Run QA and lint/type checks.
8. Open PR using the repository template.

## Database changes

Never modify production schema manually without a recorded migration except emergency procedures explicitly documented afterward.

## Data changes

Research data changes require source/provenance updates and QA, not merely editing a map feature in frontend code.
