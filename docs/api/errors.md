# API errors

## Shape

Use a consistent structured error response, for example:

```json
{
  "error": {
    "code": "SCENARIO_INVALID_ASSUMPTION",
    "message": "compute_max_mw must be non-negative",
    "details": {"field": "compute_max_mw"},
    "request_id": "..."
  }
}
```

## Principles

- stable machine-readable error codes;
- human-readable messages;
- field-level details for validation;
- no stack traces or secrets in public responses;
- request/trace IDs for support;
- 404 must not leak existence of restricted resources when policy requires concealment.
