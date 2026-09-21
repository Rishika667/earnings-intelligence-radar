"""Uncertainty / calibrated-probability layer.

Responsibility boundary:
    - Turn a model's point estimate into a prediction range/distribution
      (e.g. via residual-based intervals, quantile regression, or
      ensemble spread — method chosen during Stage 4 implementation).
    - Convert historical performance (from eir.validation) into
      calibrated beat/meet/miss probabilities. Probabilities must be
      derived from evaluated historical outcomes, never hand-assigned
      (DECISIONS.md Decision 005).

Explicitly NOT this layer's responsibility:
    - Producing the point estimate itself -> eir.forecasting
    - Running the walk-forward evaluation used to calibrate ->
      eir.validation (this layer consumes validation output)

Planned interface (Stage 4): a `Calibrator` that maps a model's
historical forecast-error distribution (from ValidationResult) onto a
PredictionRange and beat/meet/miss probability set for a new
ForecastResult.

Status: Stage 1 — module boundary only, no implementation yet.
"""
