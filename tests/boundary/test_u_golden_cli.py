"""CLI golden master — UI Track (U-*). Phase: GREEN baseline."""

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from boundary.cli import main

_GOLDEN_PATH = Path(__file__).resolve().parent.parent / "golden" / "cli_scenarios.json"


_GOLDEN_SCENARIOS = json.loads(_GOLDEN_PATH.read_text(encoding="utf-8"))["scenarios"]


@pytest.mark.parametrize(
    "scenario",
    _GOLDEN_SCENARIOS,
    ids=[s["id"] for s in _GOLDEN_SCENARIOS],
)
def test_golden_cli_scenario(scenario: dict, capsys):
    """GM-* | cli_scenarios.json | REFACTOR 회귀 검출용 characterization."""
    with patch("builtins.input", return_value=scenario["input"]):
        main()
    output = capsys.readouterr().out.strip().splitlines()
    assert output == scenario["output_lines"]
