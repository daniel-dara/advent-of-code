

stack = []

mapping = {
	'>': '<',
	']': '[',
	'}': '{',
	')': '(',
}

points = {
	'<': 4,
	'(': 1,
	'[': 2,
	'{': 3,
}

scores = []

for line in open('input.txt'):
	char2 = ''

	stack = []
	for char in list(line.strip()):
		if char in '[({<':
			stack.append(char)
		else:
			if len(stack) == 0 or mapping[char] != stack.pop():
				char2 = char
				break

	if char2 == '':
		subtotal = 0

		while stack:
			subtotal *= 5
			subtotal += points[stack.pop()]

		scores.append(subtotal)

print(sorted(scores))
print(sorted(scores)[len(scores)//2])
