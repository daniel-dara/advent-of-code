total = 0

for line in open('input.txt'):
	total += 2

	i = 0
	while i < len(line):
		if line[i] == '\\':
			if line[i + 1] == '\\' or line[i + 1] == '"':
				total += 1
				i += 1
			else:
				total += 3
				i += 3

		i += 1

print(total)
