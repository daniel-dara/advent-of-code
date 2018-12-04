import re
from collections import defaultdict
from functools import reduce

grid = defaultdict(list)
noOverlap = set()

for line in open('input.txt'):
	number, x, y, width, height = map(int, re.findall('\d+', line))

	noOverlap.add(number)

	for i in range(x, x + width):
		for j in range(y, y + height):
			grid[(i, j)].append(number)

for numbers in grid.values():
	if len(numbers) > 1:
		noOverlap = noOverlap.difference(set(numbers))

print(next(iter(noOverlap)))
