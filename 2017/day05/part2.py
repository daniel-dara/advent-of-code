instructions = list(map(int, open('input.txt').read().split('\n')))

i = 0
steps = 0

while i >= 0 and i < len(instructions):
	adjustment = (-1 if instructions[i] >= 3 else 1)
	instructions[i] += adjustment
	i += instructions[i] - adjustment
	steps += 1

print(steps)