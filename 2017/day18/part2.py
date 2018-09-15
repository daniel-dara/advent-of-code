from collections import defaultdict

regs = [defaultdict(lambda: 0), defaultdict(lambda: 0)]
regs[1]['p'] = 1
instructions = []
queues = [[], []]
progId = 0

for line in open('input.txt'):
	op, a, *b = (line.rstrip() + ' ').split(' ')
	instructions.append((op, a, b[0]))

counters = [0, 0]
stuck = 0
prog1SendCount = 0
counter = counters[progId]

while stuck < 2:
	op, a, b = instructions[counter]

	# print(progId, counter)

	if b == '':
		if op == 'snd':
			print('sending data', a, regs[progId][a], 'to prog', progId)
			if progId == 1:
				prog1SendCount += 1

			queues[(progId + 1) % 2].append(regs[progId][a])
		elif op == 'rcv':
			if queues[progId]:
				print('receiving data, reg', a, 'value', queues[progId][0], 'stuck=', stuck)
				if stuck > 0:
					stuck -= 1
				regs[progId][a] = queues[progId].pop(0)
			else:
				print('no data to receive. stuck=', stuck + 1)
				counters[progId] = counter
				stuck += 1
				progId = (progId + 1) % 2
				counter = counters[progId]
				continue

	else:
		b = regs[progId][b] if b in regs[progId] else int(b)

		if op == 'set':
			regs[progId][a] = b
		elif op == 'add':
			regs[progId][a] += b
		elif op == 'mul':
			regs[progId][a] *= b
		elif op == 'mod':
			regs[progId][a] %= b
		elif op == 'jgz' and regs[progId][a] > 0:
			counter = (counter + (b - 1)) % len(instructions)

	counter += 1

print(prog1SendCount)
