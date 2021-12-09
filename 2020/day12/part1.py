cardinals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
location = 0, 0
direction = 0

for line in open('input.txt'):
	action, value = line[0], int(line[1:])

	if action == 'F' or action in cardinals:
		change = directions[direction] if action == 'F' else cardinals[action]
		location = location[0] + value * change[0], location[1] + value * change[1]
	else:
		direction = (direction + (value if action == 'R' else -value) // 90) % len(directions)

print(sum(map(abs, location)))
