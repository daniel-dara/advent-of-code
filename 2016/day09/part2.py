
file = open('input.txt').read()


def get_decompressed_length(i: int, j: int) -> int:
	decompressed_length = 0

	while i < j:
		if file[i] == '(':
			k = file.index(')', i)
			length, repeat = map(int, file[i + 1:k].split('x'))
			i = k + length
			decompressed_length += repeat * get_decompressed_length(k + 1, i + 1)
		else:
			decompressed_length += 1

		i += 1

	return decompressed_length


print(get_decompressed_length(0, len(file)))
