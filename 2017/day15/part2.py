import re

a, b = map(int, re.findall(r'(\d+)', open('input.txt').read()))
pairs = 0

for _ in range(5000000):
	while True:
		a = (a * 16807) % 2147483647
		if a % 4 == 0:
			break

	while True:
		b = (b * 48271) % 2147483647
		if b % 8 == 0:
			break

	if a & 0xFFFF == b & 0xFFFF:
		pairs += 1

print(pairs)
