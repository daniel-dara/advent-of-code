left = []
right = []

for line in open('input.txt'):
	a, b = map(int, line.split())
	left.append(a)
	right.append(b)

left.sort()
right.sort()

print(sum(abs(a - b) for a, b in zip(left, right)))
