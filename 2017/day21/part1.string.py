# TODO: Finish solving using string matrices.

import math
import numpy

rules = {a: b.replace('/', '') for a, b in (line.strip().split(' => ') for line in open('input.txt'))}
image = '.#...####'
# image = '#..#........#..#'
# image = '##.##.#..#........##.##.#..#........'

flipped_rules = {}

for input_, output in rules.items():
	for k in range(4):
		array = [list(row) for row in input_.split('/')]
		array = numpy.rot90(array, k)
		str_array = ''.join(''.join(row) for row in array)
		# print(str_array.replace('/', '\n'), '\n')
		flipped_str = ''.join(''.join(row[::-1]) for row in array)
		# print(flipped_str.replace('/', '\n'), '\n')

		flipped_rules[str_array] = output
		flipped_rules[flipped_str] = output

rules = flipped_rules

for _ in range(5):
	size = int(math.sqrt(len(image)))
	chunk_size = 3 if size % 2 else 2
	chunks = [''] * (size // chunk_size) ** 2
	chunks_per_side = size // chunk_size

	for index, char in enumerate(image):
		chunk_index = index // (size * chunk_size) * chunks_per_side + index // chunk_size % chunks_per_side
		chunks[chunk_index] += char

	print(chunks)

	for i in range(len(chunks)):
		chunks[i] = rules[chunks[i]]

	new_image = ''
	new_size = size + chunks_per_side
	new_chunk_size = chunk_size + 1
	for index in range(new_size ** 2):
		chunk_index = index // (new_size * new_chunk_size) * chunks_per_side + index // new_chunk_size % chunks_per_side
		new_image += chunks[chunk_index][(index % (new_chunk_size ** 2 * chunks_per_side)) // new_size * new_chunk_size + 0 + index % new_chunk_size]
		# new_image += chunks[chunk_index][(index // new_size * new_chunk_size + index % new_chunk_size) % (new_chunk_size ** 2 * chunks_per_side)]

	image = new_image

print(image.count('#'))
