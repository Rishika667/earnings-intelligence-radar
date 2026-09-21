# Earnings Intelligence Radar — Project State

## Project Objective

Build a near-real-time financial intelligence platform that uses free public financial, economic, industry, and alternative-data sources to estimate upcoming company earnings performance.

The platform should provide not only a forecast, but also prediction ranges, probabilities, explanations, historical validation, data-source analysis, data freshness, provenance, and limitations.

---

## Current Status

Stage 1 — Architecture + Project Scaffold

---

## Current Version

v0.1.0

---

## Completed

- Project concept finalized
- Project separated from Financial Intelligence Radar
- Free public data requirement established
- Near-real-time requirement established
- Revenue nowcast requirement established
- Prediction range requirement established
- Probability requirement established
- Beat / meet / miss framework established
- Driver-analysis requirement established
- Data-source transparency requirement established
- Point-in-time methodology requirement established
- Historical validation requirement established
- Data freshness requirement established
- Data provenance requirement established
- Model limitation requirement established
- GitHub repository created
- PROJECT_SPEC.md created
- PROJECT_STATE.md, BUILD_LOG.md, DECISIONS.md, HANDOFF.md created
  (project-control/recovery system complete)

### Stage 1 — Architecture + Project Scaffold (this update)

- Created `src/eir/` research/engineering package with module boundaries
  for every future component: ingestion, normalization, pit, quality,
  features, forecasting (baseline/statistical/ml), uncertainty,
  attribution, altdata, validation, history, monitoring, reporting,
  utils, config. Each module has a docstring stating its responsibility
  boundary and explicit non-responsibilities; no business logic is
  implemented yet.
- Defined Stage 1 data contracts in `src/eir/schemas/`: `ProvenanceRecord`,
  `RawObservation`, `NormalizedObservation`, `PitObservation`,
  `FeatureValue`, `ForecastResult` (+ `PredictionRange`,
  `DriverContribution`), `ForecastHistoryEntry`, `ValidationResult`, plus
  shared enums (`DataSourceId`, `FreshnessStatus`, `OutcomeLabel`,
  `ForecastModelType`, `ValidationScheme`). Raw / normalized / PIT /
  features / forecast / forecast-history / validation / provenance are
  all explicitly distinct types, as required.
- Implemented a minimal, dependency-light configuration loader
  (`eir.config.settings`) with a documented env-var-only convention for
  secrets (`get_env`, `.env.example`) and YAML loading for non-secret
  config (`load_yaml_config`, with `.example.yaml` fallback).
- Created non-secret config templates: `config/companies.example.yaml`,
  `config/data_sources.example.yaml`, `config/model.example.yaml`,
  `config/app.example.yaml`, plus `config/README.md` documenting the
  convention. No API keys/secrets exist anywhere in the repository;
  credentials are referenced only by environment-variable name.
- Created project directory scaffold: `src/`, `data/{raw,normalized,pit,
  features,forecasts,validation}`, `tests/{smoke,unit}`, `dashboard/
  {pages,components}`, `config/`, `docs/`, `scripts/`.
- Created `dashboard/app.py` (Streamlit placeholder entrypoint, no
  functionality) and `dashboard/README.md` documenting the
  research/presentation separation rule.
- Wrote `docs/ARCHITECTURE.md`: system architecture, directory structure,
  module responsibilities, ASCII data-flow diagram, data contracts
  summary, configuration architecture, testing architecture, and a
  stage-dependency map.
- Established dependency management: `pyproject.toml` (setuptools,
  `src/` layout) + `requirements.txt`, deliberately minimal (PyYAML,
  python-dotenv, pytest only — no pandas/numpy/streamlit/sklearn yet,
  since Stage 1 does not need them).
- Added `pytest.ini` and a full Stage 1 test suite: 4 smoke-test groups
  (package import, all 19 module boundaries import, project-control
  files present, no `.env` committed / no secret-like values in config)
  and unit tests for schemas (structural construction, safe defaults —
  no fabricated probabilities/ranges) and config loading (template
  parsing, env-var fallback behavior, credential-field convention
  check). 37/37 tests passing.
- Added `scripts/check_scaffold.py` as a convenience manual sanity check
  outside pytest.
- Updated `README.md` with Stage 1 status and dev setup instructions
  (no rewrite of existing content, additive only).

---

## In Progress

None — Stage 1 objectives are complete as scoped (architecture + scaffold
only; no ingestion/modeling/dashboard logic).

---

## Next Task

Stage 2 — Data Foundation

Specifically (per BUILD_LOG.md Stage 2 objectives):

1. Implement `eir.ingestion` clients for at least one free/public source
   (start with SEC XBRL, per PROJECT_SPEC.md priority).
2. Implement `eir.normalization` for that source's data into
   `NormalizedObservation` records, establishing the first version of the
   canonical metric vocabulary.
3. Implement `eir.pit` point-in-time view construction.
4. Implement initial `eir.quality` freshness/provenance scoring.
5. Add corresponding unit tests (no fabricated data — use real, small,
   reproducible fixtures or clearly-marked synthetic fixtures for unit
   tests only).
6. Update PROJECT_STATE.md / BUILD_LOG.md / HANDOFF.md and commit per the
   standard stage-completion workflow.

---

## Selected LLM

Genspark AI — one consistent model will be used throughout the project.

---

## Data Cost Constraint

Target paid data/API cost:

₹0

The core project must remain buildable using free/public data sources.

---

## Core Product Outputs

- Revenue nowcast
- Prediction range
- Prediction distribution
- Beat probability
- Meet probability
- Miss probability
- Driver attribution
- Forecast evolution
- Historical prediction replay
- Data-source incremental value
- Data freshness
- Data provenance
- Data quality indicators
- Model agreement
- Probability calibration
- Limitations and model-risk information

---

## Core Data Sources Under Consideration

- SEC XBRL
- FRED
- ALFRED
- Google Trends
- U.S. Census
- NOAA
- Other relevant free public datasets where justified

---

## Important Constraints

- No paid proprietary data required
- Avoid look-ahead bias
- Use point-in-time information where feasible
- Use chronological walk-forward validation
- Do not invent probabilities
- Calibrate probabilities using historical outcomes
- Report negative or weak findings honestly
- Do not make unsupported BUY/SELL recommendations
- Maintain data provenance
- Maintain reproducibility

---

## Important Product Principle

The project is not simply an earnings prediction model.

It is a financial research and intelligence product.

The intended flow is:

Data
→ Features
→ Forecast
→ Probability
→ Explanation
→ Validation
→ Intelligence

---

## Known Problems

None. Stage 1 test suite passes (37/37). One open item worth tracking:
the canonical `company_id` convention (ticker vs. CIK vs. internal ID)
is provisionally set to "ticker" in `config/companies.example.yaml`; this
should be confirmed rather than silently changed once SEC XBRL ingestion
(Stage 2) is implemented, since CIK may be more stable long-term.

---

## Last Completed Action

Completed Stage 1 — Architecture + Project Scaffold: created the `eir`
package with module boundaries and data-contract schemas, config
templates and loader, dashboard placeholder, docs/ARCHITECTURE.md, test
suite (smoke + unit, 37/37 passing), and dependency management files.

---

## Next Exact Action

Begin Stage 2 — Data Foundation: implement `eir.ingestion` for the first
free/public source (recommended: SEC XBRL), then `eir.normalization`,
`eir.pit`, and initial `eir.quality` freshness scoring, per the "Next
Task" section above.

---

## Recovery Procedure

If project work is interrupted or AI context is lost:

1. Open the GitHub repository.
2. Read PROJECT_SPEC.md.
3. Read PROJECT_STATE.md.
4. Read DECISIONS.md.
5. Read BUILD_LOG.md.
6. Read HANDOFF.md.
7. Continue only from the task identified in PROJECT_STATE.md and HANDOFF.md.

Do not restart completed work without a documented reason.
