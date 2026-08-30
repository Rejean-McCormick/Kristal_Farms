# State and permalinks

## Shareable state

A professional user should be able to send a link that reconstructs the analytical view.

Recommended URL-state fields:

- mode;
- center/zoom/bearing/pitch;
- selected entity ID;
- visible layer IDs;
- timeline position/range;
- filter state;
- compare selections where not sensitive.

## Privacy

Never encode restricted scenario inputs, private notes, access tokens, or confidential entity names into shareable URLs.

## Stability

Use stable entity and layer IDs. URL schemas should be versioned if major changes occur.

## Showcase

Narrative scene URLs may use compact scene IDs and derive the rest from versioned story configuration.
