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

# Holds area of the special region.
area = 0

# Iterate over each relevant point.
for x in range(minCoordinates[0], maxCoordinates[0] + 1):
	for y in range(minCoordinates[1], maxCoordinates[1] + 1):
		# If the point is within the total distance limit from all other coordinates, count it.
		if sum(distance(coordinate, (x, y)) for coordinate in coordinates) < 10000:
			area += 1

print(area)
