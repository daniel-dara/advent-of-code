from collections import defaultdict

graph = defaultdict(list)

for line in open('input.txt'):
	a, b = line.strip().split('-')
	graph[a].append(b)
	graph[b].append(a)

queue = [['start']]
finished = 0

while queue:
	path = queue.pop(0)

	for next_node in graph[path[-1]]:
		if next_node == 'end':
			finished += 1
		elif not next_node.islower() or next_node not in path:
			queue.append(path + [next_node])

print(finished)
