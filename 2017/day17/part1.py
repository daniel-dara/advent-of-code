position = 0
buffer = [0]
step = int(open('input.txt').read())

for value in range(1, 2018):
	position = 1 + (position + step) % value
	buffer.insert(position, value)

print(buffer[buffer.index(2017) + 1])
