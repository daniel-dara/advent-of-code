from __future__ import annotations


class Node:
	def __init__(self, value: int, previous: Node = None, next_: Node = None):
		self.value = value
		self.previous = previous
		self.next = next_


head = Node(0)
current = head

# todo too slow, implement left/right lists of elves
# fill list of elves
size = 3014387
for i in range(1, size):
	current.next = Node(i, current)
	current = current.next

# attach ends to form a loop
current.next = head
head.previous = current
current = head

# traverse loop until it's one elf
while current.value != current.next.value:
	original = current

	# iterate to the elf across from us
	for _ in range(size // 2):
		current = current.next

	# pop the elf across (take their presents)
	current.previous.next = current.next
	current.next.previous = current.previous
	size -= 1

	# iterate to next elf
	current = original.next

print(current.value + 1)
