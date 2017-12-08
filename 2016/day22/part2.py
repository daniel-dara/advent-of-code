import re

class Node:
	def __init__(self, size, used):
		self.size = size
		self.used = used

grid = {}
empty = None

for line in list(open('input.txt'))[2:]:
	x, y, size, used, avail, use = map(int, re.findall(r'\d+', line))

	grid[x, y] = Node(size, used)

	if used == 0:
		empty = (x, y)

# Coordinate with the largest X value is the goal data.
goal = (sorted(grid.keys())[-1][0], 0)
states = {}
queue = [(0, empty, goal)]

# Breadth First Search
while goal != (0, 0):
	numOfSteps, empty, goal = queue.pop(0)

	if (empty, goal) in states:
		continue

	states[empty, goal] = numOfSteps
	x, y = empty

	swapNodes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

	for swapNode in swapNodes:
		if swapNode in grid and grid[empty].size >= grid[swapNode].used:
			queue.append((numOfSteps + 1, swapNode, empty if swapNode == goal else goal))

print(states[empty, goal])
