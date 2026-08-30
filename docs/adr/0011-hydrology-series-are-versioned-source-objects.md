# ADR-011 — Hydrology series are versioned source objects

**Status:** Accepted

## Decision

Daily/monthly hydrology is represented by `research.observation_series` plus observations, with source release, retrieval time and raw checksum. Series are not embedded in river metadata.

## Consequence

The same station can safely retain observations from multiple releases or agencies without silent overwrite.
