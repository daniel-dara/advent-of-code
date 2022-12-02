from __future__ import annotations


class Node:
	def __init__(self, value: int, previous: Node = None, next_: Node = None):
		self.value = value
		self.previous = previous
		self.next = next_


head = Node(0)
current = head

# fill list of elves
size = 3014387
for i in range(1, size):
	current.next = Node(i, current)
	current = current.next

# attach ends to form a loop
current.next = head
head.previous = current
current = head

across = current

# iterate to the elf across
for _ in range(size // 2):
	across = across.next

# traverse loop until it's one elf
while current.value != across.value:
	# pop the elf across (take their presents)
	across.previous.next = across.next
	across.next.previous = across.previous

	# iterate the elf across
	across = across.next

	# iterate the current elf
	current = current.next

print(current.value + 1)
