import re
from collections import defaultdict

stacks = defaultdict(list)

for line in open('input.txt'):
	if '[' in line:
		for i in range(1, len(line) - 1, 4):
			if line[i] != ' ':
				stacks[(i - 1) // 4].append(line[i])
	elif line.startswith('move'):
		a, b, c = map(int, re.findall(r'\d+', line))
		stacks[c - 1] = stacks[b - 1][:a] + stacks[c - 1]
		stacks[b - 1] = stacks[b - 1][a:]

print(''.join(stacks[i][0] for i in range(len(stacks))))
