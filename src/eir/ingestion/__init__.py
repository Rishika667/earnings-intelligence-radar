"""Ingestion layer — pulls data from free/public sources into RawObservation
records.

Responsibility boundary:
    - Talk to external sources (SEC XBRL, FRED, ALFRED, Google Trends,
      U.S. Census, NOAA, etc.).
    - Handle source-specific pagination/rate-limits/retries.
    - Attach ProvenanceRecord metadata (retrieval time, source series id).
    - Emit `eir.schemas.raw.RawObservation` records — nothing further
      downstream (no unit conversion, no renaming, no PIT logic).

Explicitly NOT this layer's responsibility:
    - Unit conversion / renaming -> eir.normalization
    - Point-in-time filtering -> eir.pit
    - Data-quality scoring -> eir.quality

Planned interface (implemented in Stage 2): a `DataSourceClient` base
class/Protocol per source, exposing a `fetch(entity_id, start, end) ->
list[RawObservation]` method. Credentials, if a given source requires
them, are read only via `eir.config.settings.get_env` — never hardcoded.

Status: Stage 1 — module boundary only, no implementation yet.
"""
