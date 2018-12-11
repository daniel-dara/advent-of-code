import re
from collections import defaultdict

# Define a point as having a location and a velocity.
class Point:
	def __init__(self, x, y, vx=0, vy=0):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

	def __repr__(self):
		return str([(self.x, self.y), (self.vx, self.vy)])

	# Moves the point based on the given time and the point's velocity and current location.
	def tick(self, seconds=1):
		self.x += self.vx * seconds
		self.y += self.vy * seconds

# Print the board given the boundaries
def printBoard(minX, minY, maxX, maxY):
	for y in range(minY, maxY + 1):
		for x in range(minX, maxX + 1):
			if any(point.x == x and point.y == y for point in points):
				print('#', end='')
			else:
				print('.', end='')

		print()

points = []

for line in open('input.txt'):
	x, y, vx, vy = map(int, re.findall(r'(-?\d+)', line))
	points.append(Point(x, y, vx, vy))

height = None

# Loop until a reasonable height is reached (human trial and error)
while height == None or height > 10:
	for point in points:
		point.tick()

	upperLeft  = Point(min(points, key=lambda point: point.x).x, min(points, key=lambda point: point.y).y)
	lowerRight = Point(max(points, key=lambda point: point.x).x, max(points, key=lambda point: point.y).y)

	height = lowerRight.y - upperLeft.y + 1

printBoard(upperLeft.x, upperLeft.y, lowerRight.x, lowerRight.y)
