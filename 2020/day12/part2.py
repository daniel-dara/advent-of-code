import math

cardinals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
ship = 0, 0
waypoint = 10, 1


def rotate(point, radians):
	x, y = point
	new_x = x * math.cos(radians) + y * math.sin(radians)
	new_y = -x * math.sin(radians) + y * math.cos(radians)
	return round(new_x), round(new_y)


for line in open('input.txt'):
	action, value = line[0], int(line.strip()[1:])

	if action in cardinals:
		waypoint = waypoint[0] + value * cardinals[action][0], waypoint[1] + value * cardinals[action][1]
	elif action == 'F':
		ship = ship[0] + value * waypoint[0], ship[1] + value * waypoint[1]
	else:
		waypoint = rotate(waypoint, (value if action == 'R' else -value) * math.pi / 180)

print(sum(map(abs, ship)) == 71586)
