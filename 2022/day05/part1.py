import re

STACK_COUNT = 9
stacks = [[] for _ in range(STACK_COUNT)]

for line in open('input.txt'):
	if '[' in line:
		for stack, i in zip(stacks, range(1, len(line) - 1, 4)):
			if line[i] != ' ':
				stack.append(line[i])
	elif line.startswith('move'):
		a, b, c = map(int, re.findall(r'\d+', line))
		stacks[c - 1] = stacks[b - 1][:a][::-1] + stacks[c - 1]
		stacks[b - 1] = stacks[b - 1][a:]

print(''.join(map(next, map(iter, stacks))))
