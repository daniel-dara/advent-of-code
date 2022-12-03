x, y, d = 0, 0, 0
visited = set()

for instruction in open('input.txt').read().split(', '):
	a, b = instruction[0], int(instruction[1:])
	d = (d + (a == 'R') - (a == 'L')) % 4

	for _ in range(b):
		x, y = x + ((d == 1) - (d == 3)), y + ((d == 0) - (d == 2))

		if (x, y) in visited:
			print(abs(x) + abs(y))
			exit()

		visited.add((x, y))

