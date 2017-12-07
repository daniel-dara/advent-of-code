import re

MAIN_PATTERN = re.compile(r'(\w+) \((\d+)\)')

descendents = set()
nodes = set()

for line in open('input.txt'):
	nodeInfo, *childrenInfo = line.split(' -> ')
	nodeId, weight = re.match(MAIN_PATTERN, nodeInfo).groups()

	nodes.add(nodeId)

	if len(childrenInfo) > 0:
		children = childrenInfo[0].rstrip().split(', ')
		descendents = descendents.union(children)

# Print the only node that didn't appear as a child of any other node.
print(next(iter(nodes.difference(descendents))))