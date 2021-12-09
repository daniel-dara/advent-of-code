from collections import defaultdict

instructions = tuple(line.split() for line in open('input.txt'))
registers = defaultdict(lambda: 0)
index, mul_count = 0, 0

while index < len(instructions):
	command, arg1, arg2 = instructions[index]
	arg1_value, arg2_value = map(lambda x: registers[x] if x.isalpha() else int(x), (arg1, arg2))

	if command == 'set':
		registers[arg1] = arg2_value
	elif command == 'sub':
		registers[arg1] -= arg2_value
	elif command == 'mul':
		mul_count += 1
		registers[arg1] *= arg2_value
	elif command == 'jnz' and arg1_value != 0:
		index += arg2_value - 1

	index += 1

print(mul_count)
