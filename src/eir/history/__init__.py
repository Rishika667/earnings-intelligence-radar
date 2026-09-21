"""Forecast history / information-arrival timeline layer.

Responsibility boundary:
    - Append `eir.schemas.forecast.ForecastHistoryEntry` records each
      time a new ForecastResult is generated for a given
      company/target_period_end, without mutating or deleting prior
      entries.
    - Support "Forecast Evolution", "What Changed?", and "Historical
      Replay" product features (PROJECT_SPEC.md section 11) by exposing
      a chronological read path over stored forecasts.

Explicitly NOT this layer's responsibility:
    - Deciding *why* something changed (that's an attribution/diff
      concern, potentially delegated to eir.attribution when computing
      change_summary)

Planned interface (Stage 6): `record_forecast(result) ->
ForecastHistoryEntry` and `get_history(company_id, target_period_end) ->
list[ForecastHistoryEntry]`.

Status: Stage 1 — module boundary only, no implementation yet.
"""
