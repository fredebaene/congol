"""
This module implements a view which enables a user to interact with and play 
the game using a text-based user interface (TUI).
"""


from congol.grid import LifeGrid
from congol.pattern import Pattern
import curses
from time import sleep
from typing import Optional


__all__ = ["CursesView"]


class CursesView:
    def __init__(
            self,
            pattern: Pattern,
            bounds: tuple,
            gen: int = 10,
            frame_rate: int = 7):
        self.pattern = pattern
        self.bounds = bounds
        self.gen = gen
        self.frame_rate = frame_rate
        
    def show(self) -> None:
        curses.wrapper(self._draw)

    def _draw(self, screen) -> None:
        life_grid = LifeGrid(self.pattern)
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, life_grid.get_string_representation(self.bounds))
        except curses.error:
               raise ValueError(
                   f"Error: terminal too small for pattern '{self.pattern.name}'"
               )
        
        for _ in range(self.gen):
            life_grid.evolve()
            screen.addstr(0, 0, life_grid.get_string_representation(self.bounds))
            screen.refresh()
            sleep(1 / self.frame_rate)