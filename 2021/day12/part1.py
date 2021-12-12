from collections import defaultdict
from time import time

start = time()
graph = defaultdict(list)

for line in open('input.txt'):
	a, b = line.strip().split('-')
	graph[a].append(b)
	graph[b].append(a)

queue = [['start']]
finished = 0

while queue:
	path = queue.pop(0)
	last_node = path[-1]

	for next_node in graph[last_node]:
		if next_node.islower() and next_node in path:
			continue
		if next_node == 'end':
			finished += 1
			continue

		queue.append(path + [next_node])

print(finished)
