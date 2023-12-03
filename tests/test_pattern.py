import pytest
from congol.pattern import Pattern


@pytest.fixture
def blinker_pattern():
    return Pattern("Blinker", {(2, 1), (2, 2), (2, 3)})


def test_pattern_initialization(blinker_pattern):
    assert blinker_pattern.name == "Blinker"
    assert set(sorted(blinker_pattern.alive_cells)) == {(2, 1), (2, 2), (2, 3)}