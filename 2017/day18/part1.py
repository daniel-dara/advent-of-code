from collections import defaultdict

regs = defaultdict(lambda: 0)
lastSent = None
instructions = []

for line in open('input.txt'):
	op, a, *b = (line.rstrip() + ' ').split(' ')
	instructions.append((op, a, b[0]))

i = 0

while True:
	op, a, b = instructions[i]

	if b == '':
		if op == 'snd':
			lastSent = regs[a]
		elif op == 'rcv' and regs[a] > 0:
			break
	else:
		b = regs[b] if b in regs else int(b)

		if op == 'set':
			regs[a] = b
		elif op == 'add':
			regs[a] += b
		elif op == 'mul':
			regs[a] *= b
		elif op == 'mod':
			regs[a] %= b
		elif op == 'jgz' and regs[a] > 0:
			i = (i + (b - 1)) % len(instructions)

	i = (i + 1) % len(instructions)

print(lastSent)
