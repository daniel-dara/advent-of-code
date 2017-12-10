from collections import Counter

password = list(map(ord, list(open('input.txt').read().rstrip('\n'))))

def isValid(word):
	return hasIncreasingStraight(word) and not hasInvalidLetters(word) and hasTwoPairs(word)

def hasIncreasingStraight(word):
	for i in range(len(word) - 2):
		if word[i] + 1 == word[i + 1] and word[i + 1] + 1 == word[i + 2]:
			return True

	return False

def hasInvalidLetters(word):
	for letter in [105, 111, 108]: # iol
		if letter in word:
			return True

	return False

def hasTwoPairs(word):
	pairs = None

	for i in range(len(word) - 1):
		if word[i] == word[i + 1]:
			if pairs is None:
				pairs = word[i]
			elif pairs != word[i]:
				return True

	return False

validCount = 0

while validCount < 2:
	i = len(password) - 1

	while i == len(password) - 1 or password[i + 1] == ord('a'):
		password[i] = ord('a') + ((password[i] - ord('a') + 1) % 26)
		i -= 1

	validCount += int(isValid(password))

print(''.join(list(map(chr, password))))
