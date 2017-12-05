total = 0

for line in open('input.txt'):
	ints = list(map(int, line.split('\t')))
	total += max(ints) - min(ints)

print(total)