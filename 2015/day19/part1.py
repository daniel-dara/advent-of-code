from collections import defaultdict

replacements = defaultdict(lambda: [])

for line in open('input/problem.txt'):
	if ' => ' in line:
		from_, to = line.rstrip().split(' => ')
		replacements[from_] += [to]

molecule = open('input/problem.txt').readlines()[-1]
new_molecules = set()
max_length = max(map(len, replacements))

for i in range(len(molecule)):
	for j in range(1, max_length + 1):
		for replacement in replacements[molecule[i:i + j]]:
			new_molecules.add(molecule[:i] + replacement + molecule[i + j:])

print(len(new_molecules))
