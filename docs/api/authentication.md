# Authentication and authorization

## Public mode

Showcase and explicitly public Explorer collections require no sign-in.

## Authenticated mode

Use OIDC-compatible authentication for partner/internal access.

## Authorization

Authorization decisions are server-side and may be based on:

- role;
- organization/tenant where later required;
- collection classification;
- action;
- scenario ownership/sharing state.

## Tokens

Do not place long-lived tokens in URLs or client storage when avoidable. API and tile services must validate access independently for non-public resources.
