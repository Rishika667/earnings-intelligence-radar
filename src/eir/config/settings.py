"""Application settings loader.

Conventions established in Stage 1 (see docs/ARCHITECTURE.md and
config/README.md):

- No secrets are ever stored in the repository or in YAML config files.
- Credentials, when a source eventually requires them (e.g. an API key
  with a generous free tier), are read exclusively from environment
  variables, optionally loaded from a local `.env` file that is
  git-ignored. `.env.example` documents the expected variable names
  without real values.
- Non-secret configuration (companies, data-source parameters, model
  parameters, app settings) lives in versioned YAML files under
  `config/` and `config/*.example.yaml` templates.

This module only implements loading/parsing for Stage 1. It does not
validate business rules beyond basic structural checks — richer
validation belongs to the consuming module (e.g. ingestion config
validation happens in eir.ingestion once that module exists).
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

try:  # python-dotenv is an optional convenience, not a hard dependency.
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - exercised only if dependency missing
    load_dotenv = None

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_DIR = REPO_ROOT / "config"


def load_env(env_file: Optional[Path] = None) -> None:
    """Load environment variables from a local .env file, if present.

    Never raises if the file is missing — absence of a .env file is the
    normal state for a fresh checkout, since only `.env.example` is
    committed.
    """
    if load_dotenv is None:
        return
    target = env_file or (REPO_ROOT / ".env")
    if target.exists():
        load_dotenv(dotenv_path=target)


def get_env(name: str, default: Optional[str] = None, required: bool = False) -> Optional[str]:
    """Read a single environment variable.

    Args:
        name: Environment variable name.
        default: Value to return if unset.
        required: If True, raise a RuntimeError when unset and no default
            is provided. Used for credentials that a later-stage module
            genuinely cannot function without.
    """
    value = os.environ.get(name, default)
    if required and value is None:
        raise RuntimeError(
            f"Required environment variable '{name}' is not set. "
            f"See .env.example for the expected configuration."
        )
    return value


def load_yaml_config(filename: str, config_dir: Path = CONFIG_DIR) -> Dict[str, Any]:
    """Load a single YAML configuration file from config_dir.

    Args:
        filename: File name relative to config_dir (e.g. "app.yaml").
        config_dir: Directory to load from (defaults to repo `config/`).

    Returns:
        Parsed YAML content as a dict. Returns an empty dict if the file
        contains no top-level mapping.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    path = config_dir / filename
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Config file {path} must contain a top-level mapping.")
    return data


@dataclass(frozen=True)
class AppSettings:
    """Non-secret application settings.

    Populated from config/app.yaml (or config/app.example.yaml as a
    fallback template — never used silently in place of real config for
    anything beyond local scaffolding checks).
    """

    app_name: str
    environment: str
    log_level: str
    timezone: str

    @classmethod
    def from_yaml(cls, filename: str = "app.yaml") -> "AppSettings":
        try:
            data = load_yaml_config(filename)
        except FileNotFoundError:
            data = load_yaml_config("app.example.yaml")
        return cls(
            app_name=data.get("app_name", "earnings-intelligence-radar"),
            environment=data.get("environment", "development"),
            log_level=data.get("log_level", "INFO"),
            timezone=data.get("timezone", "UTC"),
        )
