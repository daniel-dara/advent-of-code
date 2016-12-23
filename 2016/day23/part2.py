regs = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

instructions = []

for line in open('input.txt'):
	cmd, a, b, *trash = line.rstrip('\n').split(' ') + [None, None]
	instructions.append([cmd, a, b])

i = 0
while i < len(instructions):
	incr = 1
	cmd, a, b = instructions[i]

	# optimize series of instructions that effectively use multiplication
	# relies on the fact that 'tgl' never misses with this group of instructions.
	if i == 4:
		regs['a'] = regs['b'] * regs['d']
		regs['c'] = regs['d'] = 0
		i = 10
		continue

	if cmd == 'cpy':
		if not b.lstrip('-').isdigit():
			if a.lstrip('-').isdigit():
				regs[b] = int(a)
			else:
				regs[b] = regs[a]
	elif cmd == 'jnz':
		a2 = int(a) if a.lstrip('-').isdigit() else regs[a]
		b2 = int(b) if b.lstrip('-').isdigit() else regs[b]

		if a2:
			incr = b2
	elif cmd == 'tgl':
		index = i + regs[a]

		if index < len(instructions) and index >= 0:
			cmd2, a2, b2 = instructions[index]

			if cmd2 == 'inc':
				cmd2 = 'dec'
			elif cmd2 == 'dec' or cmd2 == 'tgl':
				cmd2 = 'inc'
			elif cmd2 == 'jnz':
				cmd2 = 'cpy'
			elif cmd2 == 'cpy':
				cmd2 = 'jnz'

			instructions[index] = [cmd2, a2, b2]
	elif cmd == 'dec':
		regs[a] -= 1
	elif cmd == 'inc':
		regs[a] += 1

	i += incr

print(regs)