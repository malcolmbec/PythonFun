#!/usr/bin/env/python3
from enum import Enum


class Player(Enum):
	X = 1
	O = 2

	def __str__(self):
		return self.name


class TicTacToe:

	def __init__(self):
		self.size: int = None
		self.board: list = None
		self.turn: Player = Player.X
		self.game_over: bool = False
		self.winner: Player = None

	def _init_board(self, size: int) -> list:
		if size < 3:
			raise ValueError(f'Board size {size}x{size} is invalid.')
		self.size = size
		self.board = [[0] * size for _ in range(size)]

	@staticmethod
	def _space_to_ascii(space: int) -> str:
		if space:
			return str(Player(space))
		else:
			return " "

	def _display_board(self):
		for i, _ in enumerate(self.board):
			out = ''
			for j, space in enumerate(self.board[i]):
				out += self._space_to_ascii(space)
				if j < self.size-1:
					out += ' | '
			print(out)
			if i < self.size-1:
				print(''.ljust(self.size**2, '-'))

	def _out_of_bounds(self, pos: tuple) -> bool:
		return pos[0] < 0 or self.size <= pos[0] or pos[1] < 0 or self.size <= pos[1]

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
