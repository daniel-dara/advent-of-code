

stack = []

mapping = {
	'>': '<',
	']': '[',
	'}': '{',
	')': '(',
}

points = {
	'>': 25137,
	')': 3,
	']': 57,
	'}': 1197,
}

total = 0

for line in open('input.txt'):
	char2 = ''

	for char in list(line.strip()):
		if char in '[({<':
			stack.append(char)
		else:
			if len(stack) == 0 or mapping[char] != stack.pop():
				char2 = char
				break

	if char2 != '':
		total += points[char2]

print(total)
