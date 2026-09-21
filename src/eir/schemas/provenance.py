"""Data-quality and provenance schema.

Provenance/quality metadata is modeled as a distinct, attachable object
rather than being folded into raw/normalized records. This keeps the
"how much do we trust this observation and where did it come from" concern
separate from the observation's value itself, which the project spec
requires (data-quality/provenance must stay conceptually distinct from
model probability — see DECISIONS.md and PROJECT_SPEC.md section 5/11).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from eir.schemas.common import DataSourceId, FreshnessStatus


@dataclass(frozen=True)
class ProvenanceRecord:
    """Describes where a piece of data came from and how fresh/trustworthy
    it is believed to be. Attached to raw/normalized/feature records rather
    than merged into them.

    Attributes:
        source: Which public data source produced this observation.
        source_series_id: The source's own identifier for the series
            (e.g. a FRED series ID, an SEC XBRL tag/concept name).
        retrieved_at: When EIR fetched this observation (UTC).
        source_published_at: When the source says the observation was
            published/released, if known. May be None if the source does
            not expose this reliably.
        vintage_date: For revisable series (e.g. ALFRED macro vintages),
            the "as-of" date of this particular vintage. None for series
            that are not revised.
        freshness: Computed freshness classification relative to the
            source's expected cadence.
        is_revised: Whether this observation is a later revision of a
            previously retrieved observation for the same period.
        license_note: Short human-readable note on usage terms (free/public
            data only per project constraints; this field documents that
            fact for auditability, it does not gate ingestion by itself).
        notes: Free-text notes (e.g. "estimated", "partial period").
    """

    source: DataSourceId
    source_series_id: str
    retrieved_at: datetime
    source_published_at: Optional[datetime] = None
    vintage_date: Optional[datetime] = None
    freshness: FreshnessStatus = FreshnessStatus.UNKNOWN
    is_revised: bool = False
    license_note: str = "free/public source"
    notes: Optional[str] = None
    extra: dict = field(default_factory=dict)
