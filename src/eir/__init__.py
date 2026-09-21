"""Earnings Intelligence Radar (EIR) — core research package.

This package implements the research/engineering side of the Earnings
Intelligence Radar platform: data ingestion, normalization, point-in-time
handling, feature engineering, forecasting, uncertainty/calibration,
attribution, alternative-data testing, validation, forecast history, and
freshness monitoring.

Architectural layering (see docs/ARCHITECTURE.md for details):

    ingestion -> normalization -> pit -> quality -> features
        -> forecasting -> uncertainty -> attribution
        -> validation -> history -> monitoring -> reporting

The Streamlit presentation layer lives in `dashboard/` and is intentionally
kept separate from this package. Code under `dashboard/` should only ever
call into `eir` through stable, documented interfaces — it must not contain
forecasting or data-engineering logic itself.

Stage 1 note: this package currently defines module boundaries, interfaces,
and data contracts only. No ingestion, modeling, or dashboard logic has been
implemented yet. See PROJECT_STATE.md / BUILD_LOG.md for current status.
"""

__version__ = "0.1.0"
