tree = {}

for line in open('input.txt'):
	parent, children = line.rstrip().split(' <-> ')
	tree[parent] = children.split(', ')

groupCount = 0

while tree:
	processed = set()
	unProcessed = next(iter(tree.values()))

	while unProcessed:
		node = unProcessed.pop(0)
		processed.add(node)

		if node in tree:
			unProcessed += tree.pop(node)

	groupCount += 1

print(groupCount)