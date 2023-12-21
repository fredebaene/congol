from pathlib import Path
import pytest
from congol.pattern import Pattern


@pytest.fixture
def _PATTERNS_FILE():
    return Path(__file__).parent.parent / "data" / "patterns.toml"


def test_pattern_initialization(blinker_pattern):
    assert blinker_pattern.name == "Blinker"
    assert set(sorted(blinker_pattern.alive_cells)) == {(2, 1), (2, 2), (2, 3)}


def test_reading_patterns_from_toml(_PATTERNS_FILE):
    expected_res = {"Blinker": {"alive_cells": [[2, 1], [2, 2], [2, 3]]}}
    observed_res = Pattern.read_patterns_from_toml(_PATTERNS_FILE)
    assert expected_res == observed_res