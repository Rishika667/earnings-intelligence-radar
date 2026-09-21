"""Forecasting layer — produces `eir.schemas.forecast.ForecastResult`
records from features.

Sub-packages:
    - `baseline`: historical/seasonal and naive baseline models. These
      must exist and be evaluated before any more complex model is
      trusted (PROJECT_SPEC.md section 7).
    - `statistical`: regression-family models (ridge, lasso).
    - `ml`: gradient boosting / ensemble models.

Responsibility boundary:
    - Consume `eir.schemas.features.FeatureValue` records for a given
      company/target_period_end/as_of_date.
    - Emit a point estimate + unit. Ranges/distributions/probabilities
      are layered on by `eir.uncertainty`, not computed here directly,
      so a model can be evaluated on point-forecast accuracy
      independently of probability calibration.

Explicitly NOT this layer's responsibility:
    - Calibrating beat/meet/miss probabilities -> eir.uncertainty
    - Walk-forward evaluation -> eir.validation
    - Explaining *why* -> eir.attribution

Planned interface (Stage 3): a common `Forecaster` Protocol implementing
`predict(features) -> ForecastResult` per model, so eir.validation can
walk-forward evaluate any registered model uniformly.

Status: Stage 1 — module boundary only, no implementation yet.
"""
