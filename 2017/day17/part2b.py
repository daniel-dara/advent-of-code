position = 0
step = int(open('input.txt').read())
zeroPosition = 0
afterZero = None

for value in range(1, 50_000_000):
	position = 1 + (position + step) % value

	if position == 1:
		afterZero = value

print(afterZero)
