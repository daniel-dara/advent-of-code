import re
from collections import defaultdict

with open('input.txt') as file:
	state = file.readline()[-3]
	steps = int(file.readline().split()[-2])
	file.readline()  # empty line

	directions = r'.*?(\d).*?(\d).*?(left|right).*?state (\w)' * 2
	blueprint_data = re.findall(r'state (\w)' + directions, ''.join(file.readlines()), re.DOTALL)

	blueprint = {}
	for group in blueprint_data:
		blueprint[group[0], int(group[1])] = int(group[2]), -1 if group[3] == 'left' else 1, group[4]
		blueprint[group[0], int(group[5])] = int(group[6]), -1 if group[7] == 'left' else 1, group[8]

tape = defaultdict(lambda: 0)
index = 0

while steps:
	value, move, state = blueprint[state, tape[index]]
	tape[index] = value
	index += move
	steps -= 1

print(sum(tape.values()))
