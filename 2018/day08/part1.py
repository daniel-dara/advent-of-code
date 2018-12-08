# Parse input.
data = list(map(int, open('input.txt').read().split(' ')))

nodeStack = [] # Holds ancestor nodes that haven't had metadata yet.
metadataSum = 0
i = 0

while i < len(data):
	# Check if the top node on the stack has any children left to process.
	if nodeStack and nodeStack[-1][0] == 0:
		# If it has no children left, pop it so we can capture its metadata.
		childCount, metadataCount = nodeStack.pop(-1)
	else:
		# Otherwise capture a new node (header) from input.
		childCount, metadataCount = data[i:i + 2]
		i += 2

		# If the new node has children, skip the metadata calculation until its children are processed.
		if childCount > 0:
			nodeStack.append([childCount, metadataCount])
			continue

	# Once all the children for a node are found, we can process the metadata for this node.
	metadataSum += sum(data[i:i + metadataCount])

	i += metadataCount

	# Decrement the number of children left to process on the parent node.
	if nodeStack:
		nodeStack[-1][0] -= 1
	
print(metadataSum)
