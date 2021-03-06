from collections import defaultdict

instructions = [(line.split() + ['0'])[:3] for line in open('input.txt').readlines()]
registers = defaultdict(lambda: 0)
index = 0
last_sound = None

while True:
	cmd, op1, op2 = instructions[index]
	op1_value, op2_value = (int(x) if x.strip('-').isdigit() else registers[x] for x in (op1, op2))

	if cmd == 'snd':
		last_sound = op1_value
	elif cmd == 'set':
		registers[op1] = op2_value
	elif cmd == 'add':
		registers[op1] += op2_value
	elif cmd == 'mul':
		registers[op1] *= op2_value
	elif cmd == 'mod':
		registers[op1] %= op2_value
	elif cmd == 'rcv' and op1_value != 0:
		break
	elif cmd == 'jgz' and op1_value > 0:
		index += op2_value - 1

	index += 1

print(last_sound)
