import itertools

total = 0

for line in open('input.txt'):
	words = line.strip().split(' ')

	if len(words) == len(set(words)):
		total += 1

print(total)