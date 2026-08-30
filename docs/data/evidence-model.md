# Evidence model

## Purpose

Kristal Farms must be able to show not only *what* a map says, but *why* it says it.

## Objects

### `research.source`

Represents an original source.

Suggested fields:

```text
id
title
publisher / authority
source_type
url or document reference
publication_date
retrieved_at
license_or_terms
quality_class
metadata
```

### `research.evidence`

Represents a claim or scoped research finding.

```text
id
claim
evidence_type
verification_status
confidence
valid_from
valid_to
last_verified
metadata
```

### `research.evidence_source`

Many-to-many relation between evidence and sources.

### `research.evidence_relation`

Links evidence to a place, asset, project, corridor, or other subject.

```text
evidence_id
subject_type
subject_id
relation_type
```

Example relation types:

```text
supports
describes
constrains
contradicts
references
```

### `research.observation`

A specific value or categorical observation.

```text
id
subject_type
subject_id
metric
value_numeric
value_text
unit
valid_from
valid_to
evidence_id
metadata
```

## Geometry rule

Evidence MAY have no geometry. Do not invent a point location to make evidence appear on the map. Connect non-spatial evidence to spatial subjects through relations.

## Verification statuses

Recommended baseline:

```text
verified
supported
scoped
unverified
conflicting
unknown
```

Avoid converting these labels into a generic confidence percentage unless a documented methodology exists.

## Evidence panel

The UI should expose source title, authority, publication/access dates, claim, verification status, and known limitations whenever practical.
