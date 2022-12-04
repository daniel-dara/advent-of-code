import re

total = 0

for line in open('input.txt'):
	a, b, c, d = map(int, re.findall(r'\d+', line))

	if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
		total += 1

print(total)
