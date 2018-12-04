import re
from collections import defaultdict

grid = defaultdict(int)

for line in open('input.txt'):
	number, x, y, width, height = map(int, re.findall('\d+', line))

	for i in range(x, x + width):
		for j in range(y, y + height):
			grid[(i, j)] += 1

print(sum(1 if element >= 2 else 0 for element in grid.values()))
