import pytest
from congol.pattern import Pattern


def test_pattern_initialization(blinker_pattern):
    assert blinker_pattern.name == "Blinker"
    assert set(sorted(blinker_pattern.alive_cells)) == {(2, 1), (2, 2), (2, 3)}