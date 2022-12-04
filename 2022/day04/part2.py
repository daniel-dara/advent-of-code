import re

total = 0

for line in open('input.txt'):
	a, b, c, d = map(int, re.findall(r'\d+', line))

	if a <= d and b >= c:
		total += 1

print(total)
