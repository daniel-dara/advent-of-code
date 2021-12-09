from math import prod
from typing import Set, Tuple


def get_basin(row_: int, col_: int) -> Set[Tuple[int, int]]:
	if (row_, col_) not in grid or grid[row_, col_] == 9:
		return set()

	points = {(row_, col_)}

	for row2, col2 in ((row_ - 1, col_), (row_ + 1, col_), (row_, col_ - 1), (row_, col_ + 1)):
		if (row2, col2) not in grid or grid[row2, col2] > grid[row_, col_]:
			points |= get_basin(row2, col2)

	return points


grid = {
	(row, col): int(char)
	for row, line in enumerate(open('input.txt'))
	for col, char in enumerate(line.strip())
}

basins = (
	get_basin(row, col)
	for row, col in grid
	if all(
		(row2, col2) not in grid or grid[row2, col2] > grid[row, col]
		for row2, col2 in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
	)
)

print(prod(sorted(map(len, basins))[-3:]))
