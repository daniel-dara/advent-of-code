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
		is_repeat = next_node.islower() and next_node in path

		if next_node == 'start' or path[0] == '*' and is_repeat:
			continue
		if next_node == 'end':
			finished += 1
			continue

		queue.append((['*'] if is_repeat else []) + path + [next_node])

print(finished)
