
close_to_open = {')': '(', ']': '[', '}': '{', '>': '<'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = 0

for line in open('input.txt'):
	stack = []

	for char in list(line.strip()):
		if char in close_to_open.values():
			stack.append(char)
		elif not stack or stack.pop() != close_to_open[char]:
			total += points[char]
			break

print(total)
