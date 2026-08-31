# Explorer

## Purpose

The Explorer is the professional workspace built on the same governed data used by the Showcase.

## Core capabilities

- layer catalog;
- dynamic legend;
- search;
- map selection;
- filters;
- temporal controls;
- evidence panel;
- metadata and provenance;
- compare mode;
- shareable URL state;
- export/download subject to permissions.

## Evidence-first behavior

Selecting a feature should reveal more than a popup. The primary inspector should answer:

- What is this object?
- Is it observed, referenced, hypothetical, or derived?
- What sources support it?
- When was it last verified?
- What is unknown?
- What data version is being viewed?

## Avoid

- silent ranking;
- traffic-light opportunity colors while ranking is disabled;
- exact-looking markers for approximate locations;
- derived capacity claims without methodology;
- UI-only permission hiding.

## Observatory interaction language

Explorer uses the shared [Map observatory interaction](../frontend/map-observatory-interaction.md) language: the map stays calm at rest, hover/focus performs lightweight recognition, and persistent selection opens the evidence-first Entity Inspector. Non-geometric relations are presented as UI relations rather than synthetic map geometry.
