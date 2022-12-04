import re

total = 0

for line in open('input.txt'):
	a, b, c, d = map(int, re.findall(r'\d+', line))

	if a <= c and b >= d or c <= a and d >= b:
		total += 1

print(total)
