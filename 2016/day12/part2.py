# Same as part1 but with a non-zero initial value for register 'c'.

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
instructions = open('input.txt').readlines()
index = 0

def isInt(string):
	return string.lstrip('-').isdigit()

while index < len(instructions):
	parts = instructions[index].rstrip('\n').split(' ')
	cmd, arg1, arg2, *rest = parts + [None]
	jump = 1

	if cmd == 'cpy':
		registers[arg2] = int(arg1) if isInt(arg1) else registers[arg1]
	elif cmd == 'inc':
		registers[arg1] += 1
	elif cmd == 'dec':
		registers[arg1] -= 1
	else:
		if isInt(arg1):
			if int(arg1) != 0:
				jump = int(arg2)
		elif registers[arg1] != 0:
			jump = int(arg2)

	index += jump

print(registers['a'])