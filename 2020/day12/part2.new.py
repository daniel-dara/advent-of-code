cardinals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
ship = 0, 0
waypoint = 10, 1

for line in open('input.txt'):
	action, value = line[0], int(line.strip()[1:])

	if action in cardinals:
		waypoint = waypoint[0] + value * cardinals[action][0], waypoint[1] + value * cardinals[action][1]
	elif action == 'F':
		ship = ship[0] + value * waypoint[0], ship[1] + value * waypoint[1]
	else:
		x, y = waypoint
		clockwise_degrees = {'L': 360 - value, 'R': value}[action]
		waypoint = {90: (y, -x), 180: (-x, -y), 270: (-y, x)}[clockwise_degrees]

print(sum(map(abs, ship)) == 71586)
