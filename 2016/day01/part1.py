x, y, d = 0, 0, 0

for instruction in open('input.txt').read().split(', '):
	a, b = instruction[0], int(instruction[1:])
	d = (d + (a == 'R') - (a == 'L')) % 4
	x, y = x + b * ((d == 1) - (d == 3)), y + b * ((d == 0) - (d == 2))

print(abs(x) + abs(y))
