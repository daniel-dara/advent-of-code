groupCount = 0
isGarbage = False
total = 0

stream = iter(open('input.txt').read())
for char in stream:
	if isGarbage:
		if char == '>':
			isGarbage = False
		elif char == '!':
			next(stream)
	else:
		if char == '{':
			groupCount += 1
		elif char == '}':
			total += groupCount
			groupCount -= 1
		elif char == '<':
			isGarbage = True

print(total)
