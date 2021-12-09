program = [(line.strip().replace(',', '') + ' 0').split(' ')[:3] for line in open('input.txt').read().split('\n')]
registers = {'a': 1, 'b': 0}
i = 0

while i < len(program):
	instruction, a, b = program[i]

	if instruction == 'hlf':
		registers[a] /= 2
	elif instruction == 'tpl':
		registers[a] *= 3
	elif instruction == 'inc':
		registers[a] += 1
	elif instruction == 'jmp':
		i += int(a) - 1
	elif instruction == 'jie' and registers[a] % 2 == 0:
		i += int(b) - 1
	elif instruction == 'jio' and registers[a] == 1:
		i += int(b) - 1

	i += 1

print(registers['b'])
