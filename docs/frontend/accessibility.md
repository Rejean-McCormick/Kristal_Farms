# Accessibility

The visual impact of the application must not depend on excluding keyboard, low-vision, or screen-reader users.

## Requirements

- keyboard-accessible major controls;
- meaningful focus order;
- visible focus states;
- non-color encoding for statuses;
- sufficient contrast for text/controls;
- reduced-motion option for cinematic transitions;
- textual equivalent for essential map-derived facts;
- accessible names for layer controls and inspector actions.

## Map limitations

Maps are inherently difficult for assistive technologies. Provide searchable tables/inspectors for important datasets so core information is not available only by pointing at a geometry.

## Animation

Respect `prefers-reduced-motion`. Important information should remain available when animations are reduced or disabled.
