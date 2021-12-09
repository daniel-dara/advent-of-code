cardinals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
quadrants = ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1))
ship = 0, 0
waypoint = 10, 1

for line in open('input.txt'):
	action, value = line[0], int(line.strip()[1:])

	if action in cardinals:
		waypoint = waypoint[0] + value * cardinals[action][0], waypoint[1] + value * cardinals[action][1]
	elif action == 'F':
		ship = ship[0] + value * waypoint[0], ship[1] + value * waypoint[1]
	else:
		is_odd = (value // 90) % 2
		quadrant = -1 if waypoint[0] < 0 else 1 if waypoint[0] > 0 else 0, -1 if waypoint[1] < 0 else 1 if waypoint[1] > 0 else 0
		index = (quadrants.index(quadrant) + 2 * (value if action == 'R' else -value) // 90)
		index %= len(quadrants) * (1 if index > 0 else -1)
		waypoint = abs(waypoint[is_odd]) * quadrants[index][0], abs(waypoint[not is_odd]) * quadrants[index][1]

print(sum(map(abs, ship)) == 71586)
