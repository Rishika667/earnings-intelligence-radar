"""Stage 1 smoke tests.

These tests only verify that the project scaffold is structurally sound:
the package imports, module boundaries exist, and config templates parse.
They intentionally do NOT test any forecasting, data-ingestion, or model
behavior — that functionality does not exist yet (Stage 2+).
"""

from __future__ import annotations

import importlib
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_eir_package_imports():
    """The top-level package must import without error."""
    eir = importlib.import_module("eir")
    assert hasattr(eir, "__version__")


@pytest.mark.parametrize(
    "module_name",
    [
        "eir.schemas",
        "eir.config",
        "eir.ingestion",
        "eir.normalization",
        "eir.pit",
        "eir.quality",
        "eir.features",
        "eir.forecasting",
        "eir.forecasting.baseline",
        "eir.forecasting.statistical",
        "eir.forecasting.ml",
        "eir.uncertainty",
        "eir.attribution",
        "eir.altdata",
        "eir.validation",
        "eir.history",
        "eir.monitoring",
        "eir.reporting",
        "eir.utils",
    ],
)
def test_module_boundaries_import(module_name):
    """Every planned module boundary must at least import cleanly."""
    module = importlib.import_module(module_name)
    assert module is not None


def test_project_control_files_exist():
    """Required project-control files must be present and non-empty."""
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
        path = REPO_ROOT / filename
        assert path.exists(), f"Missing required project-control file: {filename}"
        assert path.stat().st_size > 0, f"Project-control file is empty: {filename}"


def test_directory_structure_exists():
    """Top-level architectural directories must exist."""
    required_dirs = [
        "src/eir",
        "data",
        "tests",
        "dashboard",
        "config",
        "docs",
    ]
    for rel_dir in required_dirs:
        path = REPO_ROOT / rel_dir
        assert path.is_dir(), f"Missing required directory: {rel_dir}"


def test_no_env_file_committed():
    """A real .env file (with potential secrets) must never be committed;
    only .env.example is allowed to exist as tracked scaffolding."""
    env_file = REPO_ROOT / ".env"
    assert not env_file.exists(), (
        ".env must not exist in the repository checkout — only .env.example "
        "should be committed."
    )
    assert (REPO_ROOT / ".env.example").exists()


def test_no_obvious_secrets_in_config_templates():
    """Config example files must not contain populated secret-like values.

    This is a lightweight structural check, not a full secret scanner:
    it verifies known credential fields are left blank/omitted rather
    than populated with a plausible-looking value.
    """
    config_dir = REPO_ROOT / "config"
    suspicious_markers = ["sk-", "AKIA", "-----BEGIN"]
    for path in config_dir.glob("*.yaml"):
        content = path.read_text(encoding="utf-8")
        for marker in suspicious_markers:
            assert marker not in content, f"Possible secret-like value in {path}"
