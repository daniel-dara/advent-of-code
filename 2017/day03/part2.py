num = int(open('input.txt').read())

spiral = {(0, 0): 1}
pos = (0, 0)

def getValue(x, y):
	return spiral[(x, y)] if (x, y) in spiral else 0

while spiral[pos] < num:
	x, y = pos

	if x == y:
		if x > 0:
			x -= 1 # upper right corner
		elif x <= 0:
			x += 1 # lower left corner
	elif -x == y:
		if y > 0:
			y -= 1 # upper left corner
		elif y < 0:
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

	pos = (x, y)
	spiral[pos] = (
		getValue(x - 1, y) + getValue(x + 1, y) +         # left/right
		getValue(x, y + 1) + getValue(x, y - 1) +         # up/down
		getValue(x - 1, y - 1) + getValue(x - 1, y + 1) + # diag 
		getValue(x + 1, y - 1) + getValue(x + 1, y + 1)   # diag
	)

print(spiral[pos])