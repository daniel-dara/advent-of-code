x, y, z = 0, 0, 0
furthest = 0

for step in open('input.txt').read().rstrip().split(','):
	if step == 'n':
		y += 1
		z -= 1
	elif step == 'ne':
		x += 1
		z -= 1
	elif step == 'se':
		y -= 1
		x += 1
	elif step == 's':
		y -= 1
		z += 1
	elif step == 'sw':
		x -= 1
		z += 1
	elif step == 'nw':
		y += 1
		x -= 1

	furthest = max(furthest, max(map(abs, [x, y, z])))

print(furthest)
