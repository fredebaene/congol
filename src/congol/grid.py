"""
This module contains the implementation of the `LifeGrid` class. This class 
provides a blueprint for the grid and let's the grid evolve from generation to 
generation.
"""


from congol.pattern import Pattern
from typing import Optional


_DELTAS = {
    (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
}
_DEAD_CELL = "‧"
_ALIVE_CELL = "♥"


class LifeGrid:
    def __init__(self, pattern: Pattern):
        self.pattern = pattern

    def evolve(self) -> None:
        """
        This method enables a life pattern to evolve to the next generation 
        taking into account the following rules:

        - alive cells die if they have fewer than two (underpopulation) or 
          more than three living neighbors (overpopulation)
        - alive cells stay alive if they have two or three living neighbors
        - dead cells with exactly three living neighbors become alive 
          (reproduction).
        """
        self._get_grid_of_interest()
        self._count_living_neighbors()
        self._list_cells_next_generation()
        self._count_cells_next_generation()
        self.pattern.alive_cells = (
            self._surviving_cells.union(self._reproductive_cells)
        )

    def _get_grid_of_interest(self) -> None:
        """
        This method creates a dictionary in which the keys are tuples that 
        represent the coordinates of the cells in the grid of interest.
        """
        # Get the bounds of the grid of interest
        self._get_bounds()

        # Create a dictionary holding all cells in the grid of interest. THe 
        # values for each cell represent the number of living neighboring 
        # cells.
        self._goi = {}
        for x in range(self._goi_bounds["min_x"], self._goi_bounds["max_x"] + 1):
            for y in range(self._goi_bounds["min_y"], self._goi_bounds["max_y"] + 1):
                self._goi[(x, y)] = 0

    def _get_bounds(self) -> None:
        """
        This method gets the minimum and maximum x and y coordinates of the 
        current set of living cells. These minimum and maximum values can be 
        considered the bounds of the grid of interest.
        """
        self._goi_bounds = {
            "min_x": min([x for x, y in self.pattern.alive_cells]) - 1,
            "max_x": max([x for x, y in self.pattern.alive_cells]) + 1,
            "min_y": min([y for x, y in self.pattern.alive_cells]) - 1,
            "max_y": max([y for x, y in self.pattern.alive_cells]) + 1,
        }

    def _count_living_neighbors(self) -> None:
        """
        This method counts the number of living neighboring cells for each 
        cell in the grid of interest.
        """
        for x, y in self._goi.keys():
            for x_delta, y_delta in _DELTAS:
                if (x + x_delta, y + y_delta) in self.pattern.alive_cells:
                    self._goi[(x, y)] += 1

    def _list_cells_next_generation(self) -> None:
        """
        This method lists the dying cells, the surviving cells, and the 
        reproductive cells:
        
        - dying cells: the living cells that will die
        - surviving cells:  the living cells that will keep on living
        - reproductive cells: the dead cells that will become alive.

        The number of cells per subgroup can be calculated using the 
        `._count_cells_next_generation()` method.
        """
        # Initialize empty sets that will contain the different subgroups of 
        # cells
        self._dying_cells = set()
        self._surviving_cells = set()
        self._reproductive_cells = set()

        # Assess the status for each cell in the current grid of interest in 
        # the next generation
        for cell in self._goi.keys():
            if (
                cell in self.pattern.alive_cells
                and not self._goi[cell] in {2, 3}
            ):
                self._dying_cells.add(cell)
            elif (
                cell in self.pattern.alive_cells
                and self._goi[cell] in {2, 3}
            ):
                self._surviving_cells.add(cell)
            elif (
                not cell in self.pattern.alive_cells
                and self._goi[cell] == 3
            ):
                self._reproductive_cells.add(cell)

    def _count_cells_next_generation(self) -> None:
        """
        This method counts the number of cells per subgroup for the next 
        generation.
        """
        # Count the number of cells per subgroup
        self._number_of_dying_cells = len(self._dying_cells)
        self._number_of_surviving_cells = len(self._surviving_cells)
        self._number_of_reproductive_cells = len(self._reproductive_cells)

    def get_string_representation(self, bounds: Optional[tuple] = None) -> str:
        """
        This method creates a string representation of the life grid, with 
        different cell shapes for living and dead cells.

        Returns:
            str: a string representation of the life grid.
        """
        # Get the bounds of the life grid to be represented as a string
        if bounds is None:
            self._get_bounds()
            min_x, max_x = self._goi_bounds["min_x"], self._goi_bounds["max_x"]
            min_y, max_y = self._goi_bounds["min_y"], self._goi_bounds["max_y"]
        else:
            min_x, max_x, min_y, max_y = bounds

        # Initialize an empty string and start constructing it.
        life_grid = ""
        
        for i in range(min_x, max_x + 1):
            life_grid_row = ""
            for j in range(min_y, max_y + 1):
                cell = (i, j)
                if cell in self.pattern.alive_cells:
                    life_grid_row += _ALIVE_CELL + " "
                else:
                    life_grid_row += _DEAD_CELL + " "
            life_grid_row += "\n"
            life_grid += life_grid_row

        return life_grid

    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"-> living cells: {sorted(self.pattern.alive_cells)}"
        )