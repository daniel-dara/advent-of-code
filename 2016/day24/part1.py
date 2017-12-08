import itertools

maze = {}
start = None
locations = []

x, y = (0, 0)
for line in open('sample.txt'):
	for x in range(len(line.rstrip())):
		maze[x, y] = line[x]
		if line[x] == '0':
			start = (x, y)
		elif line[x] not in '#.':
			locations.append((x, y))

	y += 1

# BFS of shortest path
def getShortestPath():
	return 0

paths = {}

for location in locations:
	paths[start, location] = getShortestPath(start, location)

for pointA, pointB in itertools.combinations(locations, 2):
	length = getShortestPath(pointA, pointB)
	# store the distance in both directions for easier lookups
	paths[pointA, pointB], paths[pointB, pointA] = length, length

print(maze)
print(start, locations)
