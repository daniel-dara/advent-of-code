# A fun little interpreter for some basic instructions. Some parsing plus a basic state machine.

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
instructions = open('input.txt').readlines()
index = 0

while index < len(instructions):
	parts = instructions[index].rstrip('\n').split(' ')
	cmd, arg1, arg2, *rest = parts + [None]
	jump = 1

	if cmd == 'cpy':
		registers[arg2] = registers[arg1] if arg1 in registers else int(arg1)
	elif cmd == 'inc':
		registers[arg1] += 1
	elif cmd == 'dec':
		registers[arg1] -= 1
	else:
		val = registers[arg1] if arg1 in registers else int(arg1)

		if val != 0:
			jump = int(arg2)

	index += jump

print(registers['a'])