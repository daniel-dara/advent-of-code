import itertools

digit_to_letters = {
	0: 'abcefg',
	1: 'cf',
	2: 'acdeg',
	3: 'acdfg',
	4: 'bcdf',
	5: 'abdfg',
	6: 'abdefg',
	7: 'acf',
	8: 'abcdefg',
	9: 'abcdfg',
}

letters_to_digits = {value: key for key, value in digit_to_letters.items()}

digit_to_length = {key: len(value) for key, value in digit_to_letters.items()}
length_to_digits = {value: [k for k, v in digit_to_length.items() if value == v] for value in digit_to_length.values()}
total = 0

for line in open('input.txt'):
	in_, out = map(str.split, line.split('|'))

	for configuration in itertools.permutations('abcdefg'):
		# code to decoded character
		mappings = {key: value for key, value in zip('abcdefg', configuration)}

		is_correct = True

		for pattern in in_:
			decoded = ''.join(sorted(mappings[letter] for letter in pattern))

			if decoded not in letters_to_digits:
				is_correct = False
				break

		subtotal = ''
		if is_correct:
			for pattern in out:
				decoded = ''.join(sorted(mappings[letter] for letter in pattern))
				subtotal += str(letters_to_digits[decoded])

			total += int(subtotal)

			break

print(total)
