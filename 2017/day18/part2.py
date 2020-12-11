from collections import defaultdict

instructions = [(line.split() + ['0'])[:3] for line in open('input.txt').readlines()]
registers = defaultdict(lambda: 0)
index = 0
last_sound = None

queue = ([], [])
saved_state = 1, 0, defaultdict(lambda: 0, {'p': 1})  # pid, index, registers
pid = 0
send_total = 0

while True:
	cmd, op1, op2 = instructions[index]
	op1_value, op2_value = (int(x) if x.strip('-').isdigit() else registers[x] for x in (op1, op2))

	if cmd == 'snd':
		if pid:
			send_total += 1

		queue[not pid].append(op1_value)
	elif cmd == 'set':
		registers[op1] = op2_value
	elif cmd == 'add':
		registers[op1] += op2_value
	elif cmd == 'mul':
		registers[op1] *= op2_value
	elif cmd == 'mod':
		registers[op1] %= op2_value
	elif cmd == 'rcv':
		if not queue[pid]:
			(pid, index, registers), saved_state = saved_state, (pid, index, registers)

			if not queue[pid]:
				break

			continue

		registers[op1] = queue[pid].pop(0)
	elif cmd == 'jgz' and op1_value > 0:
		index += op2_value - 1

	index += 1

print(send_total == 5969)
