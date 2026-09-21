# Scripts

Small operational/development scripts. Kept minimal by design.

- `check_scaffold.py` — quick manual sanity check that the project
  scaffold is structurally intact (project-control files present, no
  `.env` committed, package + config templates importable/parseable).
  Run: `python scripts/check_scaffold.py`. The canonical, more thorough
  checks live in `tests/smoke/` (run via `pytest`).
