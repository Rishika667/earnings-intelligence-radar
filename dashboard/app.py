"""Streamlit dashboard entrypoint — placeholder.

Stage 1 status: this file intentionally implements no dashboard
functionality yet. It exists to establish the entrypoint location and to
document the presentation/research separation rule (see
dashboard/README.md and docs/ARCHITECTURE.md).

Real dashboard pages are Stage 7 (Productization) work, built once
forecasting (Stage 3), uncertainty (Stage 4), alternative-data research
(Stage 5), and monitoring (Stage 6) exist to display.

Do not add forecasting, ingestion, or validation logic to this file or
anything under dashboard/ — that logic belongs in `src/eir`.
"""

import streamlit as st

st.set_page_config(page_title="Earnings Intelligence Radar", layout="wide")


def main() -> None:
    st.title("Earnings Intelligence Radar")
    st.info(
        "Dashboard not yet implemented. This project is currently at "
        "Stage 1 — Architecture + Project Scaffold. See PROJECT_STATE.md "
        "for current status."
    )


if __name__ == "__main__":
    main()
