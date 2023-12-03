"""
This module contains the implementation of the `Pattern` class. A pattern is a 
set of living cells. The seed for an instance of a game is the initial life 
pattern.
"""


class Pattern:
    def __init__(self, name: str, alive_cells: set[tuple[int, int]]):
        self.name = name
        self.alive_cells = alive_cells