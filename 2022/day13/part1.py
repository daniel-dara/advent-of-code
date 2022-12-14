
def is_ordered(A, B):
	for a, b in zip(A, B):
		if type(a) is int and type(b) is int:
			if a != b:
				return b - a
		else:
			x = is_ordered([a] if type(a) is int else a, [b] if type(b) is int else b)

			if x < 0:
				return -1
			elif x > 0:
				return 1

	return len(B) - len(A)


total = 0

for i, pair in enumerate(open('input.txt').read().split('\n\n')):
	a, b = map(eval, pair.split('\n'))
	total += (i + 1) * (is_ordered(a, b) >= 0)

print(total)
