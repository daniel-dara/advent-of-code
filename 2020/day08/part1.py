program = tuple((line.split()[0], int(line.split()[1])) for line in open('input.txt'))
acc, index = 0, 0
states = set()

while index not in states:
	states.add(index)
	command, number = program[index]
	index += number if command == 'jmp' else 1
	acc += number if command == 'acc' else 0

print(acc)
