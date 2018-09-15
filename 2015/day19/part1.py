from collections import defaultdict

rules = defaultdict(lambda: [])
molecule = open('input.txt').readlines()[-1]
possibilities = set()
maxLength = 0

for line in open('input.txt'):
	if line == '\n':
		break

	a, b = line.rstrip().split(' => ')
	rules[a] += [b]
	maxLength = max(maxLength, len(a))

for i in range(len(molecule)):
	for j in range(1, maxLength + 1):
		for replacement in rules[molecule[i:i + j]]:
			possibilities.add(molecule[:i] + replacement + molecule[i + j:])

print(len(possibilities))
