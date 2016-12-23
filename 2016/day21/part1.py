import re

word = list('abcdefgh')

def rotate(direction, amount):
	index = -direction * amount % len(word)
	return word[index:] + word[:index]

for line in open('input.txt'):
	int1,  int2,  *trash = list(map(int, re.findall(r'\d+', line))) + [None, None]
	char1, char2, *trash = re.findall(r'\b\w\b', line) + [None]

	if line.startswith('swap position'):
		word[int1], word[int2] = word[int2], word[int1]

	elif line.startswith('swap letter'):
		real_word = ''.join(word)
		word = list(real_word.replace(char1, '#').replace(char2, char1).replace('#', char2))

	elif line.startswith('rotate'):
		if 'left' in line:
			word = rotate(-1, int1)
		elif 'right' in line:
			word = rotate(1, int1)
		else:
			index = word.index(char1)
			word = rotate(1, index + 1 + (index >= 4))

	elif line.startswith('reverse positions'):
		word = word[:int1] + word[int1:int2 + 1][::-1] + word[int2 + 1:]
	elif line.startswith('move'):
		word.insert(int2, word.pop(int1))

print(''.join(word))
