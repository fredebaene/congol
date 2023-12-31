import pytest
from pathlib import Path
import tomllib
from congol.pattern import Pattern
from congol.grid import LifeGrid


@pytest.fixture
def test_patterns():
    patterns_file = Path("data/patterns.toml")
    with open(patterns_file, "rb") as f:
        return tomllib.load(f)


@pytest.fixture
def blinker_pattern(test_patterns):
    return Pattern(
        name="Blinker",
        alive_cells={
            tuple(cell) for cell in test_patterns["Blinker"]["alive_cells"]
        }
    )


@pytest.fixture
def blinker_grid(blinker_pattern):
    return LifeGrid(pattern=blinker_pattern)