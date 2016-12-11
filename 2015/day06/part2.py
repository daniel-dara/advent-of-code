import re

grid = [[0] * 1000 for y in range(1000)]

for line in open('input.txt'):
	x1, y1, x2, y2 = map(int, re.search(r'(\d+),(\d+)[^\d]*(\d+),(\d+)', line).groups())

	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			if grid[x][y] > 0 or not line.startswith('turn off'):
				grid[x][y] += 1 if line.startswith('turn on') else -1 if line.startswith('turn off') else 2

print(sum(map(sum, grid)))