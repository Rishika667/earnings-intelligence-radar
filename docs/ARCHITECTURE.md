# Earnings Intelligence Radar — Technical Architecture

Status: Stage 1 — Architecture + Project Scaffold.
This document describes the architecture established at Stage 1. It
defines module boundaries and data contracts; it does not describe
functionality that does not exist yet (that functionality is called out
explicitly as "future work" below).

See `PROJECT_SPEC.md` for the product requirements this architecture is
designed to satisfy, and `PROJECT_STATE.md` / `BUILD_LOG.md` for current
progress.

---

## 1. Design principles

1. **Free/public data only.** No module may require a paid API or
   proprietary dataset to function (PROJECT_SPEC.md section 4).
2. **Point-in-time correctness is structural, not incidental.** The
   pipeline has an explicit PIT layer (`eir.pit`) between normalization
   and feature engineering, so look-ahead bias is prevented by data flow,
   not by developer discipline alone.
3. **Model probability and data confidence are different things.**
   `ForecastResult` keeps `beat_probability` / `meet_probability` /
   `miss_probability` (from calibration/validation) structurally separate
   from `data_confidence` (from data-quality/provenance). See
   DECISIONS.md Decision 005.
4. **Research/engineering logic is fully separate from presentation.**
   `src/eir/*` contains no Streamlit code; `dashboard/*` contains no
   forecasting/ingestion/validation logic.
5. **Validation claims must be traceable.** Any reported model
   performance must come from a `ValidationResult` produced by
   `eir.validation`'s walk-forward evaluation — never asserted informally.
6. **Negative findings are first-class.** `ValidationResult` has an
   explicit `is_negative_finding` flag so weak/failed alternative-data
   tests are easy to surface, not hidden.
7. **Minimal dependencies at each stage.** Only add a dependency when the
   stage that needs it is actually being implemented (see
   `pyproject.toml` comments).

---

## 2. Directory structure

```
webapp/
├── src/eir/                 Research/engineering package (importable as `eir`)
│   ├── config/              Non-secret config loading + env var conventions
│   ├── schemas/             Data contracts (raw, normalized, pit, features,
│   │                        forecast, forecast history, validation, provenance)
│   ├── ingestion/           Stage 2: pull data from free/public sources
│   ├── normalization/       Stage 2: unit conversion, canonical naming
│   ├── pit/                 Stage 2: point-in-time "as known at date X" views
│   ├── quality/             Stage 2/6: data-quality + provenance scoring
│   ├── features/            Stage 2/5: feature engineering
│   ├── forecasting/         Stage 3: baseline / statistical / ml models
│   │   ├── baseline/
│   │   ├── statistical/
│   │   └── ml/
│   ├── uncertainty/         Stage 4: prediction ranges + calibrated probabilities
│   ├── attribution/         Stage 5: driver attribution / explanation
│   ├── altdata/              Stage 5: alternative-data incremental-value testing
│   ├── validation/          Stage 3+: chronological walk-forward evaluation
│   ├── history/             Stage 6: forecast history / information timeline
│   ├── monitoring/          Stage 6: data freshness monitoring
│   ├── reporting/           Stage 7: research report assembly (no UI code)
│   └── utils/               Small shared helpers only
│
├── dashboard/               Streamlit presentation layer (Stage 7)
│   ├── app.py               Entrypoint (placeholder at Stage 1)
│   ├── pages/                Per-feature dashboard pages
│   └── components/          Reusable chart/table components
│
├── data/                    Local, mostly git-ignored data artifacts
│   ├── raw/  normalized/  pit/  features/  forecasts/  validation/
│
├── config/                  Non-secret config templates (*.example.yaml)
│
├── tests/
│   ├── smoke/               Structural/import smoke tests
│   └── unit/                Unit tests for schemas/config
│
├── docs/                    This file and future architecture notes
├── scripts/                 Small operational/dev scripts
├── .env.example             Documented environment variable names (no values)
├── pyproject.toml / requirements.txt / pytest.ini
└── PROJECT_SPEC.md, PROJECT_STATE.md, DECISIONS.md, BUILD_LOG.md,
    HANDOFF.md, README.md    Project-control files (source of truth)
```

---

## 3. Module responsibilities and data flow

The end-to-end data flow, matching PROJECT_SPEC.md section 15
(`Data → Features → Forecast → Probability → Explanation → Validation →
Intelligence`):

```
                 ┌───────────────┐
 free/public     │  ingestion    │  RawObservation
 sources ───────▶│  (Stage 2)    │──────────────┐
                 └───────────────┘              │
                                                 ▼
                 ┌───────────────┐   NormalizedObservation
                 │ normalization │◀──────────────┘
                 │  (Stage 2)    │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐   PitObservation
                 │      pit      │   ("known as of date X")
                 │  (Stage 2)    │
                 └───────┬───────┘
                         │
             ┌───────────┼────────────┐
             ▼                        ▼
     ┌───────────────┐        ┌───────────────┐
     │    quality     │        │   features    │  FeatureValue
     │ (Stage 2/6)    │        │ (Stage 2/5)   │
     └───────┬───────┘        └───────┬───────┘
             │                        │
             │                        ▼
             │                ┌───────────────┐
             │                │  forecasting   │  ForecastResult (point estimate)
             │                │   (Stage 3)    │  baseline → statistical → ml
             │                └───────┬───────┘
             │                        │
             │                        ▼
             │                ┌───────────────┐
             └───────────────▶│  uncertainty   │  + PredictionRange
              data_confidence │   (Stage 4)    │  + calibrated beat/meet/miss
                              └───────┬───────┘
                                      │
                        ┌─────────────┼─────────────┐
                        ▼             ▼             ▼
                ┌──────────────┐┌───────────┐┌───────────────┐
                │ attribution  ││ altdata   ││  validation    │
                │  (Stage 5)   ││ (Stage 5) ││ (Stage 3+)     │
                └──────────────┘└───────────┘└───────┬───────┘
                                                       │ ValidationResult
                                      ┌────────────────┴───────────────┐
                                      ▼                                ▼
                              ┌──────────────┐                ┌───────────────┐
                              │   history    │                │  monitoring   │
                              │  (Stage 6)   │                │  (Stage 6)    │
                              └──────┬───────┘                └───────┬───────┘
                                     └───────────────┬────────────────┘
                                                      ▼
                                              ┌───────────────┐
                                              │   reporting    │  (Stage 7, no UI code)
                                              │   (Stage 7)   │
                                              └───────┬───────┘
                                                      ▼
                                              ┌───────────────┐
                                              │   dashboard    │  Streamlit (Stage 7)
                                              └───────────────┘
```

Notes:
- `uncertainty` consumes `validation`'s historical `ValidationResult`
  output to calibrate probabilities — validation must run before
  calibrated probabilities can exist for a given model.
- `attribution` and `altdata` both sit downstream of forecasting/
  validation but serve different questions: attribution explains a single
  forecast; altdata evaluates whether a feature group helps across many
  forecasts.
- `dashboard` only talks to `reporting` (and, pragmatically, may read
  stored `ForecastResult`/`ValidationResult`/history records directly for
  display) — it never re-implements ingestion/modeling/validation logic.

---

## 4. Data contracts summary

Defined in `src/eir/schemas/`:

| Contract | File | Represents |
|---|---|---|
| `ProvenanceRecord` | `provenance.py` | Source, retrieval time, vintage, freshness, quality notes — attached to other records rather than merged in. |
| `RawObservation` | `raw.py` | Minimally-parsed source payload. |
| `NormalizedObservation` | `normalized.py` | Unit-converted, canonically-named; may still contain multiple revisions. |
| `PitObservation` | `pit.py` | "What was known as of `as_of_date`" — the look-ahead-bias firewall. |
| `FeatureValue` | `features.py` | Modeling-ready derived signal, tied to `as_of_date` + `target_period_end`. |
| `ForecastResult` | `forecast.py` | Point estimate + optional range/probabilities/drivers/data_confidence for one company/period/as_of_date. |
| `ForecastHistoryEntry` | `forecast.py` | Append-only pointer for reconstructing forecast evolution. |
| `ValidationResult` | `validation.py` | Walk-forward evaluation output — the only sanctioned source of performance claims. |

Enums/shared vocabulary in `common.py`: `DataSourceId`, `FreshnessStatus`,
`OutcomeLabel`, `ForecastModelType`, `ValidationScheme`.

These are Stage 1 architectural definitions. Field names/types may be
refined in Stage 2+ as real data is integrated, but changes should be
documented in `DECISIONS.md` per HANDOFF.md's change policy.

---

## 5. Configuration architecture

- **Non-secret configuration** (`config/*.example.yaml`): companies, data
  source parameters, model/validation parameters, app settings. Loaded via
  `eir.config.settings.load_yaml_config`, which falls back to the
  `.example` template if no local working copy exists.
- **Secrets**: never stored in the repo. Referenced in config only by
  environment-variable *name* (e.g. `api_key_env_var: "FRED_API_KEY"`),
  resolved at runtime via `eir.config.settings.get_env`, optionally loaded
  from a local, git-ignored `.env` (see `.env.example`).

See `config/README.md` for the full convention.

---

## 6. Testing architecture

- `tests/smoke/`: verifies the package imports, all module boundaries
  import, project-control files exist, no `.env` is committed, and config
  templates don't contain obviously secret-like values.
- `tests/unit/`: verifies schema dataclasses construct correctly with
  sane defaults (e.g. optional probability/range fields default to
  `None`/empty rather than fabricated values), and that the config loader
  parses templates and enforces the env-var-reference convention for
  credentials.

No test fabricates or asserts financial results, forecast accuracy, or
model performance — there is no model yet to test.

---

## 7. Stage dependency map

| Stage | Depends on | Adds |
|---|---|---|
| 2 — Data Foundation | Stage 1 schemas/config | `ingestion`, `normalization`, `pit`, `quality` implementations |
| 3 — Forecasting Engine | Stage 2 features | `forecasting/*`, `validation` walk-forward runner |
| 4 — Uncertainty Engine | Stage 3 validation output | `uncertainty` calibration |
| 5 — Research Intelligence | Stage 3/4 | `attribution`, `altdata` |
| 6 — Monitoring and Trust Layer | Stage 2 quality + Stage 3 history data | `history`, `monitoring` |
| 7 — Productization | All prior stages | `reporting`, `dashboard` |

This scaffold is intended to let each stage add implementation inside its
already-reserved module without restructuring the repository.
