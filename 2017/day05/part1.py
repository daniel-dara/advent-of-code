instructions = list(map(int, open('input.txt').read().split('\n')))

i = 0
steps = 0

while i >= 0 and i < len(instructions):
	instructions[i] += 1
	i += instructions[i] - 1
	steps += 1

print(steps)