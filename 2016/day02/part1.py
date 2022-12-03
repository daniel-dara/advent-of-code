code = ''
x, y = 1, 1

for line in open('input.txt'):
	for c in line:
		x += (c == 'R' and x < 2) - (c == 'L' and x > 0)
		y += (c == 'D' and y < 2) - (c == 'U' and y > 0)

	code += str(y * 3 + x + 1)

print(code)
