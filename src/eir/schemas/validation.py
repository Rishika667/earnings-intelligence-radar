"""Validation-result data contract.

Validation results are stored as first-class records, separate from
forecasts themselves, so that model performance claims are always
traceable to an explicit, chronological (walk-forward) evaluation rather
than asserted informally (PROJECT_SPEC.md section 10, DECISIONS.md
Decision 008/009).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Dict, Optional

from eir.schemas.common import ForecastModelType, ValidationScheme


@dataclass(frozen=True)
class ValidationResult:
    """Summary of a model's evaluated performance over a chronological
    evaluation window.

    Attributes:
        model_type: Which model family was evaluated.
        model_version: Version tag of the evaluated model.
        scheme: Validation methodology used. Should be
            ValidationScheme.WALK_FORWARD for primary reported results.
        evaluation_start: Start of the chronological evaluation window.
        evaluation_end: End of the chronological evaluation window.
        n_observations: Number of forecast/outcome pairs evaluated.
        error_metrics: Point-forecast error metrics (e.g.
            {"mae": ..., "rmse": ..., "mape": ...}). Only populated with
            metrics that were actually computed.
        probability_metrics: Probability-calibration metrics (e.g.
            {"brier_score": ..., "log_loss": ...}), only populated once a
            probability engine exists (Stage 4+). None beforehand.
        information_coefficient: Optional IC value for feature/signal
            evaluation (Stage 5).
        feature_group: If this result evaluates a specific alternative
            data / feature group's incremental value, the group name.
        baseline_comparison_model: If this result is framed as "does X
            improve on baseline Y", the baseline model identifier.
        is_negative_finding: Explicit flag so weak/negative results are
            easy to query and are never silently dropped from reporting.
        notes: Free-text notes, including caveats and limitations.
        computed_at: Wall-clock timestamp the validation run completed.
    """

    model_type: ForecastModelType
    model_version: str
    scheme: ValidationScheme
    evaluation_start: date
    evaluation_end: date
    n_observations: int
    error_metrics: Dict[str, float] = field(default_factory=dict)
    probability_metrics: Optional[Dict[str, float]] = None
    information_coefficient: Optional[float] = None
    feature_group: Optional[str] = None
    baseline_comparison_model: Optional[ForecastModelType] = None
    is_negative_finding: bool = False
    notes: Optional[str] = None
    computed_at: Optional[datetime] = None
