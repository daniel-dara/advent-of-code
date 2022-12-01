total = 0
i = 0
instructions = open('input.txt').read()

while total >= 0:
	total += 1 if instructions[i] == '(' else -1
	i += 1

print(i)
