import re

grid = []

for line in list(open('input.txt'))[2:]:
	x, y, size, used, avail, use = map(int, re.findall(r'\d+', line))

	grid.append((x, y, size, used, avail))

pairs = 0

for i in range(len(grid)):
	for j in range(len(grid)):
		if i == j:
			continue

		node_a = grid[i]
		node_b = grid[j]

		if node_b[4] >= node_a[3] and node_a[3] > 0:
			pairs += 1

print(pairs)