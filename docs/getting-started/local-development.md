# Local development

This document describes the local developer workflow and the separation between research, data-platform and product work.

## Prerequisites

Expected tool classes:

- Git;
- container runtime with Compose support;
- Node.js package manager selected by the implementation repo;
- Python environment manager selected by the implementation repo;
- PostgreSQL client tools where useful;
- optional QGIS for GIS workflows.

Do not pin versions in this document; pin them in repository toolchain files so CI and local environments share the same source of truth.

## Choose the workspace first

Before running code, identify the system being changed:

- exploratory investigation → `research/`;
- reproducible ingestion/validation/publication → `pipelines/`, `database/`, `contracts/`, `packages/`, `data/`;
- Observatory/product UI → `apps/web/`;
- API/tiles → `services/`.

Do not make the Web application execute a research script to obtain data. Promote data first, then consume the governed artifact/API.

## Expected startup flow

```text
1. clone repository
2. copy documented local environment template
3. start PostGIS and supporting services
4. run database migrations
5. load `data/fixtures/current` or another explicitly selected development dataset
6. start API services
7. start Web application
8. run health and QA checks
```

A single top-level developer command should eventually orchestrate the normal local stack.

## Development data

Use explicitly labeled fixtures or imported research datasets. Never silently fall back from unavailable production data to invented demo values in screens that appear authoritative.

## AI-assisted development

AI coding agents must read root `AGENTS.md`, machine contracts, and relevant ADRs before generating implementation changes.

### Observatory-only quick start

The current vertical slice can run against the checked-in immutable public release without starting PostGIS/services:

```bash
cd apps/web
npm install
npm run dev
```

Open `http://localhost:3000`. This development bridge reads `data/publish/current` and the stable layer catalog package server-side. It does not read `research/`, `pipelines/`, `data/raw/` or application fixtures at runtime.
