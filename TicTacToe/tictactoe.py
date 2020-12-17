#!/usr/bin/env/python3
from enum import Enum


class Player(Enum):
	X = 1
	O = 2


class TicTacToe:

	def __init__(self):
		self.size: tuple = None
		self.board: list = None
		self.turn: Player = Player.X
		self.game_over: bool = False
		self.winner: Player = None

	def _init_board(self, size: tuple) -> list:
		self.size = size
		self.board = [[0] * size[1] for _ in range(size[0])]

	@staticmethod
	def _space_to_ascii(space: int) -> str:
		if space:
			return Player(space)
		else:
			return " "

	def _display_board(self):
		for i, _ in enumerate(self.board):
			out = ''
			for j, space in enumerate(self.board[_]):
				out += self._space_to_ascii(space)
				if j < self.size[1]-1:
					out += ' | '
			if i < self.size[0]-1:
				print(''.ljust(self.size[1], '-'))

	def _out_of_bounds(self, pos: tuple) -> bool:
		return pos[0] < 0 or self.size[0] <= pos[0] or pos[1] < 0 or self.size[1] <= pos[1]

	def _is_occupied(self, pos: tuple) -> bool:
		if self._out_of_bounds(pos):
			raise ValueError(f'Position {pos} is out of bounds.')
		return self.board[pos[0]][pos[1]]

	def _take_turn(self, pos: tuple):
		if self._is_occupied(pos):
			raise ValueError(f'Position {pos} is occupied.')
		self.board[pos[0]][pos[1]] = self.turn.value

	def _is_game_over(self) -> bool:
		pass

	def run(self):
		pass
