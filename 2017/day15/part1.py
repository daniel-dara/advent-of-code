import re

a, b = map(int, re.findall(r'(\d+)', open('input.txt').read()))
pairs = 0

for _ in range(40000000):
	a = (a * 16807) % 2147483647
	b = (b * 48271) % 2147483647

	if a & 0xFFFF == b & 0xFFFF:
		pairs += 1

print(pairs)
