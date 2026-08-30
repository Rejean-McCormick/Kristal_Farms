# Incident response

## Incident classes

- service outage;
- incorrect public data;
- privacy/access-control exposure;
- corrupted import/publication;
- scenario/model defect;
- credential compromise.

## Immediate priorities

1. Protect users and restricted data.
2. Stop further publication or writes if needed.
3. Preserve logs/evidence.
4. Restore known-good service/data.
5. Communicate scope and affected release/version.

## Data correction

Do not silently replace an immutable public data release. Publish a corrected release and document supersession.

## Post-incident

Create corrective actions for code, data QA, policy, documentation, or monitoring as appropriate.
