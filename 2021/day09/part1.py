grid = {
	(row, col): int(char)
	for row, line in enumerate(open('input.txt'))
	for col, char in enumerate(line.strip())
}

total = 0

for row, col in grid:
	num = grid[row, col]

	total += 1 + num if all(
		(row2, col2) not in grid or grid[row2, col2] > num
		for row2, col2 in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
	) else 0

print(total)
