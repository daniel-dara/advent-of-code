positions = list(map(int, open('input.txt').read().split(',')))

def getOutputFor(positions, a, b):
	positions[1] = a
	positions[2] = b
	i = 0

	while True:
		opcode, a, b, out = positions[i:i + 4]

		if opcode == 99:
			return positions[0]
		elif opcode == 1:
			positions[out] = positions[a] + positions[b]
		else:
			positions[out] = positions[a] * positions[b]

		i += 4

for a in range(100):
	for b in range(100):
		if getOutputFor(list(positions), a, b) == 19690720:
			print(100 * a + b)
			exit()
