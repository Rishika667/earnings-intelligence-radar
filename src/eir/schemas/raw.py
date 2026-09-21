"""Raw data contract.

Raw records preserve exactly what a source returned (minimally parsed),
before any unit conversion, renaming, or cross-source alignment. This is
the audit trail: normalization bugs should always be diagnosable by
comparing normalized output back to the corresponding raw record.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional

from eir.schemas.common import DataSourceId
from eir.schemas.provenance import ProvenanceRecord


@dataclass(frozen=True)
class RawObservation:
    """A single, minimally-parsed observation as received from a source.

    Attributes:
        source: Which source this came from.
        entity_id: Source-native identifier for the subject (e.g. a CIK for
            SEC filings, a FRED series code, a ticker for company-level
            data). Interpretation is source-specific at this layer.
        as_of: The date/period the observation refers to, in the source's
            own terms (not yet aligned to a canonical fiscal calendar).
        value: The raw value, kept as returned (string, number, or nested
            structure) — deliberately untyped/unconverted at this layer.
        unit: Unit as reported by the source, if any (e.g. "USD",
            "Thousands", "Index"). Not yet normalized.
        raw_payload: Optional full raw payload (or reference to it) for
            traceability, e.g. the original JSON/XBRL fragment.
        provenance: Source/freshness/retrieval metadata.
    """

    source: DataSourceId
    entity_id: str
    as_of: datetime
    value: Any
    unit: Optional[str]
    provenance: ProvenanceRecord
    raw_payload: Optional[dict] = None
    extra: dict = field(default_factory=dict)
