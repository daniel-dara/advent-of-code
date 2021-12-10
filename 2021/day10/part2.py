
close_to_open = {')': '(', ']': '[', '}': '{', '>': '<'}
points = {'(': 1, '[': 2, '{': 3, '<': 4}
scores = []

for line in open('input.txt'):
	stack = []

	for char in list(line.strip()):
		if char in close_to_open.values():
			stack.append(char)
		elif not stack or stack.pop() != close_to_open[char]:
			stack = None
			break

	if stack:
		subtotal = 0

		for char in stack[::-1]:
			subtotal = 5 * subtotal + points[char]

		scores.append(subtotal)

print(sorted(scores)[len(scores) // 2])
