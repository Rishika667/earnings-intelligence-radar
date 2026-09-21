# Configuration Conventions

This directory holds **non-secret** configuration templates and (once
customized locally) working configuration files.

## Files

| Template | Purpose |
|---|---|
| `companies.example.yaml` | Company universe (ticker, CIK, sector, fiscal year end). |
| `data_sources.example.yaml` | Free/public data source connection parameters (URLs, rate limits, and the *name* of the environment variable holding any required credential — never the credential itself). |
| `model.example.yaml` | Forecasting/validation/uncertainty configuration shape for later stages. |
| `app.example.yaml` | General application/dashboard settings and data path conventions. |

## Usage convention

1. Copy `*.example.yaml` to the corresponding `*.yaml` file (e.g.
   `companies.example.yaml` -> `companies.yaml`) to create your own working
   configuration.
2. Edit the working copy locally. These working copies are permitted to be
   committed since they must never contain secrets — only the structural
   fields defined in the examples above.
3. `eir.config.settings.load_yaml_config()` looks for the non-`.example`
   filename first and falls back to the `.example` template if the working
   copy does not exist yet, so a fresh checkout remains runnable.

## Secrets

**No API keys, tokens, or passwords are ever stored in this directory or
anywhere else in the repository.**

Any data source that eventually requires a credential (e.g. a free FRED API
key) is referenced in `data_sources.example.yaml` only by the *name* of an
environment variable (e.g. `FRED_API_KEY`). The actual value is supplied at
runtime via:

- A real environment variable, or
- A local `.env` file at the repository root (git-ignored; see
  `.env.example` for the documented variable names).

See `src/eir/config/settings.py` for the loader that implements this
convention (`get_env`, `load_env`).
