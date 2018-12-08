from collections import defaultdict

# Holds ancestor nodes that haven't had metadata yet.
data = list(map(int, open('input.txt').read().split(' ')))

nodeStack = [] # Holds ancestor nodes that haven't had metadata yet.
metadataSum = 0
i = 0
children = defaultdict(list) # Maps parent nodes to their children.
nodeValues = defaultdict(int) # Stores the calculated value of a node.
root = None

while i < len(data):
	# Check if the top node on the stack has any children left to process.
	if nodeStack and nodeStack[-1][0] == len(children[nodeStack[-1]]):
		# If it has no children left, pop it so we can capture its metadata.
		childCount, metadataCount, index = nodeStack.pop(-1)
	else:
		# Otherwise capture a new node (header) from input.
		childCount, metadataCount = data[i:i + 2]
		index = i # index is required to deduplicate nodes with the same header values.

		# Track the first node as the root so we can check its value at the end.
		if not root:
			root = (childCount, metadataCount, i)

		# Add the new node as a child of the top node on the stack.
		if nodeStack:
			children[nodeStack[-1]].append((childCount, metadataCount, i))

		i += 2

		# Once all the children for a node are found, we can process the metadata for this node.
		if childCount > len(children[(childCount, metadataCount, index)]):
			# If the new node has children, skip the metadata calculation until its children are processed.
			nodeStack.append((childCount, metadataCount, index))
			continue

	# Calculate the nodes value.
	if childCount == 0:
		# A node with no children has a value equal to the sum of its metadata.
		nodeValues[(childCount, metadataCount, index)] = sum(data[i:i + metadataCount])
	else:
		# A node with children has a value equal to the sum of the child values at 1-based indices present in the node's metadata.
		for metadata in data[i:i + metadataCount]:
			if metadata > 0 and metadata <= len(children[(childCount, metadataCount, index)]):
				nodeValues[(childCount, metadataCount, index)] += nodeValues[children[(childCount, metadataCount, index)][metadata - 1]]

	i += metadataCount

print(nodeValues[root])
