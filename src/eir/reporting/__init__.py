"""Research reporting layer.

Responsibility boundary:
    - Assemble research-report-style summaries (e.g. model comparison
      write-ups, alternative-data findings, limitations sections) from
      ValidationResult / ForecastResult / history data.
    - Produce artifacts consumed by the dashboard or exported directly
      (e.g. Markdown/HTML research notes), but contains no Streamlit or
      other UI-framework code itself — that boundary is deliberate so
      reporting logic stays testable and reusable outside the dashboard.

Explicitly NOT this layer's responsibility:
    - Rendering UI widgets -> dashboard/
    - Computing the underlying results -> eir.forecasting / eir.validation
      / eir.altdata

Status: Stage 1 — module boundary only, no implementation yet.
"""
