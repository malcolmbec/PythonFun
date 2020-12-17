#!/usr/bin/env/python3
import unittest

from TicTacToe.tictactoe import TicTacToe, Player


class TestInit(unittest.TestCase):
	def test_init(self):
		tt = TicTacToe()
		self.assertIsNone(tt.board)
		self.assertIsNone(tt.size)
		self.assertEqual(tt.turn, Player.X)
		self.assertFalse(tt.game_over)
		self.assertIsNone(tt.winner)

	def test_board_3x3(self):
		board = TicTacToe()._init_board()


class TestDisplay(unittest.TestCase):
	def test(self):
		pass


class TestTakeTurn(unittest.TestCase):
	def test(self):
		pass


class TestGameOver(unittest.TestCase):
	def test(self):
		pass


if __name__ == "__main__":
	unittest.main()