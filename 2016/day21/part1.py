import re

word = list('cadfgbeh')
# word = list('abcde')

def rotate(direction, amount):
	for i in range(amount):
		if direction > 0:
			word.insert(0, word.pop(len(word) - 1))
		else:
			word.insert(len(word) - 1, word.pop(0))

for line in open('input.txt'):
	a, b, *t = list(map(int, re.findall(r'\d+', line))) + [None, None, None]
	x, y, *t = re.findall(r'\b\w\b', line) + [None, None, None]

	if line.startswith('swap position'):
		temp = word[a]
		word[a] = word[b]
		word[b] = temp

	elif line.startswith('swap letter'):
		real_word = ''.join(word)
		word = list(real_word.replace(x, '#').replace(y, x).replace('#', y))

	elif line.startswith('rotate'):
		if 'left' in line:
			rotate(-1, a)
		elif 'right' in line:
			rotate(1, a)
		else:
			index = word.index(x)
			print(index, x)
			rotate(1, index + 1 + (index >= 4))

	elif line.startswith('reverse positions'):
		new_word = []

		if a > 0:
			new_word += word[:a]


		new_word += word[a:b + 1][::-1]

		if b < len(word) - 1:
			new_word += word[b + 1:]

		word = new_word
	else:
		letter = word[a]
		word.pop(a)
		word.insert(b, letter)

	print(line)
	print(''.join(word))


print(''.join(word))