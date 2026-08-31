# Showcase

## Purpose

The Showcase is the public-first narrative mode of the Kristal Farms application.

## Characteristics

- minimal persistent controls;
- cinematic camera transitions;
- selective use of terrain and globe;
- synchronized map, diagrams, text, and key metrics;
- progressive disclosure of technical detail;
- a clear path into the professional Explorer.

## Recommended narrative structure

1. Northern energy context.
2. Remote communities and autonomous systems.
3. Existing renewable reference projects.
4. Constraint: existing grids are not assumed to provide multi-MW compute headroom.
5. Kristal Farms architecture: new generation → protected community interface → flexible compute → fibre.
6. Demonstration of evidence and open questions.
7. Transition to Explorer.

## Technical rule

Showcase scenes are configuration-driven. Camera positions, active layers, narrative copy IDs, selected entities, and animation parameters should be stored in story configuration rather than hard-coded across page components.

Example:

```yaml
id: architecture-reveal
camera:
  center: [-73.3, 58.4]
  zoom: 5.4
  pitch: 48
layers:
  visible:
    - communities
    - reference_projects
    - conceptual_energy_flow
focus_entity: REF-INNAVIK
panel: architecture-intro
```

## Observatory interaction language

Showcase shares the [Map observatory interaction](../frontend/map-observatory-interaction.md) language with Explorer, but may use cinematic camera motion, temporary terrain/globe emphasis, and screen-space relation graphics. These effects must preserve evidence semantics and must not create synthetic geographic infrastructure.
