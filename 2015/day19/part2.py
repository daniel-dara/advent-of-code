from collections import defaultdict

rules = defaultdict(lambda: [])
revRules = {}
molecule = open('input.txt').readlines()[-1]
possibilities = set()
maxLength = 0

for line in open('input.txt'):
	if line == '\n':
		break

	a, b = line.rstrip().split(' => ')
	rules[b] = [a]
	revRules[b] = a
	maxLength = max(maxLength, len(b))



while molecule not in rules['e']:
	for i in range(len(molecule)):
		for j in range(1, maxLength + 1):

			for replacement in revRules[molecule[i:i + j]]:
				possibilities.add(molecule[:i] + replacement + molecule[i + j:])

print(len(possibilities))
