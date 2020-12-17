#!/usr/bin/env/python3
import unittest
from unittest.mock import patch
from io import StringIO

from TicTacToe.tictactoe import TicTacToe, Player


class TestInit(unittest.TestCase):
	def test_init(self):
		tt = TicTacToe()
		self.assertIsNone(tt.board)
		self.assertIsNone(tt.size)
		self.assertEqual(tt.turn, Player.X)
		self.assertFalse(tt.game_over)
		self.assertIsNone(tt.winner)

	def test_board_neg(self):
		tt = TicTacToe()
		with self.assertRaises(ValueError, msg='Board size -1x-1 is invalid.'):
			tt._init_board(-1)

	def test_board_2x2(self):
		tt = TicTacToe()
		with self.assertRaises(ValueError, msg='Board size 2x2 is invalid.'):
			tt._init_board(2)

	def test_board_3x3(self):
		tt = TicTacToe()
		tt._init_board(3)
		self.assertEqual(tt.size, 3)
		self.assertEqual(tt.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

	def test_board_5x5(self):
		tt = TicTacToe()
		tt._init_board(5)
		self.assertEqual(tt.size, 5)
		self.assertEqual(tt.board, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])


class TestDisplay(unittest.TestCase):
	def test_space(self):
		tt = TicTacToe()
		self.assertEqual(tt._space_to_ascii(0), ' ')

	def test_space_x(self):
		tt = TicTacToe()
		self.assertEqual(tt._space_to_ascii(1), 'X')

	def test_space_o(self):
		tt = TicTacToe()
		self.assertEqual(tt._space_to_ascii(2), 'O')

	def test_display_new_game(self):
		tt = TicTacToe()
		tt._init_board(3)
		expected = "  |   |  \n" \
				   "---------\n" \
				   "  |   |  \n" \
				   "---------\n" \
				   "  |   |  \n"
		with patch('sys.stdout', new=StringIO()) as mock_out:
			tt._display_board()
			self.assertEqual(mock_out.getvalue(), expected)

	def test_display_mid_game(self):
		tt = TicTacToe()
		tt.size = 3
		tt.board = [[0, 1, 1], [2, 0, 2], [0, 0, 0]]
		expected = "  | X | X\n" \
				   "---------\n" \
				   "O |   | O\n" \
				   "---------\n" \
				   "  |   |  \n"
		with patch('sys.stdout', new=StringIO()) as mock_out:
			tt._display_board()
			self.assertEqual(mock_out.getvalue(), expected)

	def test_display_end_game(self):
		tt = TicTacToe()
		tt.size = 3
		tt.board = [[0, 1, 1], [2, 1, 2], [2, 2, 1]]
		expected = "  | X | X\n" \
				   "---------\n" \
				   "O | X | O\n" \
				   "---------\n" \
				   "O | O | X\n"
		with patch('sys.stdout', new=StringIO()) as mock_out:
			tt._display_board()
			self.assertEqual(mock_out.getvalue(), expected)


class TestTakeTurn(unittest.TestCase):
	def test_out_of_bounds(self):
		tt = TicTacToe()
		tt._init_board(3)
		self.assertFalse(tt._out_of_bounds((0, 2)))

	def test_out_of_bounds_lower(self):
		tt = TicTacToe()
		tt._init_board(3)
		self.assertTrue(tt._out_of_bounds((-1, 0)))

	def test_out_of_bounds_upper(self):
		tt = TicTacToe()
		tt._init_board(3)
		self.assertTrue(tt._out_of_bounds((0, 3)))

	def test_is_occupied(self):
		pass

	def test_is_occupied_x(self):
		pass

	def test_is_occupied_o(self):
		pass

	def test_take_turn(self):
		pass

	def take_turn_out_of_bounds(self):
		pass

	def take_turn_is_occupied(self):
		pass


class TestGameOver(unittest.TestCase):
	def test(self):
		pass


if __name__ == "__main__":
	unittest.main()