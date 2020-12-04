from collections import Counter
import re

class Node:
	def __init__(self, weight, totalWeight, children):
		self.weight = weight
		self.totalWeight = totalWeight
		self.children = children

MAIN_PATTERN = re.compile(r'(\w+) \((\d+)\)')

descendents = set()
nodes = {}

for line in open('input.txt'):
	nodeInfo, *childrenInfo = line.split(' -> ')
	nodeId, weight = re.match(MAIN_PATTERN, nodeInfo).groups()

	children = []

	if len(childrenInfo) > 0:
		children = childrenInfo[0].rstrip().split(', ')
		descendents = descendents.union(children)

	nodes[nodeId] = Node(int(weight), None, children)

root = next(iter(set(nodes.keys()).difference(descendents)))

def checkBalance(nodeId):
	node = nodes[nodeId]
	childWeights = []

	for childId in node.children:
		if nodes[childId].totalWeight is None:
			if checkBalance(childId):
				return True

		childWeights.append(nodes[childId].totalWeight)

	counter = Counter(childWeights)

	if len(counter.most_common()) > 1:
		rightWeight = counter.most_common(1)[0][0]
		wrongWeight = counter.most_common()[-1][0]

		difference = wrongWeight - rightWeight

		print(nodes[node.children[childWeights.index(wrongWeight)]].weight - difference)
		return True

	node.totalWeight = node.weight + sum(childWeights)
	return False

checkBalance(root)
