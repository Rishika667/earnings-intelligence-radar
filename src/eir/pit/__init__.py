"""Point-in-time (PIT) layer — builds "what was known as of date X" views
from normalized data.

Responsibility boundary:
    - Given a normalized series (potentially containing multiple
      revisions/vintages) and an as_of_date, select the latest vintage
      that would actually have been available at that date.
    - Emit `eir.schemas.pit.PitObservation` records.
    - This is the layer that structurally enforces the project's no-
      look-ahead-bias requirement (PROJECT_SPEC.md section 6).

Explicitly NOT this layer's responsibility:
    - Fetching data -> eir.ingestion
    - Feature computation -> eir.features (features consume PIT output,
      they do not re-decide point-in-time correctness)

Planned interface (Stage 2): a `build_pit_view(metric, company_id,
as_of_date) -> list[PitObservation]` function operating over normalized
data, using each observation's ProvenanceRecord.vintage_date /
source_published_at to determine availability.

Status: Stage 1 — module boundary only, no implementation yet.
"""
