"""Configuration loading layer.

Non-secret configuration (companies, data sources, model parameters, app
settings) is loaded from YAML files under the repository's top-level
`config/` directory. Secrets/credentials are read only from environment
variables (optionally via a local, git-ignored `.env` file) — see
`eir.config.settings.get_env` and `.env.example` at the repo root.
"""

from eir.config.settings import AppSettings, get_env, load_env, load_yaml_config

__all__ = ["AppSettings", "get_env", "load_env", "load_yaml_config"]
