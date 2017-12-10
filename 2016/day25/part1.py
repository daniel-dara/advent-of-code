instructions = open('input.txt').readlines()

def validSignal(initialA):
	registers = {'a': initialA, 'b': 0, 'c': 0, 'd': 0}
	index = 0
	states = set()
	expectedSignal = 0

	while index < len(instructions) and str((registers, index)) not in states:
		states.add(str((registers, index)))

		parts = instructions[index].rstrip('\n').split(' ')
		cmd, arg1, arg2, *rest = parts + [None]
		jump = 1

		if cmd == 'cpy':
			registers[arg2] = registers[arg1] if arg1 in registers else int(arg1)
		elif cmd == 'inc':
			registers[arg1] += 1
		elif cmd == 'dec':
			registers[arg1] -= 1
		elif cmd == 'out':
			if registers[arg1] != expectedSignal:
				return False

			expectedSignal = int(not expectedSignal)
		else:
			val = registers[arg1] if arg1 in registers else int(arg1)

			if val != 0:
				jump = int(arg2)

		index += jump

	return True

i = 1
while not validSignal(i):
	i += 1

print(i)
