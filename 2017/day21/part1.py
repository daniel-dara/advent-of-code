# TODO: Cleanup this disgusting code
import numpy

rules = {}

for line in open('input.txt'):
	input_, output = (numpy.array([list(row) for row in pattern.split('/')]) for pattern in line.strip().split(' => '))

	for k in range(4):
		rules[tuple(map(tuple, numpy.rot90(input_, k)))] = output
		rules[tuple(map(tuple, numpy.rot90(numpy.flip(input_, 0), k)))] = output

image = numpy.array([list(row) for row in '.#./..#/###'.split('/')])

for _ in range(5):
	size = len(image)
	chunk_size = 3 if len(image) % 2 else 2
	chunk_count = (size // chunk_size) ** 2
	next_image = [[] for row in range(size + size // chunk_size)]

	for i in range(chunk_count):
		row, col = i * chunk_size // size * chunk_size, (i * chunk_size) % size
		chunk = image[row:row + chunk_size, col:col + chunk_size]
		new_chunk = rules[tuple(map(tuple, chunk))]

		new_row = i * chunk_size // size * (chunk_size + 1)
		for j, chunk_row in enumerate(new_chunk):
			next_image[new_row + j] += chunk_row.tolist()

	image = numpy.array(next_image)

print(sum(row.tolist().count('#') for row in image))
print(sum(row.tolist().count('#') for row in image) == 176)
