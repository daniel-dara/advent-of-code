import re

total = 0

for line in open('input.txt'):
	digits = re.findall(r'\d', line)
	total += int(digits[0] + digits[-1])

print(total)
