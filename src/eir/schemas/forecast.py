"""Forecast and forecast-history data contracts.

Two distinct concerns are kept separate here, per PROJECT_SPEC.md /
DECISIONS.md:

1. `ForecastResult` — a single model's output for a single target period as
   of a single date. Includes the point estimate, range/distribution, and
   calibrated beat/meet/miss probabilities *if and when they exist*. This
   schema does not itself guarantee calibration; calibration is a property
   the validation layer must establish before probabilities are trusted.
2. `ForecastHistoryEntry` — a lightweight, append-only record used to
   reconstruct "how did the forecast evolve over time" (PROJECT_SPEC.md
   section 11, "Forecast Evolution"). History entries reference a
   ForecastResult rather than duplicating its full contents.

`ModelConfidence` (data-quality/coverage based) is intentionally a separate
field from `beat_probability` / calibration outputs — model probability and
data confidence must not be conflated (DECISIONS.md Decision 005,
PROJECT_SPEC.md section 8).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Dict, List, Optional

from eir.schemas.common import ForecastModelType


@dataclass(frozen=True)
class PredictionRange:
    """A prediction interval/range around a point estimate.

    Attributes:
        low: Lower bound of the interval.
        high: Upper bound of the interval.
        confidence_level: Nominal interval coverage (e.g. 0.80 for an 80%
            interval). Must be documented, never left implicit.
    """

    low: float
    high: float
    confidence_level: float


@dataclass(frozen=True)
class DriverContribution:
    """A single feature/driver's estimated contribution to a forecast.

    Attributes:
        feature_name: Canonical feature name (see eir.schemas.features).
        contribution: Signed estimated contribution, in the same units as
            the forecast target unless otherwise noted.
        rank: Optional rank by absolute contribution magnitude.
        method: Attribution method used (e.g. "linear_coefficient",
            "shap"). Established during Stage 5 implementation.
    """

    feature_name: str
    contribution: float
    rank: Optional[int] = None
    method: Optional[str] = None


@dataclass(frozen=True)
class ForecastResult:
    """A single model's forecast for one company/target-period/as-of date.

    Attributes:
        company_id: Canonical company identifier.
        target_period_end: The fiscal period being forecast.
        as_of_date: The date this forecast was generated as of. Combined
            with target_period_end, this lets forecast history reconstruct
            "what did we predict, and how far ahead of the print."
        model_type: Which model family produced this result.
        point_estimate: Central forecast value (e.g. forecast revenue).
        unit: Unit of the point estimate.
        prediction_range: Optional interval around the point estimate.
        beat_probability: Calibrated probability of beating the reference
            figure, if available. Must come from the calibration/
            validation layer — never hand-set.
        meet_probability: Calibrated probability of meeting.
        miss_probability: Calibrated probability of missing.
        drivers: Attributed driver contributions for this forecast.
        data_confidence: Data-quality/coverage-based confidence score for
            this forecast (0-1), kept conceptually separate from the
            probability fields above.
        reference_value: The consensus/reference figure the beat/meet/miss
            framing is measured against, if known at as_of_date.
        model_version: Free-form version tag for the producing model.
        generated_at: Wall-clock timestamp the forecast was computed.
        notes: Free-text notes, e.g. known limitations for this forecast.
    """

    company_id: str
    target_period_end: date
    as_of_date: date
    model_type: ForecastModelType
    point_estimate: float
    unit: str
    prediction_range: Optional[PredictionRange] = None
    beat_probability: Optional[float] = None
    meet_probability: Optional[float] = None
    miss_probability: Optional[float] = None
    drivers: List[DriverContribution] = field(default_factory=list)
    data_confidence: Optional[float] = None
    reference_value: Optional[float] = None
    model_version: str = "unversioned"
    generated_at: Optional[datetime] = None
    notes: Optional[str] = None
    extra: Dict = field(default_factory=dict)


@dataclass(frozen=True)
class ForecastHistoryEntry:
    """An append-only pointer used to reconstruct forecast evolution.

    Attributes:
        company_id: Canonical company identifier.
        target_period_end: The fiscal period being forecast.
        as_of_date: The date this entry corresponds to.
        forecast_ref: Identifier/key of the corresponding ForecastResult
            (e.g. a storage key), so history does not duplicate full
            forecast payloads.
        change_summary: Optional short human-readable description of what
            changed vs. the previous entry (e.g. "revenue estimate revised
            up after retail sales release"). Populated by Stage 6 logic,
            not fabricated.
        recorded_at: Wall-clock timestamp this history entry was recorded.
    """

    company_id: str
    target_period_end: date
    as_of_date: date
    forecast_ref: str
    change_summary: Optional[str] = None
    recorded_at: Optional[datetime] = None
