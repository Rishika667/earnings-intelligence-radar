"""Alternative-data incremental-value research layer.

Responsibility boundary:
    - Compare model performance (via eir.validation) with vs. without a
      given feature_group, to test whether it provides genuine
      incremental predictive value (PROJECT_SPEC.md section 9).
    - Apply multiple-testing controls and signal-decay analysis when
      testing many candidate feature groups/sources.
    - Report negative/weak findings as first-class results, not just
      positive ones (DECISIONS.md Decision 009).

Explicitly NOT this layer's responsibility:
    - Computing the features themselves -> eir.features
    - Running the underlying walk-forward evaluation -> eir.validation
      (this layer orchestrates comparisons across validation runs)

Planned interface (Stage 5): a `run_incremental_value_test(feature_group,
baseline_model, candidate_model) -> ValidationResult` style comparison
helper.

Status: Stage 1 — module boundary only, no implementation yet.
"""
