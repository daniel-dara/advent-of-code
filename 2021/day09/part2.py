from math import prod


def get_basin_size(row_: int, col_: int) -> int:
	if (row_, col_) not in grid or grid[row_, col_] == 9:
		return 0

	grid[row_, col_] = 9

	return 1 + sum(
		get_basin_size(row2, col2)
		for row2, col2 in ((row_ - 1, col_), (row_ + 1, col_), (row_, col_ - 1), (row_, col_ + 1))
	)


grid = {
	(row, col): int(char)
	for row, line in enumerate(open('input.txt'))
	for col, char in enumerate(line.strip())
}

basin_sizes = (
	get_basin_size(row, col)
	for row, col in grid
	if grid[row, col] != 9
)

print(prod(sorted(basin_sizes)[-3:]))
