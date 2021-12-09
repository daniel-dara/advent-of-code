from math import prod

grid = [[9] + list(map(int, list(line.strip()))) + [9] for line in open('input.txt')]
grid = [[9] * len(grid[0])] + grid + [[9] * len(grid[0])]

basins = []


def count_basin(row_: int, col_: int):
	num = grid[row_][col_]

	if num == 9:
		return set()

	total = {(row_, col_)}

	if num < grid[row_ - 1][col_]:
		total |= count_basin(row_ - 1, col_)

	if num < grid[row_ + 1][col_]:
		total |= count_basin(row_ + 1, col_)

	if num < grid[row_][col_ - 1]:
		total |= count_basin(row_, col_ - 1)

	if num < grid[row_][col_ + 1]:
		total |= count_basin(row_, col_ + 1)

	return total


for row in range(1, len(grid) - 1):
	for column in range(1, len(grid[row]) - 1):
		num = grid[row][column]

		if (
			num < grid[row - 1][column] and
			num < grid[row + 1][column] and
			num < grid[row][column - 1] and
			num < grid[row][column + 1]
		):
			basins.append(count_basin(row, column))

# print(basins)
print(prod(sorted(map(len, basins))[-3:]))
