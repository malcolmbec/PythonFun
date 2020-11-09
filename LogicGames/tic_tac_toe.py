#!/usr/bin/env/python3
import argparse
from .GamePieces.Board import Board, Posn

parser = argparse.ArgumentParser(description='A simple game of Tic Tac Toe!')
parser.add_argument('-s', '--size', nargs=1, type=int, default=3, help='the size of the Tic Tac Toe board')
args = parser.parse_args()