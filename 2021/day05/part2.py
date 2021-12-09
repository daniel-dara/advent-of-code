import re
from collections import defaultdict

graph = defaultdict(int)

for line in open('input.txt'):
	x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))

	graph[x1, y1] += 1

	while (x1, y1) != (x2, y2):
		x1 += (x2 > x1) - (x1 > x2)
		y1 += (y2 > y1) - (y1 > y2)
		graph[x1, y1] += 1

print(sum(value > 1 for value in graph.values()))
