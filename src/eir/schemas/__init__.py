"""EIR data contracts (schemas).

This module defines the architectural data contracts for the project:
raw -> normalized -> point-in-time -> features -> forecast ->
forecast history -> validation results, plus a shared provenance/quality
record attached across layers.

These are structural definitions for Stage 1. No data-producing logic
lives here.
"""

from eir.schemas.common import (
    DataSourceId,
    ForecastModelType,
    FreshnessStatus,
    OutcomeLabel,
    ValidationScheme,
)
from eir.schemas.provenance import ProvenanceRecord
from eir.schemas.raw import RawObservation
from eir.schemas.normalized import NormalizedObservation
from eir.schemas.pit import PitObservation
from eir.schemas.features import FeatureValue
from eir.schemas.forecast import (
    DriverContribution,
    ForecastHistoryEntry,
    ForecastResult,
    PredictionRange,
)
from eir.schemas.validation import ValidationResult

__all__ = [
    "DataSourceId",
    "ForecastModelType",
    "FreshnessStatus",
    "OutcomeLabel",
    "ValidationScheme",
    "ProvenanceRecord",
    "RawObservation",
    "NormalizedObservation",
    "PitObservation",
    "FeatureValue",
    "DriverContribution",
    "ForecastHistoryEntry",
    "ForecastResult",
    "PredictionRange",
    "ValidationResult",
]
