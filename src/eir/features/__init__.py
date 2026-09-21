"""Feature engineering layer — derives modeling-ready FeatureValue records
from PIT observations.

Responsibility boundary:
    - Compute lags, growth rates, rolling statistics, and cross-source
      derived signals, always parameterized by an explicit as_of_date.
    - Tag each feature with a `feature_group` (financial, macro,
      search_interest, industry, consumer, other) so the alternative-data
      research layer (eir.altdata) can evaluate incremental value by
      group.
    - Consume only `eir.schemas.pit.PitObservation` records — never raw
      or normalized data directly, so PIT correctness is inherited rather
      than re-implemented.

Explicitly NOT this layer's responsibility:
    - Forecasting -> eir.forecasting
    - Deciding whether a feature group is useful -> eir.altdata /
      eir.validation

Planned interface (Stage 2/5): a `FeatureBuilder` per feature/group
implementing `build(company_id, target_period_end, as_of_date) ->
list[FeatureValue]`.

Status: Stage 1 — module boundary only, no implementation yet.
"""
