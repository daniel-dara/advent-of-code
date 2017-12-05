import itertools

total = 0

for line in open('input.txt'):
	words = line.strip().split(' ')
	sortedWords = list(map(''.join, map(sorted, words)))

	if len(sortedWords) == len(set(sortedWords)):
		total += 1

print(total)