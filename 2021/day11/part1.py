from itertools import product
from typing import Set, Tuple


def increment(row: int, col: int, flashed_: Set[Tuple[int, int]]) -> int:
	if (row, col) not in grid or (row, col) in flashed_:
		return 0

	grid[row, col] += 1

	if grid[row, col] > 9:
		grid[row, col] = 0
		flashed_.add((row, col))

		return 1 + sum(
			increment(row - row_delta, col - col_delta, flashed_)
			for row_delta, col_delta in set(product((-1, 0, 1), repeat=2)) - {0, 0}
		)

	return 0


grid = {
	(row, col): char
	for row, line in enumerate(open('input.txt'))
	for col, char in enumerate(map(int, line.strip()))
}
total = 0

for _ in range(100):
	flashed = set()
	total += sum(increment(row, col, flashed) for row, col in grid)

print(total)
