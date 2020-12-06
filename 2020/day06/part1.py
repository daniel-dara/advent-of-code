
print(sum(
	len(set(group.replace('\n', '')))
	for group in open('input.txt').read().split('\n\n')
))
