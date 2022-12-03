# Same solution but using a single index instead of two.

code = ''
i = 4

for line in open('input.txt'):
	for c in line:
		i += (
			(c == 'R' and i % 3 < 2)
			- (c == 'L' and i % 3 > 0)
			+ 3 * (c == 'D' and i // 3 < 2)
			- 3 * (c == 'U' and i // 3 > 0)
		)

	code += str(i + 1)

print(code)
