from math import prod
from typing import Set, Tuple


def get_basin(row_: int, col_: int, visited: Set[Tuple[int, int]] = None) -> Set[Tuple[int, int]]:
	visited = visited or set()

	if (row_, col_) in visited or (row_, col_) not in grid or grid[row_, col_] == 9:
		return set()

	visited.add((row_, col_))

	for row2, col2 in ((row_ - 1, col_), (row_ + 1, col_), (row_, col_ - 1), (row_, col_ + 1)):
		if (row2, col2) not in grid or grid[row2, col2] > grid[row_, col_]:
			visited |= get_basin(row2, col2, visited)

	return visited


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

basins = list(basins)
print(prod(sorted(map(len, basins))[-3:]))
print(prod(sorted(map(len, basins))[-3:]) == 736920)
