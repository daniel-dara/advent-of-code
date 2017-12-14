tree = {}

for line in open('input.txt'):
	parent, children = line.rstrip().split(' <-> ')
	tree[parent] = children.split(', ')

processed = set()
unProcessed = tree['0']

while unProcessed:
	node = unProcessed.pop(0)
	processed.add(node)

	if node in tree:
		unProcessed += tree.pop(node)

print(len(processed))