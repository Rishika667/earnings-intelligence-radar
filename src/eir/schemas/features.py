"""Feature data contract.

A feature is a modeling-ready numeric input derived from one or more PIT
observations. Features are always tied to a specific `as_of_date` so that
the forecasting layer never has to re-derive point-in-time correctness —
that responsibility is fully discharged by the time data reaches this
layer (see eir.schemas.pit).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

from eir.schemas.common import DataSourceId


@dataclass(frozen=True)
class FeatureValue:
    """A single computed feature value for one company/period/as-of date.

    Attributes:
        company_id: Canonical company identifier.
        feature_name: Canonical feature name (versioned feature vocabulary
            defined during Stage 2/5 implementation, e.g.
            "revenue_yoy_growth_lag1", "search_interest_zscore_8w").
        target_period_end: The fiscal period this feature is meant to help
            predict (e.g. the upcoming quarter's period end).
        as_of_date: The date this feature was computed as of — must not
            use any information dated after this cutoff.
        value: The computed feature value.
        source_metrics: Canonical metric names this feature was derived
            from, for traceability back to normalized/PIT data.
        source_ids: Data sources contributing to this feature.
        feature_group: Coarse grouping for alternative-data analysis
            (e.g. "financial", "macro", "search_interest", "industry",
            "consumer"). Matches PROJECT_SPEC.md section 9 feature groups.
    """

    company_id: str
    feature_name: str
    target_period_end: date
    as_of_date: date
    value: float
    source_metrics: List[str] = field(default_factory=list)
    source_ids: List[DataSourceId] = field(default_factory=list)
    feature_group: Optional[str] = None
    extra: dict = field(default_factory=dict)
