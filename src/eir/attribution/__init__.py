"""Driver attribution layer.

Responsibility boundary:
    - Explain a given ForecastResult by producing DriverContribution
      records (e.g. linear-model coefficients x feature value, or SHAP
      values for tree-based models).
    - Support the "Driver Analysis" and "What Changed?" product features
      (PROJECT_SPEC.md section 11) by attributing both a single forecast
      and the delta between two forecasts for the same target period.

Explicitly NOT this layer's responsibility:
    - Producing the forecast itself -> eir.forecasting
    - Deciding whether a feature group is broadly useful across many
      forecasts -> eir.altdata

Planned interface (Stage 5): an `Attributor` per model family
implementing `attribute(model, features) -> list[DriverContribution]`.

Status: Stage 1 — module boundary only, no implementation yet.
"""
