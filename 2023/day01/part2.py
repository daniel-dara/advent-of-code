import re

word_to_digit = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
}

total = 0

# 54607 too high?
for line in open('input.txt'):
	line2 = ''
	i = 0
	while i < len(line):
		is_word_digit = False

		for word in word_to_digit.keys():
			if line[i:].startswith(word):
				line2 += word_to_digit[word]
				is_word_digit = True
				break

		if not is_word_digit:
			line2 += line[i]

		i += 1

	digits = re.findall(r'\d', line2)
	total += int(digits[0] + digits[-1])

print(total)
