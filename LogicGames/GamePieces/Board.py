#!/usr/bin/env/python3
from typing import List, NamedTuple, Callable, Dict
Dimensions = List[int, int]


class Posn(NamedTuple):
    """ Represents a position on a game board as a (row, col) tuple. """
    r: int
    c: int


class Board:
    """
    Represents a game board as a grid of spaces indexed from 0 - N where N is the size of the board - 1.
    Indexes start from the top left and increase left-to-right and top-to-bottom.
    """

    def __init__(self):
        """ Initializes a game board. """
        self.size: Dimensions = []
        self.grid: List[List[int]] = {}
        pass

    def _init_rect_grid(self):
        """ Initializes the board as a rectangular grid. """
        pass

    def _init_hex_grid(self):
        """ Initializes the board as a hexagon grid. """
        pass

    def positions(self) -> List[Posn]:
        """ Returns a list of all positions on the board """
        pass

    def filter_positions(self, pos: List[Posn], func: Callable) -> List[Posn]:
        """
        Filters a list of positions using a given function of type position -> boolean.
        :param func: function to filter positions
        :param pos: list of positions
        :return: list of filtered positions
        """
        pass

    def _reachable_positions_hex(self, pos: Posn) -> List[List[Posn]]:
        """
        Find all reachable positions (via straight line) from the given position for a hexagon grid.
        :param pos: given position
        :return: list of list of positions
        """
        pass

    def _reachable_positions_rect(self, pos: Posn) -> List[List[Posn]]:
        """
        Find all reachable positions (via straight line) from the given position for a hexagon grid.
        :param pos: given position
        :return: list of list of positions
        """
        pass

    def reachable_positions(self, pos: Posn) -> List[List[Posn]]:
        """
        Find all reachable positions (via straight line) from the given position. Returns a list of positions reachable
        for every direction (including diagonals) in order of [up, up-left, up-right, down down-left, down-right].
        :param pos: given position
        :return: list of list of positions
        """
        pass
