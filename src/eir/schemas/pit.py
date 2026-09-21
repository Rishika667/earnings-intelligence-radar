"""Point-in-time (PIT) data contract.

A PIT snapshot answers: "what would a forecaster have known about this
metric if they were standing at `as_of_date`?" This is the mechanism used
throughout the project to avoid look-ahead bias (PROJECT_SPEC.md section 6,
DECISIONS.md Decision 007).

Design choice: PIT is modeled as an explicit *view* built from normalized
data plus an as-of cutoff, rather than mutating normalized data in place.
This keeps the full revision history intact and auditable while still
letting the forecasting layer consume a simple "what was known" table.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from eir.schemas.common import DataSourceId
from eir.schemas.provenance import ProvenanceRecord


@dataclass(frozen=True)
class PitObservation:
    """A single observation as it was known as of a given cutoff date.

    Attributes:
        company_id: Canonical company identifier, or None for
            company-agnostic (e.g. macro) series.
        metric: Canonical metric name.
        period_start: Start of the period the value applies to.
        period_end: End of the period the value applies to.
        value: The value as known at `as_of_date` (may be a preliminary
            vintage that was later revised).
        unit: Canonical unit.
        as_of_date: The cutoff date this PIT view represents — i.e., "as
            of this date, this was the latest known value for this
            period." This is the field that makes the record point-in-time
            rather than just normalized.
        source: Originating data source.
        provenance: Provenance/quality metadata for the underlying
            observation, including its vintage_date if applicable.
        is_latest_known: Whether this was still the latest known vintage
            at `as_of_date` (True by construction for a correctly built
            PIT view; kept explicit for auditability).
    """

    company_id: Optional[str]
    metric: str
    period_start: date
    period_end: date
    value: float
    unit: str
    as_of_date: date
    source: DataSourceId
    provenance: ProvenanceRecord
    is_latest_known: bool = True
    extra: dict = field(default_factory=dict)
