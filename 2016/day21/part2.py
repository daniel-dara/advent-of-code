import re

# word = list('fbgdceah')
word = list('decab')

def rotate(direction, amount):
	for i in range(amount):
		if direction > 0:
			word.insert(0, word.pop(len(word) - 1))
		else:
			word.insert(len(word) - 1, word.pop(0))
lines = []
for line in open('sample.txt'):
	lines.append(line.rstrip('\n'))

for line in lines[::-1]:
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
			rotate(1, a)
		elif 'right' in line:
			rotate(-1, a)
		else:
			index = word.index(x) - 1
			rotate(-1, (len(word) - index  + 1))
			print('new index', word.index(x))
			if word.index(x) > 4:
				printf('hit 4')
				rotate(-1, 1)

	elif line.startswith('reverse positions'):
		new_word = []

		if a > 0:
			new_word += word[:a]

		new_word += word[a:b + 1][::-1]

		if b < len(word) - 1:
			new_word += word[b + 1:]

		word = new_word
	else:
		if b < a:
			a += 1

		letter = word[b]
		word.pop(b)
		word.insert(a, letter)

	print(line)
	print('wtf', ''.join(word))
	print()
