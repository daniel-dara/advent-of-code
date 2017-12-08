import re
from collections import defaultdict

registers = defaultdict(lambda: 0)
maxEver = 0

for line in open('input.txt'):
	regA, op1, val1, regB, op2, val2 = re.match(r'(\w+) (inc|dec) (-?\d+) if (\w+) ([^ ]+) (-?\d+)', line).groups()

	if eval(str(registers[regB]) + op2 + val2):
		registers[regA] += int(val1) if op1 == 'inc' else -int(val1)

	maxEver = max(maxEver, max(registers.values()))

print(maxEver)
