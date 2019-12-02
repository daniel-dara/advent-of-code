positions = list(map(int, open('input.txt').read().split(',')))
positions[1] = 12
positions[2] = 2
i = 0

while True:
	opcode, a, b, out = positions[i:i + 4]

	if opcode == 99:
		break
	elif opcode == 1:
		positions[out] = positions[a] + positions[b]
	else:
		positions[out] = positions[a] * positions[b]

	i += 4

print(positions[0])
