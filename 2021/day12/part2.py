from collections import defaultdict

graph = defaultdict(list)

for line in open('input.txt'):
	a, b = line.strip().split('-')
	graph[a].append(b)
	graph[b].append(a)

path = 'start'
queue = [path]
finished = 0
visited = set()

while queue:
	path = queue.pop(0)

	if path in visited:
		continue

	visited.add(path)
	last_node = path.split('-')[-1]


	for next_node in graph[last_node]:
		if next_node == 'start' or path[0] == '*' and next_node.islower() and next_node in path:
			continue
		if next_node == 'end':
			# print(path.strip('*') + '-end')
			finished += 1
			continue

		queue.append(('*' if next_node.islower() and next_node in path else '') + path + '-' + next_node)

print(finished)
