from more_itertools import chunked

SIDE_LENGTH = 5
input_file = 'example.txt'
# input_file = 'input.txt'

pool = map(int, open(input_file).readlines()[0].split(','))


def is_bingo(board):
	for chunk in chunked(board, SIDE_LENGTH):
		if chunk.count(None) == SIDE_LENGTH:
			return True

	for i in range(SIDE_LENGTH):
		if [num for num in board[i::SIDE_LENGTH]].count(None) == SIDE_LENGTH:
			return True

	return False


board_data = (
	map(int, open(input_file).read().split()[1:])
)

boards = list(chunked(board_data, SIDE_LENGTH ** 2))

for number in pool:
	j = 0
	while j < len(boards):
		board = boards[j]

		for i in range(len(board)):
			if board[i] == number:
				board[i] = None

		if is_bingo(board):
			if len(boards) > 1:
				boards.pop(j)
				j -= 1
			else:
				print(sum(filter(lambda x: x is not None, board)) * number)
				exit()

		j += 1
