"""
This module contains the implementation of the `LifeGrid` class. This class 
provides a blueprint for the grid and let's the grid evolve from generation to 
generation.
"""


from pattern import Pattern


_DELTAS = {
    "top_left": (-1, -1),
    "top_center": (0, -1),
    "top_right": (1, -1),
    "center_left": (-1, 0),
    "center_right": (1, 0),
    "bottom_left": (-1, 1),
    "bottom_center": (0, 1),
    "bottom_right": (1, 1),
}

class LifeGrid:
    def __init__(self, pattern: Pattern):
        self.pattern = pattern

    def evolve(self):
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
        self._count_dying_cells()
        self._count_surviving_cells()
        self._count_reproductive_cells()
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
        for x_coord in range(self._goi_bounds["min_x"], self._goi_bounds["max_x"] + 1):
            for y_coord in range(self._goi_bounds["min_y"], self._goi_bounds["max_y"] + 1):
                self._goi[(x_coord, y_coord)] = 0

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
            for x_delta, y_delta in _DELTAS.values():
                if (x + x_delta, y + y_delta) in self.pattern.alive_cells:
                    self._goi[(x, y)] += 1

    def _count_dying_cells(self) -> None:
        """
        This method lists and counts the living cells in the current grid of 
        interest that will die. A living cell dies if it has less than two 
        (underpopulation) or more than three (overpopulation) living 
        neighbors.
        """
        self._dying_cells = set()
        for cell in self._goi.keys():
            if (
                cell in self.pattern.alive_cells
                and not self._goi[cell] in {2, 3}
            ):
                self._dying_cells.add(cell)
        self._number_of_dying_cells = len(self._dying_cells)

    def _count_surviving_cells(self) -> None:
        """
        This method lists and counts the surviving cells in the current grid 
        of interest. Living cells survive if they have two or three living 
        neighbors.
        """
        self._surviving_cells = set()
        for cell in self._goi.keys():
            if (
                cell in self.pattern.alive_cells
                and self._goi[cell] in {2, 3}
            ):
                self._surviving_cells.add(cell)
        self._number_of_surviving_cells = len(self._surviving_cells)

    def _count_reproductive_cells(self) -> None:
        """
        This method lists and counts the non-living cells that become alive. A 
        non-living cell becomes alive if it has exactly three living neigbors.
        """
        self._reproductive_cells = set()
        for cell in self._goi.keys():
            if (
                not cell in self.pattern.alive_cells
                and self._goi[cell] == 3
            ):
                self._reproductive_cells.add(cell)
            self._number_of_reproductive_cells = len(self._reproductive_cells)

    def show_as_string(self, bounding_box):
        pass

    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"  -> living cells: {sorted(self.pattern.alive_cells)}"
        )