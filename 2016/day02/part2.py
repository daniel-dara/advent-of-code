code = ''
keypad = [
	'  1  ',
	' 234 ',
	'56789',
	' ABC ',
	'  D  ',
]
x, y = 0, 2

for line in open('input.txt'):
	for c in line:
		x2 = x + (c == 'R') - (c == 'L')
		y2 = y + (c == 'D') - (c == 'U')

		if 0 <= x2 < 5 and 0 <= y2 < 5 and keypad[y2][x2] != ' ':
			x, y = x2, y2

	code += keypad[y][x]

print(code)
