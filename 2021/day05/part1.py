import re
from collections import defaultdict

graph = defaultdict(int)

for line in open('input.txt'):
	x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))

	if x1 == x2:
		y1, y2 = min(y1, y2), max(y1, y2)

		for y in range(y1, y2 + 1):
			graph[(x1, y)] += 1
	elif y1 == y2:
		x1, x2 = min(x1, x2), max(x1, x2)

		for x in range(x1, x2 + 1):
			graph[(x, y1)] += 1

print(sum(1 for value in graph.values() if value >= 2))
