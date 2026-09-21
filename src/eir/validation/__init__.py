"""Validation layer — chronological walk-forward evaluation.

Responsibility boundary:
    - Run walk-forward (never random-split, per DECISIONS.md Decision
      008) evaluation of a model over a historical window, using only
      PIT-correct features at each historical as_of_date.
    - Compute point-forecast error metrics (MAE, RMSE, MAPE, etc.) and,
      once a probability engine exists, probability-calibration metrics
      (Brier score, log loss).
    - Emit `eir.schemas.validation.ValidationResult` records — the sole
      source of truth for any claimed model performance in this project.
      No performance figures should ever be asserted outside of a
      ValidationResult produced by this layer.

Explicitly NOT this layer's responsibility:
    - Deciding calibration mapping used at forecast time ->
      eir.uncertainty (which consumes ValidationResult as its input)

Planned interface (Stage 3+): a `walk_forward_evaluate(model,
company_ids, start, end) -> ValidationResult` function.

Status: Stage 1 — module boundary only, no implementation yet.
"""
