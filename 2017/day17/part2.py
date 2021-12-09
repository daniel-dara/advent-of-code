position = 0
buffer = [0]
step = int(open('input.txt').read())

for value in range(1, 50_000_000):
	position = (position + step) % len(buffer) + 1
	buffer.insert(position, value)

print(buffer[buffer.index(0) + 1])