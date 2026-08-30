# Local development

This document describes the intended developer experience once implementation code is added.

## Prerequisites

Expected tool classes:

- Git;
- container runtime with Compose support;
- Node.js package manager selected by the implementation repo;
- Python environment manager selected by the implementation repo;
- PostgreSQL client tools where useful;
- optional QGIS for GIS workflows.

Do not pin versions in this document; pin them in repository toolchain files so CI and local environments share the same source of truth.

## Expected startup flow

```text
1. clone repository
2. copy documented local environment template
3. start PostGIS and supporting services
4. run database migrations
5. load fixtures / Pass 8 development dataset
6. start API services
7. start Web application
8. run health and QA checks
```

A single top-level developer command should eventually orchestrate the normal local stack.

## Development data

Use explicitly labeled fixtures or imported research datasets. Never silently fall back from unavailable production data to invented demo values in screens that appear authoritative.

## AI-assisted development

AI coding agents must read root `AGENTS.md`, machine contracts, and relevant ADRs before generating implementation changes.
