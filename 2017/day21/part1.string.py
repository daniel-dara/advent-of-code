# Random challenge: solve using strings instead of 2d arrays and numpy.
import math


def get_chunk_index(index, size, chunk_size):
	chunks_per_side = size // chunk_size
	return index // (size * chunk_size) * chunks_per_side + index // chunk_size % chunks_per_side


def rotate_clockwise(string, k):
	if k == 0:
		return string

	if len(string) == 4:
		string = ''.join(string[i] for i in [2, 0, 3, 1])
	else:
		string = ''.join(string[i] for i in [6, 3, 0, 7, 4, 1, 8, 5, 2])

	return rotate_clockwise(string, k - 1)


def flip(string):
	if len(string) == 4:
		return ''.join(string[i] for i in [2, 0, 3, 1])
	else:
		return ''.join(string[i] for i in [6, 7, 8, 3, 4, 5, 0, 1, 2])


image = '.#...####'
enhancements = {}

for line in open('input.txt'):
	input_, output = (pattern.replace('/', '') for pattern in line.strip().split(' => '))

	for k in range(4):
		enhancements[rotate_clockwise(input_, k)] = output
		enhancements[rotate_clockwise(flip(input_), k)] = output

for _ in range(5):
	size = int(math.sqrt(len(image)))
	chunk_size = 3 if size % 2 else 2
	chunks_per_side = size // chunk_size
	chunks = [''] * chunks_per_side ** 2
	new_image = ''

	for index, char in enumerate(image):
		chunk_index = get_chunk_index(index, size, chunk_size)
		chunks[chunk_index] += char

	new_chunks = [enhancements[chunk] for chunk in chunks]
	size += chunks_per_side
	chunk_size += 1

	for index in range(size ** 2):
		chunk_index = get_chunk_index(index, size, chunk_size)
		chunk_column = (index // size) % chunk_size * chunk_size + index % chunk_size
		new_image += new_chunks[get_chunk_index(index, size, chunk_size)][chunk_column]

	image = new_image

print(image.count('#'))
