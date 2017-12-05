import itertools

total = 0

for line in open('input.txt'):
	ints = list(map(int, line.split('\t')))

	for pair in itertools.permutations(ints, 2):
		if pair[0] % pair[1] == 0:
			total += pair[0] // pair[1]
			break

print(total)