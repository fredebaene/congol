import pytest
from congol.grid import LifeGrid


def test_grid_initialization(blinker_pattern):
    life_grid = LifeGrid(pattern=blinker_pattern)
    assert life_grid.pattern.name == "Blinker"
    assert (
        set(sorted(life_grid.pattern.alive_cells)) == {(2, 1), (2, 2), (2, 3)}
    )


def test_get_bounds(blinker_grid):
    blinker_grid._get_bounds()
    assert blinker_grid._goi_bounds == {
        "min_x": 1, "max_x": 3, "min_y": 0, "max_y": 4
    }


def test_get_grid_of_interest(blinker_grid):
    grid_of_interest = {
        (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0,
        (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0,
        (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0,
    }
    blinker_grid._get_grid_of_interest()
    assert blinker_grid._goi == grid_of_interest