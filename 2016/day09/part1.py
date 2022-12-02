
decompressed_length = 0
i = 0
file = open('input.txt').read()

while i < len(file):
	if file[i] == '(':
		j = file.index(')', i)
		length, repeat = map(int, file[i + 1:j].split('x'))
		i = j + length
		decompressed_length += repeat * length
	else:
		decompressed_length += 1

	i += 1

print(decompressed_length)
