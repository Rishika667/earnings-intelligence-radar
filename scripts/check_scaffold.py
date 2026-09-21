#!/usr/bin/env python3
"""Lightweight Stage 1 scaffold check.

Run manually (`python scripts/check_scaffold.py`) as a quick sanity check
outside of pytest — e.g. right after cloning. Exits non-zero on failure.

This intentionally duplicates a small subset of tests/smoke checks in a
standalone script form for convenience; pytest remains the canonical test
runner (see tests/smoke/test_project_scaffold.py).
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))


def main() -> int:
    errors = []

    required_files = [
        "PROJECT_SPEC.md",
        "PROJECT_STATE.md",
        "DECISIONS.md",
        "BUILD_LOG.md",
        "HANDOFF.md",
        "README.md",
        ".gitignore",
    ]
    for filename in required_files:
        if not (REPO_ROOT / filename).exists():
            errors.append(f"Missing project-control file: {filename}")

    if (REPO_ROOT / ".env").exists():
        errors.append(".env file must not be committed/present in a clean checkout")

    try:
        import eir  # noqa: F401
        from eir.config import load_yaml_config

        for filename in [
            "companies.example.yaml",
            "data_sources.example.yaml",
            "model.example.yaml",
            "app.example.yaml",
        ]:
            load_yaml_config(filename)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Package/config import failed: {exc}")

    if errors:
        print("Scaffold check FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("Scaffold check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
