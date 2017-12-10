x, y = (0, 0)
spiral = {(x, y): 1}

def getValue(x, y):
	return spiral[(x, y)] if (x, y) in spiral else 0

while spiral[x, y] < int(open('input.txt').read()):
	if x == y:
		if x > 0:
			x -= 1 # upper right corner
		else:
			x += 1 # lower left corner
	elif -x == y:
		if y > 0:
			y -= 1 # upper left corner
		else:
			x += 1 # bottom right corner
	else:
		if abs(x) < abs(y):
			if y > 0:
				x -= 1 # top side
			else:
				x += 1 # bottom side
		else:
			if x > 0:
				y += 1 # right side
			else:
				y -= 1 # left side

	spiral[x, y] = sum([getValue(x, y) for x, y in (
		(x - 1, y),
		(x + 1, y),
		(x, y + 1),
		(x, y - 1),
		(x - 1, y - 1),
		(x - 1, y + 1),
		(x + 1, y - 1),
		(x + 1, y + 1),
	)])

print(spiral[x, y])