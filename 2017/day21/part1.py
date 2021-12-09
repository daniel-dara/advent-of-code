import numpy

enhancements = {}

for line in open('input.txt'):
	input_, output = (tuple(map(tuple, pattern.split('/'))) for pattern in line.strip().split(' => '))

	for k in range(4):
		enhancements[tuple(map(tuple, numpy.rot90(input_, k)))] = output
		enhancements[tuple(map(tuple, numpy.rot90(numpy.flip(input_, 0), k)))] = output

image = numpy.array(tuple(map(tuple, '.#./..#/###'.split('/'))))

for _ in range(5):
	size = len(image)
	chunk_size = 3 if len(image) % 2 else 2
	chunk_count = (size // chunk_size) ** 2
	next_image = [[] for row in range(size + size // chunk_size)]

	for row in range(0, size, chunk_size):
		for col in range(0, size, chunk_size):
			chunk = image[row:row + chunk_size, col:col + chunk_size]
			new_chunk = enhancements[tuple(map(tuple, chunk))]

			for row_index, chunk_row in enumerate(new_chunk):
				next_image[row + row // chunk_size + row_index] += chunk_row

	image = numpy.array(next_image)

print(sum(row.tolist().count('#') for row in image))
