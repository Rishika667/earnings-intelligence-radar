"""Normalized data contract.

Normalized records represent data after unit conversion, renaming to
canonical field names, and alignment onto a consistent entity/time
representation — but BEFORE any point-in-time filtering is applied. A
normalized series may still contain later revisions; it is not yet a
"what was known as of date X" view (see eir.schemas.pit for that).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional

from eir.schemas.common import DataSourceId
from eir.schemas.provenance import ProvenanceRecord


@dataclass(frozen=True)
class NormalizedObservation:
    """A single observation after normalization to canonical form.

    Attributes:
        company_id: Canonical company identifier used throughout EIR
            (e.g. ticker or internal ID — finalized in Stage 2).
        metric: Canonical metric name (e.g. "revenue", "fed_funds_rate",
            "search_interest_index"). Canonical metric vocabulary is
            defined and versioned during Stage 2 implementation.
        period_start: Start of the period the value applies to.
        period_end: End of the period the value applies to (for
            point-in-time macro series, period_start == period_end).
        value: Normalized numeric value.
        unit: Canonical unit after conversion (e.g. "USD", "percent").
        source: Originating data source.
        provenance: Provenance/quality metadata for this observation.
        revision_of: If this observation revises an earlier one, a
            reference identifier for the observation it revises. None for
            first-seen observations.
    """

    company_id: Optional[str]
    metric: str
    period_start: date
    period_end: date
    value: float
    unit: str
    source: DataSourceId
    provenance: ProvenanceRecord
    revision_of: Optional[str] = None
    extra: dict = field(default_factory=dict)
