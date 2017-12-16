programs = list('abcdefghijklmnop')
iterations = 0
moves = open('input.txt').read().split(',')

def dance(programs):
	for move in moves:
		operation, operands = move[0], move[1:].split('/')

		if operation == 's':
			programs = programs[-int(operands[0]):] + programs[:-int(operands[0])]
		else:
			func = int if operation == 'x' else lambda name: programs.index(name)
			a, b = map(func, operands)
			programs[a], programs[b] = programs[b], programs[a]

	return programs

while iterations == 0 or programs != list('abcdefghijklmnop'):
	programs = dance(programs)
	iterations += 1

for _ in range(1000000000 % iterations):
	programs = dance(programs)

print(''.join(programs))
