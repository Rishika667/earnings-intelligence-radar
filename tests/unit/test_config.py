"""Structural validity tests for the Stage 1 configuration loading layer."""

from __future__ import annotations

import pytest

from eir.config import AppSettings, get_env, load_yaml_config


def test_load_yaml_config_example_templates_parse():
    """All committed *.example.yaml templates must parse as valid YAML
    mappings."""
    for filename in [
        "companies.example.yaml",
        "data_sources.example.yaml",
        "model.example.yaml",
        "app.example.yaml",
    ]:
        data = load_yaml_config(filename)
        assert isinstance(data, dict)
        assert len(data) > 0


def test_load_yaml_config_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_yaml_config("does_not_exist.yaml")


def test_app_settings_falls_back_to_example_template():
    """When no local app.yaml override exists, AppSettings must fall back
    to app.example.yaml rather than failing, so a fresh checkout works."""
    settings = AppSettings.from_yaml()
    assert settings.app_name == "earnings-intelligence-radar"
    assert settings.environment in {"development", "production"}


def test_get_env_returns_default_when_unset(monkeypatch):
    monkeypatch.delenv("EIR_TEST_VAR_DOES_NOT_EXIST", raising=False)
    assert get_env("EIR_TEST_VAR_DOES_NOT_EXIST", default="fallback") == "fallback"


def test_get_env_required_raises_when_missing(monkeypatch):
    monkeypatch.delenv("EIR_TEST_REQUIRED_VAR", raising=False)
    with pytest.raises(RuntimeError):
        get_env("EIR_TEST_REQUIRED_VAR", required=True)


def test_data_sources_config_never_contains_literal_api_key_field():
    """Data source config must reference credentials only via
    *_env_var keys, never a literal api_key/token value."""
    data = load_yaml_config("data_sources.example.yaml")
    for source_name, source_cfg in data["data_sources"].items():
        for key in source_cfg:
            if key in {"api_key", "token", "password", "secret"}:
                pytest.fail(
                    f"data_sources.example.yaml source '{source_name}' has a "
                    f"literal credential field '{key}' — credentials must be "
                    f"referenced via an *_env_var key instead."
                )
