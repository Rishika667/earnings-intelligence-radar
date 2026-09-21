# Dashboard (Presentation Layer)

This directory will hold the Streamlit dashboard (Stage 7 —
Productization), plus lighter-weight page/component scaffolding that may
be exercised earlier for manual checks.

## Boundary rule

Code under `dashboard/` must not contain forecasting, data-engineering, or
validation logic. It may only:

- Call into the `eir` package (`src/eir`) through its public module
  interfaces.
- Handle presentation concerns: layout, widgets, charts, user input.

This separation is intentional (see `docs/ARCHITECTURE.md`, "Separation of
research logic and presentation logic") so the research/engineering code
remains independently testable and reusable (e.g. for batch report
generation) without a Streamlit runtime.

## Current status

Stage 1: directory scaffold only.

`app.py` is a placeholder entrypoint that will be filled in during Stage 7
once there is real forecast/validation data to display. It currently does
not implement any dashboard functionality.

## Layout

- `app.py` — Streamlit entrypoint (placeholder).
- `pages/` — Additional Streamlit pages (e.g. per product feature from
  PROJECT_SPEC.md section 11: Driver Analysis, Forecast Evolution, Data
  Source Analysis, etc.).
- `components/` — Reusable presentation components (charts, tables).
