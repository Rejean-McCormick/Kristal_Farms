# Documentation index

This documentation is the operational contract for Kristal Farms.

## Read in this order

1. [Product vision](product/vision.md)
2. [Architecture overview](architecture/overview.md)
3. [Kristal Farms domain principles](domain/kristal-farms-principles.md)
4. [Data model](data/data-model.md)
5. [Evidence model](data/evidence-model.md)
6. [Layer catalog](frontend/layer-catalog.md)
7. [API overview](api/overview.md)
8. [Deployment architecture](architecture/deployment.md)
9. [Implementation plan](roadmap/implementation-plan.md)

## Documentation philosophy

The repository separates three kinds of documentation:

- **Normative:** rules the software and data must obey.
- **Descriptive:** how the current implementation works.
- **Decision records:** why a durable technical choice was made.

Normative documents use terms such as **MUST**, **MUST NOT**, **SHOULD**, and **MAY** intentionally.

## Machine-readable contracts

The `contracts/` directory contains schemas and policy files intended to be consumed by code, tests, CI, and AI coding agents. Human documentation and machine contracts must remain consistent.
