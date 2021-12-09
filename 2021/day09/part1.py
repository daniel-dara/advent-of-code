grid = {
	(row, col): int(char)
	for row, line in enumerate(open('input.txt'))
	for col, char in enumerate(line.strip())
}

print(
	sum(
		1 + grid[row, col]
		for row, col in grid
		if all(
			(row2, col2) not in grid or grid[row2, col2] > grid[row, col]
			for row2, col2 in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
		)
	)
)
