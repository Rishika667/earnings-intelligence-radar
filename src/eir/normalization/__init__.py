"""Normalization layer — converts RawObservation records into
NormalizedObservation records.

Responsibility boundary:
    - Unit conversion to canonical units (e.g. thousands -> raw USD).
    - Renaming source-specific fields/tags to the canonical metric
      vocabulary (defined in Stage 2).
    - Aligning entity identifiers to the canonical `company_id`.
    - Aligning arbitrary source period conventions to a consistent
      period_start/period_end representation.
    - Preserving a link back to the originating raw record + provenance.

Explicitly NOT this layer's responsibility:
    - Point-in-time cutoff filtering -> eir.pit
    - Deciding which vintage is "the" value for historical replay
      (normalized data may still contain multiple revisions)

Planned interface (Stage 2): a `Normalizer` per source implementing
`normalize(raw: RawObservation) -> NormalizedObservation`.

Status: Stage 1 — module boundary only, no implementation yet.
"""
