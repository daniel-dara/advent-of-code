

stack = []

close_to_open = {
	')': '(',
	']': '[',
	'}': '{',
	'>': '<',
}

points = {
	'<': 4,
	'(': 1,
	'[': 2,
	'{': 3,
}

scores = []

for line in open('input.txt'):
	stack = []

	for char in list(line.strip()):
		if char in close_to_open.values():
			stack.append(char)
		else:
			if not stack or stack.pop() != close_to_open[char]:
				stack = []
				break

	if stack:
		subtotal = 0

		while stack:
			subtotal *= 5
			subtotal += points[stack.pop()]

		scores.append(subtotal)

print(sorted(scores)[len(scores) // 2] == 3646451424)
print(sorted(scores)[len(scores) // 2])
