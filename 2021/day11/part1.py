from itertools import product
from typing import Set, Tuple


def increment(row: int, col: int, flashed: Set[Tuple[int, int]]) -> int:
	if (row, col) in flashed or row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
		return 0

	grid[row][col] += 1

	if grid[row][col] > 9:
		grid[row][col] = 0
		flashed.add((row, col))

		return 1 + sum(
			increment(row - row_delta, col - col_delta, flashed)
			for row_delta, col_delta in set(product((-1, 0, 1), repeat=2)) - {0, 0}
		)

	return 0


grid = [
	list(map(int, line.strip()))
	for line in open('input.txt')
]
total = 0

for _ in range(100):
	flashed = set()

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			total += increment(row, col, flashed)

print(total)
