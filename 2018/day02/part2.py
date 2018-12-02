import itertools
import difflib

def getCommonCharacters(a, b):
	return ''.join(x for x, y in zip(a, b) if x == y)

ids = open('input.txt').read().splitlines()

for a, b in itertools.combinations(ids, 2):
	commonCharacters = getCommonCharacters(a, b)

	if len(commonCharacters) == len(ids[0]) - 1:
		print(commonCharacters)
		break
