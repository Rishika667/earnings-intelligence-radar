# earnings-intelligence-radar
Near-real-time earnings nowcasting and alternative-data intelligence platform using free public financial and economic data.

## Project status

Stage 1 — Architecture + Project Scaffold. See `PROJECT_STATE.md` for
current status, `docs/ARCHITECTURE.md` for the technical architecture,
and `HANDOFF.md` for how to continue this project in a new AI session.

## Repository layout (Stage 1)

- `src/eir/` — research/engineering package (data contracts + module
  boundaries for ingestion, normalization, point-in-time handling,
  features, forecasting, uncertainty, attribution, alt-data research,
  validation, forecast history, monitoring, reporting).
- `dashboard/` — Streamlit presentation layer (placeholder; Stage 7).
- `config/` — non-secret configuration templates (`*.example.yaml`).
- `data/` — local data directories (mostly git-ignored).
- `tests/` — smoke and unit tests.
- `docs/ARCHITECTURE.md` — full technical architecture.

## Development setup

```bash
pip install -e ".[dev]"
cp .env.example .env   # fill in local, free-tier credentials only
pytest
```

No paid data sources or secrets are required to run the Stage 1 scaffold.
