import re

# I tried 3 different implementations to see how each would perform

# Using regex (requires Python3.6)
# runtime: 1s
def solution1():
	polymer = open('input.txt').read()

	previousLength = 0

	while previousLength != len(polymer):
		previousLength = len(polymer)
		polymer = re.sub(r'(\w)(?!\1)(?i:\1)', '', polymer)

	print(len(polymer))


# Using list manipulation
# runtime: 5.5s
def solution2():
	polymer = open('input.txt').read()

	keepReacting = True

	while keepReacting:
		keepReacting = False

		for i in range(len(polymer) - 1):
			if i < len(polymer) - 1 and polymer[i].upper() == polymer[i + 1].upper() and polymer[i] != polymer[i + 1]:
				polymer = polymer[:i] + polymer[i + 2:]
				keepReacting = True

	print(len(polymer))

# Using a doubly-linked list
# runtime: 6s
class Node:
	def __init__(self, value, next=None, previous=None):
		self.value = value
		self.next = next
		self.previous = previous

def solution3():
	polymer = open('input.txt').read()

	previousNode = None
	root = None

	for char in polymer:
		node = Node(char)
		node.previous = previousNode

		if previousNode:
			previousNode.next = node

		previousNode = node

		if not root:
			root = node

	keepReacting = True

	def listLength(node):
		length = 0

		while node:
			node = node.next
			length += 1

		return length

	lastLength = 0

	while keepReacting:
		keepReacting = False

		node = root

		while node != None and node.next != None:
			if node.value.upper() == node.next.value.upper() and node.value != node.next.value:
				previous = node.previous
				next = node.next.next

				if previous:
					previous.next = next
				else:
					root = next

				if next:
					next.previous = previous

				node = next
				keepReacting = True
			else:
				node = node.next

	print(listLength(root))

solution1()
