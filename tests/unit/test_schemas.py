"""Structural validity tests for the Stage 1 data contracts.

These tests check that the dataclasses can be constructed with sane
example values and that field relationships hold (e.g. optional fields
default correctly). They do not test any real financial data or model
output, since none exists yet.
"""

from __future__ import annotations

from datetime import date, datetime, timezone

from eir.schemas import (
    DataSourceId,
    ForecastModelType,
    ForecastResult,
    FreshnessStatus,
    NormalizedObservation,
    PitObservation,
    PredictionRange,
    ProvenanceRecord,
    RawObservation,
    ValidationResult,
    ValidationScheme,
)


def _sample_provenance() -> ProvenanceRecord:
    return ProvenanceRecord(
        source=DataSourceId.FRED,
        source_series_id="EXAMPLESERIES",
        retrieved_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        freshness=FreshnessStatus.CURRENT,
    )


def test_raw_observation_constructs():
    obs = RawObservation(
        source=DataSourceId.FRED,
        entity_id="EXAMPLESERIES",
        as_of=datetime(2026, 1, 1, tzinfo=timezone.utc),
        value="1.23",
        unit="percent",
        provenance=_sample_provenance(),
    )
    assert obs.source == DataSourceId.FRED
    assert obs.raw_payload is None


def test_normalized_observation_constructs():
    obs = NormalizedObservation(
        company_id=None,
        metric="fed_funds_rate",
        period_start=date(2026, 1, 1),
        period_end=date(2026, 1, 31),
        value=1.23,
        unit="percent",
        source=DataSourceId.FRED,
        provenance=_sample_provenance(),
    )
    assert obs.value == 1.23
    assert obs.revision_of is None


def test_pit_observation_constructs():
    obs = PitObservation(
        company_id="AAPL",
        metric="revenue",
        period_start=date(2025, 10, 1),
        period_end=date(2025, 12, 31),
        value=100.0,
        unit="USD_millions",
        as_of_date=date(2026, 1, 15),
        source=DataSourceId.SEC_XBRL,
        provenance=_sample_provenance(),
    )
    assert obs.is_latest_known is True


def test_forecast_result_defaults():
    result = ForecastResult(
        company_id="AAPL",
        target_period_end=date(2026, 3, 31),
        as_of_date=date(2026, 1, 15),
        model_type=ForecastModelType.BASELINE_NAIVE,
        point_estimate=100.0,
        unit="USD_millions",
    )
    # Probabilities/ranges are optional and must not be silently invented.
    assert result.prediction_range is None
    assert result.beat_probability is None
    assert result.drivers == []


def test_forecast_result_with_range_is_consistent():
    rng = PredictionRange(low=90.0, high=110.0, confidence_level=0.80)
    result = ForecastResult(
        company_id="AAPL",
        target_period_end=date(2026, 3, 31),
        as_of_date=date(2026, 1, 15),
        model_type=ForecastModelType.BASELINE_SEASONAL,
        point_estimate=100.0,
        unit="USD_millions",
        prediction_range=rng,
    )
    assert result.prediction_range.low <= result.point_estimate <= result.prediction_range.high


def test_validation_result_defaults_to_no_probability_metrics():
    result = ValidationResult(
        model_type=ForecastModelType.BASELINE_NAIVE,
        model_version="v0",
        scheme=ValidationScheme.WALK_FORWARD,
        evaluation_start=date(2020, 1, 1),
        evaluation_end=date(2025, 1, 1),
        n_observations=0,
    )
    # No probability engine exists yet (Stage 4+); must default to None,
    # never a fabricated metric.
    assert result.probability_metrics is None
    assert result.is_negative_finding is False


def test_validation_scheme_flags_random_split_as_not_recommended():
    """The random-split enum value must exist for completeness but must be
    distinguishable/flaggable as non-primary, per DECISIONS.md Decision 008."""
    assert ValidationScheme.RANDOM_SPLIT_NOT_RECOMMENDED.value == "random_split_not_recommended"
    assert ValidationScheme.WALK_FORWARD.value == "walk_forward"
