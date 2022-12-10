c = 1
x = 1
f = open('input.txt')
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

p = 0
for _ in range(6):
	for _ in range(40):
		print('#' if p in lit else '.', end='')
		p += 1

	print()
