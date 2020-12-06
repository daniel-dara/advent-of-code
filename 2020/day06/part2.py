
print(sum(
	len(set.intersection(*map(set, group.split('\n'))))
	for group in open('input.txt').read().split('\n\n')
))
