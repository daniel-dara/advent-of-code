import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

v = 0
l = []

STACK_COUNT = 9
stacks = [[] for _ in range(STACK_COUNT)]

for line in open(input_file):
	if line.strip().startswith('['):
		for i in range(STACK_COUNT):
			if 1 + i * 4 < len(line) and line[1 + i * 4] != ' ':
				stacks[i].append(line[1 + i * 4])
	elif line.startswith('move'):
		a, b, c = map(int, re.findall(r'\d+', line))

		stacks[c - 1] = stacks[b - 1][:a] + stacks[c - 1]

		for _ in range(a):
			stacks[b - 1].pop(0)

print(''.join(stacks[i][0] for i in range(STACK_COUNT) if len(stacks[i]) > 0))
