from copy import deepcopy

gridSize = 100
steps = 100
grid = [['.'] * (gridSize + 2)]
offsets = [-1, 0, 1]
stuckPoints = ((1, 1), (1, gridSize), (gridSize, 1), (gridSize, gridSize))

for line in open('input.txt'):
	grid.append(list('.' + line.rstrip() + '.'))

grid += [['.'] * (gridSize + 2)]

for point in stuckPoints:
	r, c = point
	grid[r][c] = '#'

def calcConfig(i, j):
	totalOn = 0

	for r in offsets:
		for c in offsets:
			if r or c:
				totalOn += 1 if grid[i + r][j + c] == '#' else 0

	if grid[i][j] == '#':
		return '#' if totalOn in [2, 3] else '.'
	else:
		return '#' if totalOn == 3 else '.'

for _ in range(steps):
	nextGrid = deepcopy(grid)

	for i in range(1, gridSize + 1):
		for j in range(1, gridSize + 1):
			if (i, j) not in stuckPoints:
				nextGrid[i][j] = calcConfig(i, j)

	grid = nextGrid

print(sum(row.count('#') for row in grid))
