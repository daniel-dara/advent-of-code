from collections import defaultdict

molecule = open('input.txt').readlines()[-1]
replacements = defaultdict(lambda: [])

for line in open('input.txt'):
	if ' => ' in line:
		from_, to = line.rstrip().split(' => ')
		replacements[from_] += [to]

steps = 0

while molecule != 'e':
	possible_replacements = []

	for from_, to_list in replacements.items():
		for to in to_list:
			if to in molecule:
				possible_replacements.append((from_, to))

	possible_replacements.sort(key=lambda x: len(x[0]) - len(x[1]))

	if not possible_replacements:
		print('Greedy replacement failed to find a path.', molecule)
		break
	else:
		molecule = molecule.replace(possible_replacements[0][1], possible_replacements[0][0], 1)
		steps += 1

print(steps)
