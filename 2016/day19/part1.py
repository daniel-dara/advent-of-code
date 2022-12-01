from __future__ import annotations


class Node:
	def __init__(self, value: int, previous: Node = None, next_: Node = None):
		self.value = value
		self.previous = previous
		self.next = next_


head = Node(0)
current = head

# fill list of elves
for i in range(1, 3014387):
	current.next = Node(i, current)
	current = current.next

# attach ends to form a loop
current.next = head
head.previous = current
current = head

# traverse loop until it's one elf
while current.value != current.next.value:
	# pop the next elf (take their presents)
	current.next = current.next.next
	current.next.previous = current

	# iterate to next elf
	current = current.next

print(current.value + 1)
