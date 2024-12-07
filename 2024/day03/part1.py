import re
import math

total = 0
for params in re.findall(r'mul\((\d+),(\d+)\)', open('input.txt').read()):
	total += math.prod(map(int, params))

print(total)
