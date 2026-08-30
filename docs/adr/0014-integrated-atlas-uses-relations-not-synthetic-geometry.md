# ADR-014 — Integrated atlas uses relations, not synthetic geometry

## Status
Accepted

## Context
The integrated atlas must connect rivers, communities, ports, telecom, energy and logistics even when exact facility/route geometry is absent.

## Decision
Use canonical entity relations and evidence/observations to create context. Do **not** create a map line or point solely to satisfy the frontend. Community points imported from legacy My Maps remain explicitly approximate centroids. Regional marine systems, ferry/fibre corridors and external projects may have `geometry = NULL`.

## Consequences
The Explorer can show badges and Evidence Panel context without inventing spatial precision. Map rendering becomes a projection of what has real geometry, not a requirement imposed on all knowledge.
