# Data release versioning

## Separate versions

Track independently:

- application version;
- database migration version;
- data release version;
- model/scenario-engine version;
- policy version.

## Suggested data release format

A date-based release is appropriate during research, for example:

```text
2026.08.30-r1
```

If formal semantic compatibility requirements emerge, a semantic version can be introduced later.

## Immutability

Published release identifiers must be immutable. Corrections create a new release.

## Scenario linkage

Every persisted scenario result must record the data release or dataset snapshot and model version used to produce it.
