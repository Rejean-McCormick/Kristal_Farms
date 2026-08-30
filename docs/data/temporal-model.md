# Temporal model

Kristal Farms distinguishes **world time** from **knowledge time**.

## World/valid time

When the statement or object is true:

```text
valid_from
valid_to
```

Examples:

- project operating period;
- regulatory decision validity;
- planning period;
- infrastructure commissioning.

## Knowledge/provenance time

When Kristal Farms learned or recorded it:

```text
published_at
retrieved_at
observed_at
last_verified
created_at
updated_at
```

## Timeline UI

The map timeline should filter or style by valid time. It must not implicitly treat `retrieved_at` as the date the real-world state became true.

## Period labels

Planning periods such as `2025-2026` should be stored in a normalized form suitable for ordering, while preserving the source label for display.
