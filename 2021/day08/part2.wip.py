import itertools

digit_to_letters = {
	0: set('abcefg'),
	1: set('cf'),
	2: set('acdeg'),
	3: set('acdfg'),
	4: set('bcdf'),
	5: set('abdfg'),
	6: set('abdefg'),
	7: set('acf'),
	8: set('abcdefg'),
	9: set('abcdfg'),
}

# lengths = {
# 	0: 6,
# 	1: 2,
# 	2: 5,
# 	3: 5,
# 	4: 4,
# 	5: 5,
# 	6: 6,
# 	7: 3,
# 	8: 7,
# 	9: 6
# }

digit_to_length = {key: len(value) for key, value in digit_to_letters.items()}
length_to_digits = {value: [k for k, v in digit_to_length.items() if value == v] for value in digit_to_length.values()}

total = 0
for line in open('short_example.txt'):
	in_, out = map(str.split, line.split('|'))

	# code to decoded character
	mappings = {
		'a': set('abcdefg'),
		'b': set('abcdefg'),
		'c': set('abcdefg'),
		'd': set('abcdefg'),
		'e': set('abcdefg'),
		'f': set('abcdefg'),
		'g': set('abcdefg'),
	}

	for i in range(2):
		# value = 'ag'
		for value in in_ + out:
			value = set(value)
			length = len(value)

			if len(length_to_digits[length]) == 1:
				# digit = 1
				digit = length_to_digits[length][0]

				# letters = 'cf'
				letters = digit_to_letters[digit]

				# code = 'ag'
				# decoded = 'cf'
				# mappings = {k: (v & value if k in letters else v - value) for k, v in mappings.items()}
				mappings = {k: v & letters if k in value else v - letters for k, v in mappings.items()}
				# breakpoint()
			else:
				# value = 'cbdgef'
				# digits = [0, 6, 9]
				digits = length_to_digits[length]

				# letters = 'digits of 2 | 3 | 5'
				letters = set(itertools.chain.from_iterable(digit_to_letters[digit] for digit in digits))

				# mappings = {k: (v & value if k in letters else v) for k, v in mappings.items()}
				mappings = {k: v & letters if k in value else v for k, v in mappings.items()}
				# breakpoint()

	breakpoint()
print(total)

# a -> c
# b -> f
# c -> g
# d -> a
# e -> b
# f -> d
# g -> e



# fbcad = 3 -> [db][cf][eg][cf][a]    5 letters with c + f is 3
#
