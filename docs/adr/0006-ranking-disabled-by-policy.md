# ADR-0006 — Ranking disabled by policy

**Status:** accepted  
**Date:** 2026-08-30

## Context

Legacy site tiers exist in historical research, but current direction supersedes those rankings and requires unranked evidence screening.

## Decision

Represent ranking permission as versioned policy. Current value is `ranking_allowed: false`. UI, API, analysis, and publication QA must enforce it.

## Consequences

Legacy priorities remain available only as provenance. Future ranking requires an explicit methodology, governance decision, policy update, and superseding/related ADR.
