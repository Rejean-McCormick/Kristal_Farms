# Kristal Farms application data model — Pass 11 foundation

Pass 11 implements the first executable subset of the architecture v0.1.

## Refinements

1. `core.entity` becomes the canonical identity supertype.
2. `core.natural_feature` is added for rivers, watersheds and reaches.
3. Source/evidence/observation are normalized and many-to-many evidence-source relations are explicit.
4. Screening dimensions are status/evidence/open-question records, not numeric scores.
5. Extraction windows/jobs move to `system.ingestion_job` instead of pretending to be domain layers.
6. Public web layers come from `publish` views.

The current fixture contains 24 river natural features and 24 WSC monitoring-station assets. Only WSC station points have physical geometry in the canonical fixture.

7. Pass 10 service/schema registry records migrate to `system.dataset_schema`; operational extraction attempts/windows migrate to `system.ingestion_job`.
