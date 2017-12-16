programs = list('abcdefghijklmnop')

for move in open('input.txt').read().split(','):
	operation, operands = move[0], move[1:].split('/')

	if operation == 's':
		programs = programs[-int(operands[0]):] + programs[:-int(operands[0])]
	else:
		func = int if operation == 'x' else lambda name: programs.index(name)
		a, b = map(func, operands)
		programs[a], programs[b] = programs[b], programs[a]

print(''.join(programs))
