from typing import List
from more_itertools import chunked


class ListTools:
	@staticmethod
	def replace(list_: List, old, new_) -> List:
		return [new_ if old == value else value for value in list_]

	@staticmethod
	def remove(list_: List, target) -> List:
		return [value for value in list_ if value != target]


def is_bingo(board):
	has_bingo_row = any(
		row.count(None) == len(row)
		for row in chunked(board, SIDE_LENGTH)
	)

	has_bingo_column = any(
		all(num is None for num in board[i::SIDE_LENGTH])
		for i in range(SIDE_LENGTH)
	)

	return has_bingo_row or has_bingo_column


SIDE_LENGTH = 5
input_file = 'input.txt'

pool = map(int, open(input_file).readlines()[0].split(','))

boards = chunked(
	map(int, open(input_file).read().split()[1:]),
	SIDE_LENGTH ** 2
)

for number in pool:
	boards = [ListTools.replace(board, number, None) for board in boards]

	for board in boards:
		if is_bingo(board):
			print(sum(ListTools.remove(board, None)) * number)
			exit()
