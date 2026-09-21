# Data Directory

This directory holds local, git-ignored working data. Only directory
structure (`.gitkeep` placeholders) is committed — actual data files are
not, per `.gitignore` (`data/raw/` is explicitly ignored; other
subdirectories hold intermediate/derived artifacts that are also treated
as local/regenerable rather than committed).

Layout mirrors the architectural data-flow stages (see
`docs/ARCHITECTURE.md`):

| Directory | Contents | Produced by |
|---|---|---|
| `raw/` | Minimally-parsed source payloads (`RawObservation`). | `eir.ingestion` |
| `normalized/` | Unit-converted, canonically-named data, may still contain multiple revisions (`NormalizedObservation`). | `eir.normalization` |
| `pit/` | Point-in-time snapshots — "what was known as of date X" (`PitObservation`). | `eir.pit` |
| `features/` | Modeling-ready derived features (`FeatureValue`). | `eir.features` |
| `forecasts/` | Model outputs and forecast history (`ForecastResult`, `ForecastHistoryEntry`). | `eir.forecasting`, `eir.uncertainty`, `eir.history` |
| `validation/` | Walk-forward evaluation results (`ValidationResult`). | `eir.validation` |

No data files are populated at Stage 1. Ingestion begins in Stage 2.
