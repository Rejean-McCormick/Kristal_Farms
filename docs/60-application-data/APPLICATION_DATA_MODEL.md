# Kristal Farms application data model

The application uses a canonical relational/geospatial model rather than treating each research file as a permanent map layer.

## Core refinements

1. `core.entity` provides a shared canonical identity.
2. `core.natural_feature` represents rivers, watersheds and research reaches.
3. Source, evidence and observation records are normalized and linked explicitly.
4. Screening dimensions are evidence/status/open-question records, not numeric scores.
5. Extraction windows and processing jobs live under `system.ingestion_job` rather than masquerading as domain geography.
6. Public Web layers are derived from `publish` views and immutable releases.

The current fixture contains 24 river natural features and 24 WSC hydrometric-station assets. Only the official station positions have physical geometry in the current canonical fixture; river and watershed geometry remains null until authoritative geometry is ingested and accepted.
