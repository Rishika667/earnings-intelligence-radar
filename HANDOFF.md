# Earnings Intelligence Radar — AI Handoff

This file provides the instructions required for another AI session to continue the project without losing project context.

---

# READ FIRST

Before making any changes to the project, read these files in this order:

1. PROJECT_SPEC.md
2. PROJECT_STATE.md
3. DECISIONS.md
4. BUILD_LOG.md
5. HANDOFF.md

Do not begin implementation until these files have been read.

---

# PROJECT

Name:

Earnings Intelligence Radar

Purpose:

Build a near-real-time financial intelligence platform that uses free public financial, economic, industry, and alternative-data sources to estimate upcoming company earnings performance.

---

# CURRENT STATUS

Stage:

Stage 1 — Architecture + Project Scaffold (complete)

Repository:

earnings-intelligence-radar

Current version:

v0.1.0

---

# COMPLETED

- Project concept finalized
- Project separated from Financial Intelligence Radar
- Free/public data requirement established
- Near-real-time requirement established
- Revenue nowcasting requirement established
- Prediction range requirement established
- Probability requirement established
- Beat / meet / miss framework established
- Driver-analysis requirement established
- Point-in-time requirement established
- Historical validation requirement established
- Data freshness requirement established
- Data provenance requirement established
- Model limitation requirement established
- GitHub repository created
- PROJECT_SPEC.md created
- PROJECT_STATE.md created
- BUILD_LOG.md created
- DECISIONS.md created
- HANDOFF.md created
- **Stage 1 complete:** `src/eir` package scaffolded with one subpackage
  per architectural component (ingestion, normalization, pit, quality,
  features, forecasting/{baseline,statistical,ml}, uncertainty,
  attribution, altdata, validation, history, monitoring, reporting,
  utils, config) — each documented with a responsibility boundary, no
  business logic implemented.
- Data contracts defined in `src/eir/schemas/` (raw, normalized,
  point-in-time, features, forecast, forecast history, validation,
  provenance) as frozen dataclasses.
- Non-secret config templates created under `config/` +
  `config/README.md`; `.env.example` added; env-var-only credential
  convention implemented in `src/eir/config/settings.py`.
- Directory scaffold created: `data/`, `dashboard/` (placeholder
  `app.py`), `docs/`, `tests/{smoke,unit}`, `scripts/`.
- `docs/ARCHITECTURE.md` written (architecture, directory structure,
  module responsibilities, data flow diagram, data contracts,
  configuration architecture, testing architecture, stage-dependency
  map).
- Dependency management set up: `pyproject.toml` + `requirements.txt`
  (minimal: PyYAML, python-dotenv, pytest), `pytest.ini`.
- Test suite added and passing: 37/37 tests
  (`tests/smoke/test_project_scaffold.py`,
  `tests/unit/test_schemas.py`, `tests/unit/test_config.py`).
- `scripts/check_scaffold.py` added as a manual sanity-check
  convenience script.

---

# NEXT TASK

Begin:

Stage 2 — Data Foundation

Per PROJECT_SPEC.md / BUILD_LOG.md Stage 2 objectives, this means:

1. Implement `eir.ingestion` clients for at least one free/public source.
   Recommended first source: SEC XBRL (company facts API), since it is
   directly tied to the revenue-nowcasting target and requires no paid
   API key (only a compliant User-Agent header, per
   `config/data_sources.example.yaml`).
2. Implement `eir.normalization` to turn that source's `RawObservation`
   records into `NormalizedObservation` records — this is also where the
   first version of the canonical metric-name vocabulary should be
   established and documented (e.g. in `docs/ARCHITECTURE.md` or a new
   `docs/DATA_DICTIONARY.md`).
3. Implement `eir.pit` to build point-in-time views from normalized data
   (respecting `ProvenanceRecord.source_published_at` / `vintage_date`).
4. Implement initial `eir.quality` freshness/completeness scoring.
5. Decide and document the canonical `company_id` convention (ticker vs.
   CIK) — currently only provisionally set to ticker in
   `config/companies.example.yaml`; see PROJECT_STATE.md "Known
   Problems". If CIK or another scheme is chosen, update
   `config/companies.example.yaml` and `docs/ARCHITECTURE.md`
   accordingly and record the decision in `DECISIONS.md`.
6. Add unit tests for the new modules using small, reproducible fixtures
   — do not fabricate realistic-looking financial results; either use
   real small SEC/FRED responses (cached as test fixtures) or clearly
   label synthetic fixture data as such in code/comments.
7. Follow the standard stage-completion workflow (tests → update
   PROJECT_STATE.md → update BUILD_LOG.md → update DECISIONS.md if a
   major decision was made → update this HANDOFF.md → commit).

Do not implement forecasting, uncertainty, attribution, alt-data testing,
or the dashboard yet — those remain Stage 3+.

---

# NON-NEGOTIABLE CONSTRAINTS

Do not:

- Introduce paid data as a core requirement
- Introduce unnecessary complexity
- Use future information in historical forecasts
- Use random train/test splitting as the primary validation method
- Invent probability values
- Hide negative research results
- Claim true real-time coverage when sources are delayed
- Build unsupported BUY/SELL recommendations
- Rewrite completed modules without a documented reason
- Change established data schemas without documenting the change
- Replace working components unnecessarily

---

# DEVELOPMENT PRINCIPLE

Build the smallest credible working version first.

Then expand functionality only when the core system works.

Do not attempt to build every advanced feature simultaneously.

---

# EXPECTED DEVELOPMENT STAGES

Stage 1 — Architecture + Project Scaffold

Stage 2 — Data Foundation

Stage 3 — Forecasting Engine

Stage 4 — Uncertainty Engine

Stage 5 — Research Intelligence

Stage 6 — Monitoring and Trust Layer

Stage 7 — Productization

---

# WHEN A STAGE IS COMPLETED

The AI must:

1. Run appropriate tests.
2. Verify that the implementation works.
3. Update PROJECT_STATE.md.
4. Update BUILD_LOG.md.
5. Update DECISIONS.md if a major decision was made.
6. Update this HANDOFF.md.
7. Create a Git commit/checkpoint.
8. Clearly state the next exact task.

---

# IF CONTEXT OR CREDITS ARE LOST

Do not restart the project.

Instead:

1. Open the GitHub repository.
2. Read PROJECT_SPEC.md.
3. Read PROJECT_STATE.md.
4. Read DECISIONS.md.
5. Read BUILD_LOG.md.
6. Read HANDOFF.md.
7. Identify the current stage.
8. Identify the "Next Exact Action" in PROJECT_STATE.md.
9. Continue from that point.

---

# AI BEHAVIOR

Act as a technical implementation partner.

Do not redesign the entire project unnecessarily.

Do not make major architectural decisions silently.

When a major decision is required:

1. Identify the decision.
2. Explain the relevant trade-off.
3. Record the decision in DECISIONS.md.
4. Continue implementation only after the decision is established.

Keep implementation focused on the current task.

Do not modify unrelated parts of the project.

---

# FINAL PRODUCT GOAL

The completed system should allow a user to:

Company
→ Current available data
→ Earnings nowcast
→ Prediction range
→ Beat / Meet / Miss probability
→ Driver analysis
→ Forecast evolution
→ Historical validation
→ Alternative-data value analysis
→ Data freshness
→ Data provenance
→ Limitations

The final product should be presented as a serious financial research and intelligence platform.
