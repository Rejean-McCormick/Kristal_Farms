# Map observatory interaction

## Status

This document defines the interaction and visual-behavior specification for the Kristal Farms map experience shared by **Explorer** and **Showcase**.

The design language is called the **Observatory interaction language**. It borrows the calm, instrument-like qualities of astronomical observation interfaces without turning the application into decorative science fiction.

This document is normative where it uses **MUST**, **MUST NOT**, **SHOULD**, and **MAY**.

Related documents:

- [Explorer](../product/explorer.md)
- [Showcase](../product/showcase.md)
- [Cartography](cartography.md)
- [Design system](design-system.md)
- [Layer catalog](layer-catalog.md)
- [Accessibility](accessibility.md)
- [State and permalinks](state-and-permalinks.md)
- [Frontend architecture](../architecture/frontend.md)
- [Explorer data contract](../60-application-data/EXPLORER_DATA_CONTRACT.md)
- [ADR-014 — Integrated atlas uses relations, not synthetic geometry](../adr/0014-integrated-atlas-uses-relations-not-synthetic-geometry.md)

---

## 1. Product intent

The map is not a generic GIS canvas and not a futuristic decoration layer. It is an **instrument for observing territorial knowledge**.

The interaction model should communicate the following progression:

```text
WHERE?
  ↓
MAP OBJECT
  ↓
WHAT IS IT?
  ↓
ENTITY
  ↓
WHAT IS IT RELATED TO?
  ↓
RELATIONS
  ↓
WHY DO WE BELIEVE IT?
  ↓
EVIDENCE
```

The map is the entry point into the knowledge model, not the full knowledge model itself.

### 1.1 Core experience

The signature interaction sequence is:

```text
silence → detection → observation → investigation
```

- **Silence:** the map is calm and legible at rest.
- **Detection:** nearby interactive features respond subtly to pointer proximity.
- **Observation:** hover or focus reveals a compact factual summary.
- **Investigation:** selection opens persistent evidence, relations, observations, and provenance.

### 1.2 Design principle

The interface SHOULD reveal information progressively instead of rendering all labels, metadata, relationships, and evidence simultaneously.

The visual sophistication of the application MUST come from hierarchy, precision, state transitions, and data semantics—not from permanent glow, animation, or visual noise.

---

## 2. Relationship to the existing cartographic identity

The current Kristal Farms cartographic references establish a recognizable semantic palette and symbol language. The interactive application SHOULD preserve that identity while adapting it to a dark, screen-native environment.

Recommended continuity:

- turquoise remains a product/context accent;
- blue remains associated with hydrology;
- amber/orange remains associated with communities where the semantic token specifies it;
- green remains associated with energy/reference energy objects where the semantic token specifies it;
- hypothetical/scenario states remain visually distinguishable from observed or verified objects.

The interactive interface SHOULD transform the medium rather than replace the vocabulary:

```text
editorial map
paper + ink + symbols

        ↓

interactive atlas
terrain + darkness + signals
```

Colors MUST remain semantic tokens. Components MUST NOT hardcode ad-hoc colors to imply site quality, merit, attractiveness, or ranking.

The current machine-readable visual authority is `packages/shared/visual_semantics.json`. Where this document and that file differ, implementation MUST follow the machine-readable rule until both are intentionally changed in the same pull request.

Current canonical role rules include:

```text
community             circle
hydrometric_station   small_dot
external_reference    triangle
conceptual_corridor   panel_only
unknown_geometry      no_map_symbol
```

Current canonical evidence/status treatments include:

```text
verified      solid
supported     solid_light
scoped        outline
unverified    dashed_outline
conflicting   split_or_warning
unknown       question
```

---

## 3. Visual hierarchy

The active viewport SHOULD follow this order of attention:

1. selected or focused subject;
2. active technical layers;
3. labels required for interpretation;
4. hydrography and terrain context;
5. administrative/contextual geometry;
6. decorative effects.

### 3.1 Base map

The dark map SHOULD retain geographic materiality rather than use a uniform black background.

Recommended depth hierarchy:

```text
UI / selected information    highest luminance
active technical layer       high
hydrography                  medium-high
terrain/topography           medium-low
administrative boundaries    low
background                   lowest
```

The base map SHOULD make northern geography, coastlines, water, remoteness, and terrain legible without competing with active data.

### 3.2 Glow discipline

Permanent glow MUST NOT be applied to every object.

Glow/halo effects SHOULD be reserved for:

- pointer/focus proximity;
- active hover/focus;
- selected entities;
- temporary Showcase narrative emphasis.

If everything glows, glow no longer communicates state.

---

## 4. Primary screen composition

Explorer SHOULD allow the map to occupy most of the viewport.

Persistent controls SHOULD be limited to compact functional zones rather than a permanently dominant GIS sidebar.

A reference composition:

```text
┌─────────────────────────────────────────────────────────────────────┐
│ KRISTAL / NORTHERN ATLAS                         SEARCH   LAYERS     │
│ NUNAVIK · HYDROLOGY                                                │
│                                                                     │
│                               ·                                     │
│                      ·               ◇                              │
│                                                                     │
│             •                                                       │
│                                   ·                                 │
│                                                                     │
│    •                     •                            ▲              │
│                                                                     │
│ 58.70250, -68.52000                 Z 6.42     RELEASE 2026.08.30   │
└─────────────────────────────────────────────────────────────────────┘
```

The actual labels and release values are data-driven; the wireframe above is illustrative only.

### 4.1 HUD

A compact map HUD MAY expose:

- current geographic context;
- cursor/center coordinates;
- zoom level;
- active layer count;
- public release identifier;
- scale;
- north/bearing state.

HUD information SHOULD be factual and useful. Decorative telemetry with no meaning SHOULD NOT be added solely to create an “astro” appearance.

---

## 5. Map object state model

Interactive map features MUST have explicit UI states.

Minimum states:

```text
idle
proximity
hovered / keyboard-focused
selected
compared
```

A feature MAY also be visually dimmed as a derived presentation state when another object is selected, but `dimmed` is not a domain status.

### 5.1 Idle

Idle objects SHOULD remain clear but restrained.

```text
•
```

No permanent pulse is required.

### 5.2 Proximity

When a pointer enters a small interaction radius around a feature, the feature MAY enter a proximity state before a hover card is shown.

```text
◉
```

Recommended response:

- slightly increased luminance;
- thin outer ring or reticle;
- no camera movement;
- no persistent information panel.

This state SHOULD feel like detection, not selection.

### 5.3 Hover / keyboard focus

Hover or keyboard focus reveals a compact summary.

The feature SHOULD gain a clear but restrained focus treatment such as:

- an outer ring;
- a reticle;
- a short leader line when needed;
- increased contrast relative to nearby objects.

Hover/focus MUST NOT change the map camera.

### 5.4 Selected

Selection is persistent until replaced or dismissed.

Selected state SHOULD:

- remain visually stable after the pointer leaves;
- open or update the Entity Inspector;
- optionally reduce competing layer contrast slightly;
- serialize the entity ID to URL state where permitted.

Selection MAY cause a small camera adjustment when required to keep the subject visible beside the Inspector. It MUST NOT produce aggressive camera motion.

### 5.5 Compared

Compare mode SHOULD support at least two pinned entity IDs when the product flow enables comparison.

Compare styling MUST NOT imply a winner, score, rank, or preferred option.

---

## 6. Pointer proximity and hover behavior

### 6.1 Detection target

The visible symbol size and the pointer hit target are separate concerns.

Small technical points, especially hydrometric stations, SHOULD retain precise visual geometry while exposing a larger invisible interaction target.

The hit target SHOULD be large enough for reliable pointer acquisition without causing excessive overlap between nearby entities.

### 6.2 Hover delay

The application SHOULD use a short hover-intent delay before opening a card. A starting range of approximately **80–120 ms** is recommended for prototype tuning.

The delay is a UX tuning value, not a data contract.

### 6.3 Exit grace period

Hover cards SHOULD remain interactive long enough for the pointer to move from the map feature into the card without immediate dismissal.

The implementation SHOULD avoid flicker when crossing the feature/card boundary.

### 6.4 Overlapping candidates

When multiple features are within the hit region, selection SHOULD be deterministic.

Recommended ordering criteria:

1. rendered/topmost interactive layer;
2. shortest screen-space distance to pointer;
3. stable layer/entity ID as final tie-breaker.

The application MUST NOT resolve overlap by hidden site merit or opportunity ranking.

---

## 7. Hover card

The hover card is a **recognition surface**, not a full inspector.

It should answer quickly:

1. What is this?
2. What is its relevant current state?
3. Why is it relevant in the current context?
4. What is the geometry/evidence confidence I should understand immediately?

### 7.1 Content budget

A hover card SHOULD normally contain:

- object type;
- title/identifier;
- secondary geographic/context label;
- 2–4 high-value fields;
- evidence/geometry qualifier;
- selection affordance.

It SHOULD NOT render the complete entity record.

### 7.2 Example: hydrometric station

Illustrative structure:

```text
HYDROMETRIC STATION                       VERIFIED

02WB003
Natashquan River

ACTIVE

DRAINAGE AREA
15,400 km²

REGION
Côte-Nord / Minganie

──────────────────────────────────────────────
Official station position · Click to inspect
```

Values above are illustrative of card structure; rendered values MUST come from governed application data.

### 7.3 Example: community

Illustrative structure:

```text
COMMUNITY                                  APPROX.

AKULIVIK
Nunavik / Hudson coast

FIBRE
Operating

MARINE
Regional port-system context

ROAD
No intercommunity road link

──────────────────────────────────────────────
Reference point · not facility location
```

Community coordinates that are approximate reference points MUST NOT be presented as facility coordinates.

### 7.4 Placement

The hover card SHOULD choose an anchor direction based on available viewport space.

It SHOULD avoid:

- clipping against viewport edges;
- covering the selected feature when avoidable;
- covering critical controls;
- large pointer travel between the feature and card.

A leader line MAY be used when the card is displaced from its source feature.

---

## 8. Entity Inspector

The Entity Inspector is the primary investigation surface.

It MUST contain more than a generic map popup and SHOULD expose governed context, evidence, relations, observations, provenance, and unknowns as appropriate to the entity type.

### 8.1 Recommended width

On desktop Explorer layouts, a starting width in the approximate **380–460 px** range is recommended. Exact dimensions remain responsive design tokens.

### 8.2 Generic information architecture

Recommended generic sections:

```text
OVERVIEW
EVIDENCE
RELATIONS
```

Entity-specific sections MAY extend the model.

For example:

```text
hydrometric station
OVERVIEW · OBSERVATIONS · HYDROLOGY · EVIDENCE

community
OVERVIEW · INFRASTRUCTURE · RELATIONS · EVIDENCE
```

### 8.3 Evidence visibility

Evidence status SHOULD be visible before the user opens a dedicated evidence section.

Useful compact labels include concepts such as:

```text
VERIFIED
CONTEXTUAL
APPROXIMATE GEOMETRY
UNRESOLVED
```

Actual values MUST use governed status enums and data contracts rather than invented frontend-only truth states.

### 8.4 Unknowns

Unknown or unresolved information MUST remain explicit.

The Inspector MUST NOT silently omit an important unknown in a way that makes the record appear more complete than the evidence supports.

---

## 9. Evidence and uncertainty as visual language

Evidence quality and geometry precision are not opportunity quality.

They MUST be encoded independently from any site merit concept.

### 9.1 Non-color encoding

Statuses SHOULD have a geometric/stroke treatment that remains understandable without color.

A possible design family:

```text
●  verified / exact presentation where supported
◉  supported/contextual
○  scoped/reference
◌  approximate or unresolved presentation state
?  insufficient/unknown
```

These glyphs are a visual design direction, not a replacement for canonical status enums.

### 9.2 Approximate point geometry

Approximate community/reference points SHOULD look approximate.

A thin dashed or incomplete outer ring MAY be used to communicate that the point is a geographic reference rather than a precise facility location.

The Inspector or hover card SHOULD state the limitation textually as well.

### 9.3 Do not punish uncertainty

Unknown or unresolved data MUST NOT automatically be colored red.

Red commonly implies failure or negative evaluation and would incorrectly conflate evidence completeness with opportunity quality.

---

## 10. Symbol anatomy

A point symbol MAY communicate three layers of information without changing its apparent merit:

```text
core      = object family/type
ring      = evidence/geometry precision cue
state     = interaction cue
```

Example conceptual families:

| Object | Current core rule | Precision/evidence treatment |
| --- | --- | --- |
| Community | circle | outer ring may show approximate reference geometry |
| Hydrometric station | small dot; reticle may be added as interaction state | official geometry treatment when supported |
| External reference project | triangle | governed reference/evidence treatment |
| Conceptual corridor | panel only | no map symbol/line while current rule is active |
| Unknown geometry | no map symbol | expose through Inspector/search/context only |

Other object families use their catalog/design-system semantic token until a canonical role rule exists. Marker size MUST NOT be used as a hidden site-quality score.

---

## 11. Labels and progressive disclosure

The interactive atlas SHOULD render fewer permanent labels than an editorial poster map.

### 11.1 Label priority

At low zoom:

- major geographic context;
- selected/focused entity;
- only essential community labels.

At regional zoom:

- more community labels;
- selected technical features;
- contextual hydrography.

At technical zoom:

- station IDs and local technical labels MAY become available where collision handling permits.

### 11.2 Hover labels

Technical station identifiers and dense labels SHOULD prefer hover/focus disclosure over permanent map text when simultaneous rendering would cause clutter.

### 11.3 Selection emphasis

When an entity is selected, non-essential neighboring labels MAY reduce contrast. They MUST remain available through search/inspection and MUST NOT disappear in a way that removes required context.

---

## 12. Linear and polygon features

The observatory interaction model applies to more than points.

### 12.1 Rivers

Hovering/focusing a river MAY highlight the rendered feature and show a compact card with:

- canonical river name;
- related monitoring station count or selected station where supported;
- evidence/provenance summary;
- inspection affordance.

Example structure:

```text
RIVER
Natashquan River / Rivière Natashquan

HYDROMETRIC OBSERVATION
02WB003

EVIDENCE
Verified station metadata

Click to inspect hydrology
```

Rendered values and relations MUST come from canonical data.

### 12.2 Polygons

Polygons SHOULD use boundary/fill changes that preserve surrounding geography. Selection MUST NOT create the appearance of greater certainty than the source geometry provides.

---

## 13. Relations as constellations

Relations are central to the integrated atlas, but relations are not automatically geometry.

### 13.1 Rule

A relation without authoritative route/facility geometry MUST NOT be drawn as a geographic line merely to make the interface look connected.

This is a direct application of [ADR-014](../adr/0014-integrated-atlas-uses-relations-not-synthetic-geometry.md).

### 13.2 Inspector constellation

The preferred representation for non-geometric relationships is a small relation graph inside the Inspector.

Example:

```text
             FIBRE
               ○

MARINE ○       ◎       ○ ENERGY

               ○
            EVIDENCE
```

The center represents the selected entity. Satellites represent relation dimensions or related entities.

This graph is **topological UI**, not map geometry.

### 13.3 Screen-space constellation

Showcase MAY use temporary relation lines in screen space, anchored visually to a selected entity and UI labels.

Screen-space relation lines:

- MUST NOT be written into the map source as synthetic geographic geometry;
- MUST NOT be exported as a route or infrastructure feature;
- MUST disappear when the narrative/focus state ends;
- SHOULD be labeled or styled clearly enough to avoid confusion with actual infrastructure;
- MUST NOT be used to represent `conceptual_corridor` while the current `panel_only` rule is active.

### 13.4 Geographic relations with real geometry

When governed geometry exists for an actual route, network, or feature, it MAY be rendered geographically using its normal semantic layer style.

The existence of a relation alone is insufficient to create that geometry.

---

## 14. Conceptual corridor treatment

Conceptual corridor context requires special care because a connecting line can be misread as an asserted route.

### 14.1 Explorer

The current machine rule for `conceptual_corridor` is `panel_only`. Explorer MUST therefore use an ordered entity/context representation rather than a map line for conceptual corridor context.

Example:

```text
NORTHERN CORRIDOR CONTEXT

Akulivik
↓
Inukjuak
↓
Kuujjuaq
↓
Nain
↓
Hopedale

Conceptual relationship
No route geometry asserted
```

Related map entities MAY receive temporary focus emphasis while this view is active.

### 14.2 Showcase

The current `conceptual_corridor: panel_only` machine rule also applies to Showcase. A story MAY sequence camera focus across related entities, but it MUST NOT draw a connecting corridor trace while that rule is active.

A future screen-space narrative trace would require an explicit change to the governing visual-semantics contract and corresponding documentation/tests. It must never be introduced by frontend styling alone.

---

## 15. Cursor and focus reticle

Explorer MAY use a map-only reticle cursor to reinforce the instrument-like interaction model.

Example:

```text
    │
  ──┼──
    │
```

Near an interactive feature:

```text
    │
  ──◎──
    │
```

Requirements:

- custom cursor treatment MUST be limited to the map canvas;
- standard pointer/text cursors MUST remain available over controls and text;
- the interaction MUST remain usable without the custom cursor;
- keyboard focus MUST provide equivalent discovery and selection states.

---

## 16. Observation lens / mobile targeting

Hover does not exist on touch devices. The design language MUST have a touch-equivalent interaction.

A future or optional **observation lens** MAY provide a center-screen targeting mode:

```text
        │
     ───┼───
        │
```

As the user pans the map, the closest eligible feature to the lens becomes the focus candidate.

A tap or explicit Inspect action selects it.

The lens can also be useful for keyboard/gamepad-like navigation, but it MUST NOT become the only way to select a feature.

---

## 17. Camera behavior

Camera motion MUST be tied to clear user or narrative intent.

### Explorer

- hover/focus: **no camera movement**;
- click/select: minor recentering MAY occur to preserve subject + Inspector visibility;
- explicit “explore/focus” action: stronger transition MAY occur;
- camera MUST remain interruptible by the user.

### Showcase

Showcase MAY use cinematic camera transitions when they improve geographic understanding.

Showcase camera behavior remains configuration-driven as specified in [Showcase](../product/showcase.md).

### Motion timing

Exact transition durations are implementation tokens, not hard domain rules. As a starting direction:

- ordinary Explorer selection transitions SHOULD feel short and functional;
- Showcase scene transitions MAY be longer and cinematic.

All essential information MUST remain available with reduced motion enabled.

---

## 18. Motion language

Animation SHOULD represent a system response to user or narrative action.

Recommended transitions:

- outer ring drawing in on proximity/focus;
- hover card reveal;
- leader line reveal;
- Inspector panel transition;
- relation constellation assembling after explicit selection;
- temporary subject emphasis in Showcase.

Avoid:

- continuous marker pulsing;
- decorative particle fields;
- unrelated HUD movement;
- animated flows that imply measured direction, capacity, or precision when none exists.

`prefers-reduced-motion` MUST be respected.

---

## 19. Compare mode

Compare mode SHOULD present dimensions side by side without scoring.

Example:

```text
AKULIVIK                         NAIN

TELECOM
operating fibre                  unresolved backbone

MARINE
regional context                 scheduled service context

ENERGY
—                                remote diesel context

GEOMETRY
approximate                      approximate
```

The exact fields are entity/data dependent.

Compare mode MUST NOT:

- rank entities implicitly;
- sort by hidden merit;
- use “winner/loser” visual treatments;
- convert evidence completeness into opportunity quality.

Compare entity IDs MAY be stored in URL state where safe.

---

## 20. Explorer vs Showcase density

The Observatory language is shared, but density differs.

### 20.1 Explorer

Explorer prioritizes:

- stable projection and camera behavior;
- precise selection;
- search and filters;
- compact metadata;
- evidence/provenance;
- tables and export;
- predictable workstation layout.

### 20.2 Showcase

Showcase prioritizes:

- large geographic composition;
- fewer controls;
- progressive narrative disclosure;
- cinematic camera movement;
- temporary terrain/globe effects;
- temporary screen-space relation graphics.

Showcase MUST NOT weaken evidence semantics merely for visual drama.

---

## 21. Frontend component model

Recommended component structure:

```text
MapWorkspace
├── MapViewport
│   ├── BaseGeography
│   ├── HydrographyLayers
│   ├── CommunityLayers
│   ├── HydrometricLayers
│   ├── EnergyReferenceLayers
│   └── FocusEffects
├── MapHUD
│   ├── ContextHeader
│   ├── Search
│   ├── CoordinateReadout
│   └── LayerControls
├── HoverController
│   └── HoverCard
├── SelectionController
├── EntityInspector
│   ├── Overview
│   ├── Relations
│   ├── Evidence
│   └── EntitySpecificSections
└── CompareTray
```

This is a logical decomposition, not a required directory structure.

### 21.1 Rendering responsibility

MapLibre SHOULD render normal geographic feature layers directly.

React SHOULD own interface surfaces around the map, including:

- hover cards;
- Inspector;
- relation graph UI;
- compare surfaces;
- layer/search controls.

DOM map markers SHOULD NOT be the default mechanism for large or ordinary point layers.

### 21.2 deck.gl

deck.gl SHOULD remain optional for interactions or visualizations that justify a second rendering layer, such as:

- large analytical overlays;
- advanced relation/flow visualization;
- specialized 3D/aggregation work.

Basic communities, stations, and ordinary geographic features do not require deck.gl.

---

## 22. Feature state

MapLibre `feature-state` is the preferred mechanism for ephemeral visual interaction state on compatible rendered features.

Expected presentation states include:

```text
hovered
selected
compared
```

`dimmed` MAY be derived by style logic when another entity is selected.

These are UI states and MUST NOT be persisted as domain attributes.

### 22.1 Stable feature IDs

Layers using feature-state MUST expose stable feature IDs compatible with the rendering source.

Feature IDs SHOULD map cleanly to canonical entity IDs where practical.

---

## 23. Frontend state model

Recommended local UI state:

```ts
hoveredEntityId: string | null
selectedEntityId: string | null
compareEntityIds: string[]
activeInspectorSection: string
```

Implementation MAY use a more structured state machine, but transient hover state MUST remain local UI state.

Selected entity and safe compare IDs SHOULD participate in URL state as specified in [State and permalinks](state-and-permalinks.md).

Remote entity/evidence records remain server state and SHOULD use the frontend query/cache layer.

---

## 24. Data loading behavior

### 24.1 Hover path

Hover MUST be fast enough to feel immediate.

Information needed for the hover card SHOULD be available from:

- rendered feature properties;
- a small local/indexed entity summary cache;
- another preloaded lightweight representation.

Hover SHOULD NOT require a full entity/evidence API round trip for every pointer movement.

### 24.2 Selection path

Selection MAY fetch richer data from endpoints such as:

```text
GET /entities/{id}
GET /entities/{id}/evidence
GET /entities/{id}/screening
```

The Inspector SHOULD show a stable selected state while detailed data loads.

### 24.3 Stale and versioned data

The Inspector SHOULD make the active public/data release discoverable. Evidence timestamps and source-version information remain governed by the existing data contracts.

---

## 25. Layer catalog integration

The existing layer catalog already defines source, renderer, style token, inspector fields, evidence support, and feature-state behavior.

The first implementation SHOULD use those existing capabilities before expanding the machine schema.

### 25.1 Current configuration mapping

The generic interaction system can derive:

- whether a feature is inspectable from layer/catalog behavior;
- card title from `inspector.title_field`;
- card/Inspector fields from `inspector.fields`;
- evidence affordance from `inspector.evidence_enabled`;
- semantic styling from `display.style_token`.

### 25.2 Future schema extension

If layer-specific hover cards require declarative field subsets, a future catalog schema version MAY introduce explicit interaction/card configuration.

Illustrative only—not a current contract:

```yaml
interaction:
  hover: true
  select: true
hover_card:
  title_field: station_number
  subtitle_field: river_name
  fields:
    - status
    - gross_drainage_area_km2
    - region
```

This example MUST NOT be treated as valid production configuration until the machine schema and example contract are updated together.

---

## 26. Search and non-map access

Map discovery MUST NOT be the only way to reach important data.

Explorer SHOULD provide search and, where appropriate, table/list access so users can locate entities by:

- name;
- identifier;
- type;
- region/context;
- other governed searchable fields.

Selecting an entity from search or a table SHOULD produce the same Inspector state as selecting it on the map.

---

## 27. Accessibility

The Observatory interaction language MUST remain operable without precise pointer hover.

Requirements:

- major map actions keyboard accessible;
- focused map entities receive the same factual summary as hover;
- selection is possible without mouse hover;
- important facts exist in Inspector/table/search surfaces;
- focus state is visible without relying on color;
- evidence/uncertainty cues are textual as well as graphical;
- reduced motion is supported;
- hover cards do not contain information unavailable elsewhere;
- custom cursor effects are optional enhancements, not functional dependencies.

Touch layouts MUST provide a selection path that does not depend on hover.

---

## 28. Performance requirements

The interaction must feel like direct manipulation.

Implementation SHOULD:

- render ordinary feature layers in MapLibre rather than as many DOM markers;
- avoid React rerenders on every raw pointer event;
- throttle/debounce pointer queries appropriately;
- use feature-state for visual hover/selection when possible;
- keep hover-card data lightweight;
- defer rich evidence loading until selection;
- avoid expensive deck.gl layers when MapLibre is sufficient.

The application SHOULD be tested on representative lower-powered laptops, not only high-end development hardware.

---

## 29. Interaction event flow

Reference flow:

```text
pointer move
   ↓
query rendered interactive features
   ↓
resolve deterministic candidate
   ↓
set proximity/hover feature-state
   ↓
short hover-intent delay
   ↓
render HoverCard from local summary

click / Enter
   ↓
set selected entity
   ↓
serialize safe selection state
   ↓
open EntityInspector
   ↓
fetch entity + evidence + screening as needed
   ↓
render relations / provenance / observations
```

Leaving a feature clears transient hover state but MUST NOT clear a selected entity.

---

## 30. Testing

### 30.1 Unit/component tests

Test at minimum:

- deterministic hover candidate resolution;
- hover delay cancellation;
- card placement near viewport edges;
- selected state surviving pointer exit;
- selection from keyboard/search equivalent to map click;
- relation graph not generating synthetic geographic features;
- reduced-motion behavior;
- safe URL serialization of selected/compare IDs.

### 30.2 Visual regression fixtures

Curated deterministic fixtures SHOULD cover:

- idle map;
- point proximity;
- hover card for a community;
- hover card for a hydrometric station;
- selected community + Inspector;
- selected station + Inspector;
- approximate geometry treatment;
- verified vs hypothetical symbol treatment;
- relation constellation in Inspector;
- compare mode;
- reduced-motion version;
- narrow/mobile layout.

Visual review MUST include semantic correctness, not only pixel similarity.

### 30.3 Integration tests

At least one Explorer integration flow SHOULD verify:

```text
search entity
→ select
→ Inspector opens
→ evidence loads
→ relation shown
→ URL captures selection
→ reload reconstructs view
```

---

## 31. Acceptance criteria for the first Observatory implementation

A first implementation is successful when all of the following are true.

### Map behavior

- the map is visually calm at rest;
- hover/focus is discoverable without permanent animation;
- hover does not move the camera;
- selected state is persistent and visually distinct;
- labels remain legible without displaying all entity names simultaneously.

### Information behavior

- hover answers identity + key state + evidence/precision at a glance;
- click opens a richer Inspector rather than a larger popup;
- important unknowns are visible;
- approximate locations look and read as approximate;
- relations without geometry are not drawn as geographic infrastructure.

### Architecture

- ordinary layers are catalog-driven;
- ordinary map features are rendered by MapLibre;
- feature-state is used where appropriate;
- transient hover state is not persisted to the domain model;
- hover does not require full entity API requests;
- selection integrates with canonical entity/evidence APIs.

### Accessibility

- keyboard selection reaches equivalent information;
- touch has an explicit selection path;
- status is not communicated by color alone;
- reduced-motion mode preserves all essential information.

---

## 32. Implementation sequence

The Observatory language SHOULD be implemented incrementally.

### Stage A — Interaction foundation

Build first:

1. dark base map and semantic symbols;
2. stable interactive feature IDs;
3. proximity/hover feature-state;
4. hover card with intelligent placement;
5. persistent selection;
6. Entity Inspector shell;
7. keyboard/touch equivalent interaction.

This stage should prove the product signature before adding cinematic effects.

### Stage B — Evidence and relation depth

Add:

1. evidence/provenance summary in Inspector;
2. entity-specific Inspector sections;
3. approximate-geometry treatments;
4. Inspector relation constellation;
5. shareable selection state;
6. line/polygon inspection behavior.

### Stage C — Professional Explorer depth

Add:

1. compare mode;
2. advanced filters/timeline integration;
3. observation lens if user testing supports it;
4. richer keyboard navigation;
5. performance tuning for denser datasets.

### Stage D — Showcase expression

Add selectively:

1. cinematic camera scenes;
2. temporary screen-space constellations;
3. narrative focus traces;
4. terrain/globe transitions;
5. stronger but still semantic motion treatments.

---

## 33. Explicit anti-patterns

Do not implement the Observatory language as:

- every marker pulsing continuously;
- neon outlines on every layer;
- star-field or particle decoration unrelated to data;
- synthetic geographic lines for non-geometric relations;
- auto-zoom on hover;
- full metadata dumps in hover cards;
- marker size as hidden opportunity score;
- red = unknown / green = good;
- separate interaction logic hard-coded for every ordinary layer;
- DOM markers for all data points by default;
- animation that suggests measured flows when only conceptual relations exist;
- a custom cursor that makes ordinary controls harder to use.

---

## 34. Design review checklist

Before merging a new interactive map behavior, reviewers should ask:

### Semantics

- Does this graphic imply geometry, precision, capacity, ranking, or causality that the data does not support?
- Is evidence quality being confused with opportunity quality?
- Is an approximate location visually honest?

### Interaction

- Does hover only reveal, while selection persists?
- Can the same information be reached by keyboard/touch/search?
- Does the user retain control of the camera?

### Visual hierarchy

- Is the selected subject clearly dominant?
- Is the base map quieter than active technical data?
- Are glow and motion reserved for state changes?

### Architecture

- Can the behavior be driven by the layer catalog and canonical entity IDs?
- Is transient UI state kept out of domain data?
- Is a non-geometric relation kept out of geographic sources?

### Evidence

- Can the user discover what supports the claim?
- Are unknowns and limitations visible?
- Is the active data/release context discoverable?

---

## 35. Summary

The Observatory interaction language should make Kristal Farms recognizable through restraint rather than spectacle.

Its core rules are:

1. **The map is calm until the user observes something.**
2. **Hover reveals; click investigates.**
3. **Evidence and uncertainty are visible design primitives.**
4. **Relations are not geography unless governed geometry exists.**
5. **MapLibre owns ordinary geographic rendering; React owns investigation UI.**
6. **Motion responds to intent; it does not decorate idle state.**
7. **Explorer remains precise and analytical; Showcase may be cinematic.**
8. **Accessibility and touch are first-class, not fallback modes.**
9. **No visual treatment may imply site ranking while ranking is disabled.**
10. **The visual system should feel like a territorial observation instrument, not a generic GIS theme.**
