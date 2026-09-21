"""Freshness monitoring layer.

Responsibility boundary:
    - Continuously (or on-demand) check each configured data source's
      latest available observation against its expected publication
      cadence, classifying it as current/delayed/stale/missing.
    - Surface a per-source, per-company freshness summary for the
      "Data Freshness" product feature (PROJECT_SPEC.md section 11).

Explicitly NOT this layer's responsibility:
    - Fetching the data itself -> eir.ingestion
    - Scoring quality/completeness of an individual observation ->
      eir.quality (monitoring aggregates quality/freshness signals over
      time and across sources for reporting)

Planned interface (Stage 6): a `FreshnessSnapshot` builder that reads
the latest ProvenanceRecord per tracked series and returns a
FreshnessStatus summary.

Status: Stage 1 — module boundary only, no implementation yet.
"""
