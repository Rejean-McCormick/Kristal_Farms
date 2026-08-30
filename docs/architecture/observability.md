# Observability

Track enough information to distinguish application, data, and infrastructure failures.

## Application telemetry

- API request latency/error rate;
- tile request latency/error rate;
- frontend exceptions;
- failed scenario evaluations;
- authentication/authorization failures.

## Data pipeline telemetry

- import start/end;
- source version/hash;
- row/feature counts;
- validation failures;
- publish artifact hashes;
- release version;
- public/private leakage checks.

## Database telemetry

- connection saturation;
- slow queries;
- storage growth;
- replication/backup health where applicable.

## Privacy

Public product analytics must not collect sensitive research contents or private scenario parameters unless expressly required and disclosed.
