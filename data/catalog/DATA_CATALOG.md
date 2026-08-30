# Data Catalog

The active data tree is organized by **role**, not by research chronology. Historical snapshots are retained under `archive/research-snapshots/`.

## Active canonical fixtures

`data/fixtures/current/` contains the application-oriented canonical fixture set used by validators and local development. It separates physical entities, evidence, observations, scenarios and system configuration.

Important rules:

- evidence may legitimately have no geometry;
- hydrometric station points are not river, dam or basin geometry;
- external reference projects are not Kristal Farms candidates;
- planning margin is not validated compute hosting capacity;
- ranking remains disabled.

## Active processed data

`data/processed/current/` contains normalized research and scenario outputs used to build releases. These files are intermediate products, not the operational source of truth.

## Active public release

`data/publish/current/` contains publishable, immutable-style release artifacts for Showcase/Explorer integration, including communities, hydrometric stations, evidence summaries and the economic sensitivity frontier.

Public release artifacts must never expose restricted data or silently promote legacy rankings, assumptions or approximate geometry into verified facts.

## Examples

- `data/examples/hydrology/` contains synthetic or demonstrative hydrology fixtures used for tests and examples.
- `data/examples/cartography/` contains design references.

Examples are not project evidence.

## Raw and historical data

Raw source acquisitions and older research snapshots are retained for reproducibility and provenance. They are not application-domain models and should not be imported directly into the public interface without normalization, validation and source review.
