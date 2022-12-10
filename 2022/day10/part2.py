f = open('input.txt')
c = 1
x = 1
t = 0
v = 0
lit = set()

while c <= 6 * 40:
	if x - 1 <= (c - 1) % 40 <= x + 1:
		lit.add(c - 1)

	if v:
		x += v
		v = 0
	else:
		line = next(f, None)

		if 'addx' in line:
			v = int(line.split()[1])

	c += 1

for r in range(6):
	for c in range(40):
		print('#' if r * 40 + c in lit else '.', end='')

	print()
