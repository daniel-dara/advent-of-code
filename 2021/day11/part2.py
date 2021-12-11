
total = 0
flashed = set()

grid = [
	list(map(int, line.strip()))
	for line in open('input.txt')
]


def incr(row, col):
	global total, flashed

	if (row, col) in flashed or row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
		return

	grid[row][col] += 1

	if grid[row][col] > 9:
		total += 1
		grid[row][col] = 0
		flashed.add((row, col))
		incr(row - 1, col)
		incr(row + 1, col)
		incr(row, col - 1)
		incr(row, col + 1)
		incr(row - 1, col - 1)
		incr(row - 1, col + 1)
		incr(row + 1, col + 1)
		incr(row + 1, col - 1)


for step in range(100000):
	flashed = set()
	total = 0

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			incr(row, col)

	if len(flashed) == len(grid) * len(grid[0]):
		print(step + 1)
		exit()

# print(total)
