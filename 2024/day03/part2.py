import re
import math

total = 0
instructions = re.sub(r"don't\(\).*?(do\(\)|$)", '', open('input.txt').read().replace('\n', ''))

for params in re.findall(r'mul\((\d+),(\d+)\)', instructions):
	total += math.prod(map(int, params))

print(total)
