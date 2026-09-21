"""Shared primitive types and enums used across all EIR data contracts.

Kept intentionally small at Stage 1. These types exist so later stages can
build ingestion, feature, and forecasting schemas without needing to
re-derive shared vocabulary (source identifiers, freshness states, etc.).
"""

from __future__ import annotations

from enum import Enum


class DataSourceId(str, Enum):
    """Identifiers for supported/target free public data sources.

    This is a controlled vocabulary, not a completeness guarantee — sources
    are added only when actually implemented in a later stage. Listing a
    source here does NOT mean it is wired up yet.
    """

    SEC_XBRL = "sec_xbrl"
    FRED = "fred"
    ALFRED = "alfred"
    GOOGLE_TRENDS = "google_trends"
    US_CENSUS = "us_census"
    NOAA = "noaa"
    OTHER_PUBLIC = "other_public"


class FreshnessStatus(str, Enum):
    """Freshness classification for a data point or source, relative to its
    own expected publication cadence (not a fixed wall-clock threshold)."""

    CURRENT = "current"
    DELAYED = "delayed"
    STALE = "stale"
    MISSING = "missing"
    UNKNOWN = "unknown"


class OutcomeLabel(str, Enum):
    """Realized outcome relative to a reference/consensus figure.

    Used only for historical, already-realized earnings outcomes when
    scoring forecasts — never as a forward-looking recommendation.
    """

    BEAT = "beat"
    MEET = "meet"
    MISS = "miss"
    UNKNOWN = "unknown"


class ForecastModelType(str, Enum):
    """Model family identifiers. Establishes vocabulary only; the actual
    model implementations are Stage 3+ work."""

    BASELINE_SEASONAL = "baseline_seasonal"
    BASELINE_NAIVE = "baseline_naive"
    RIDGE = "ridge"
    LASSO = "lasso"
    GRADIENT_BOOSTING = "gradient_boosting"
    ENSEMBLE = "ensemble"


class ValidationScheme(str, Enum):
    """Validation methodology identifiers.

    Per PROJECT_SPEC.md / DECISIONS.md, chronological walk-forward
    validation is the primary/required scheme. Random splitting is listed
    only so the type system can reject or flag it explicitly if it is ever
    encountered — it is not sanctioned as a primary validation method.
    """

    WALK_FORWARD = "walk_forward"
    HOLDOUT_OUT_OF_SAMPLE = "holdout_out_of_sample"
    RANDOM_SPLIT_NOT_RECOMMENDED = "random_split_not_recommended"
