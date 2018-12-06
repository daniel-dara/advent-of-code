from collections import defaultdict

# Holds input data.
coordinates = []

# Read input.
for line in open('input.txt'):
	x, y = map(int, line.split(','))
	coordinates.append((x, y))

# Get min/max coordinates for later iteration.
xCoordinates = [coordinate[0] for coordinate in coordinates]
yCoordinates = [coordinate[1] for coordinate in coordinates]
minCoordinates = [min(xCoordinates), min(yCoordinates)]
maxCoordinates = [max(xCoordinates), max(yCoordinates)]

# Calculate Manhattan distance.
def distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Holds total area per coordinate region.
areas = defaultdict(int)

# Holds disqualified regions that are infinite.
infiniteCoordinates = set()

# Iterate over each relevant point.
for x in range(minCoordinates[0], maxCoordinates[0] + 1):
	for y in range(minCoordinates[1], maxCoordinates[1] + 1):
		# Holds distances mapped to coordinates.
		distances = defaultdict(list)

		# Calculate all distances and track which coordinate(s) they map to.
		for coordinate in coordinates:
			distances[distance(coordinate, (x, y))].append(coordinate)

		shortestDistance = min(distances.keys())

		# If the shortest distance belongs to only one coordinate.
		if len(distances[shortestDistance]) == 1:
			# Increment the coordinate's area.
			areas[distances[shortestDistance][0]] += 1

			# Locations on the border that also have one owning coordinate indicate an infinite region.
			if (y == minCoordinates[1] or y == maxCoordinates[1] or
				x == minCoordinates[0] or x == maxCoordinates[0]):
				infiniteCoordinates |= set(distances[shortestDistance])

# Remove disqualified (infinite) regions.
for coordinate in infiniteCoordinates:
	del areas[coordinate]

print(max(areas.values()))
