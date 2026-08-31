# Kristal Farms documentation

This documentation covers the **Kristal Farms infrastructure project** and the application/data system used to explain, research and evaluate it.

## Read in this order

### Project

1. [Project state](00-control/PROJECT_STATE.md)
2. [Strategic principles](00-control/STRATEGIC_PRINCIPLES.md)
3. [Reference architecture — English](10-core/Kristal_Farms_Reference_Architecture_EN.md) or [français](10-core/Architecture_de_reference_Kristal_Farms_FR.md)
4. [Deployment strategy — English](10-core/deployment/DEPLOYMENT_STRATEGY_EN.md) or [français](10-core/deployment/STRATEGIE_DE_DEPLOIEMENT_FR.md)
5. [Corridor dossier strategy](00-control/CORRIDOR_DOSSIER_STRATEGY.md)

### Application and data

1. [Application product vision](product/vision.md)
2. [Architecture overview](architecture/overview.md)
3. [Kristal Farms domain principles](domain/kristal-farms-principles.md)
4. [Data model](data/data-model.md)
5. [Evidence model](data/evidence-model.md)
6. [Map observatory interaction](frontend/map-observatory-interaction.md)
7. [Layer catalog](frontend/layer-catalog.md)
8. [API overview](api/overview.md)
9. [Implementation plan](roadmap/implementation-plan.md)

## Documentation authority

The active authority order is defined in [Document Authority](00-control/DOCUMENT_AUTHORITY.md). In short:

- current project-control documents govern intent and interpretation;
- current reference architecture governs the physical/commercial model;
- source evidence governs factual claims within its actual scope;
- assumptions remain assumptions;
- archived material never silently overrides active state.

## Documentation philosophy

The repository separates three kinds of active documentation:

- **Normative:** rules the project data/software must obey.
- **Descriptive:** how the current project/application implementation works.
- **Decision records:** why a durable technical choice was made.

Normative documents use terms such as **MUST**, **MUST NOT**, **SHOULD**, and **MAY** intentionally.

## Machine-readable contracts

The `contracts/` directory contains schemas and policy files intended to be consumed by code, tests, CI and coding agents. Human documentation and machine contracts must remain consistent.

## Long-horizon material

Optional human-infrastructure, learning and education concepts are isolated under [Long-Horizon Concepts](70-long-horizon/README.md). They are not prerequisites or commitments for the first energy/compute deployment.
