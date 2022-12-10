c = 1
x = 1
f = open('input.txt')
t = 0
v = 0

while c <= 220:
	if (c - 20) % 40 == 0:
		t += c * x

	if v:
		x += v
		v = 0
	else:
		line = next(f, None)

		if 'addx' in line:
			v = int(line.split()[1])

	c += 1

print(t == 14520)
