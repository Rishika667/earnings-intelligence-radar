"""Data quality and provenance layer.

Responsibility boundary:
    - Compute data-quality/coverage indicators (completeness, staleness,
      freshness classification) attached to ProvenanceRecord objects.
    - Track per-source freshness status against each source's own
      expected publication cadence.
    - Provide the data-confidence signal consumed by
      `ForecastResult.data_confidence` — kept conceptually and
      structurally separate from calibrated beat/meet/miss probabilities
      (DECISIONS.md Decision 005).

Explicitly NOT this layer's responsibility:
    - Deciding model probability calibration -> eir.uncertainty /
      eir.validation

Planned interface (Stage 2/6): a `FreshnessMonitor` that classifies a
ProvenanceRecord's FreshnessStatus, and a `DataQualityReport` aggregate
per company/source.

Status: Stage 1 — module boundary only, no implementation yet.
"""
