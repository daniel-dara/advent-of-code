import itertools

maze = {}
start = None
locations = []

x, y = 0, 0
for line in open('input.txt'):
	for x in range(len(line.rstrip())):
		maze[x, y] = line[x]
		if line[x] == '0':
			start = (x, y)
		elif line[x] not in '#.':
			locations.append((x, y))

	y += 1

# BFS for shortest path
def getShortestPath(start, end):
	states = {}
	steps = 0
	pos = start
	queue = [(pos, steps)]

	while pos != end:
		pos, steps = queue.pop(0)

		if pos in states:
			continue

		states[pos] = steps

		x, y = pos

		for move in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
			if maze[move] != '#':
				queue.append((move, steps + 1))

	return steps

distances = {}

for location in locations:
	distances[start, location] = getShortestPath(start, location)
	distances[location, start] = distances[start, location]

for pointA, pointB in itertools.combinations(locations, 2):
	length = getShortestPath(pointA, pointB)

	# store the distance in both directions for easier lookups
	distances[pointA, pointB], distances[pointB, pointA] = length, length

leastSteps = float('inf')
for path in itertools.permutations(locations, len(locations)):
	path = (start,) + path + (start,)
	steps = 0

	for i in range(len(path) - 1):
		steps += distances[path[i], path[i + 1]]

	leastSteps = min(leastSteps, steps)

print(leastSteps)
