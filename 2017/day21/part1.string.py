# TODO: Finish solving using string matrices.

import math
import numpy

rules = {a: b for a, b in (line.strip().split(' => ') for line in open('input.txt'))}
image = '.#...####'

flipped_rules = {}

for input_, output in rules.items():
	for k in range(4):
		array = [list(row) for row in input_.split('/')]
		array = numpy.rot90(array, k)
		str_array = '/'.join(''.join(row) for row in array)
		# print(str_array.replace('/', '\n'), '\n')
		flipped_str = '/'.join(''.join(row[::-1]) for row in array)
		# print(flipped_str.replace('/', '\n'), '\n')

		flipped_rules[str_array] = output
		flipped_rules[flipped_str] = output

rules = flipped_rules

# Properly split matrix: https://stackoverflow.com/a/11105569/1313439
# transform, then put back together
for i in range(5):
	image = '#..#........#..#'
	size = int(math.sqrt(len(image)))

	square_size = 3 if size % 2 else 2
	squares = [''] * (size // square_size) ** 2

	for index, char in enumerate(image):
		row, col = index // size, index % size

		row_limit == index // (size * square_size) +
		# loc = i // (size // chunk_size), (i * chunk_size) % size
		# square_index = (index // square_size) % len(squares)

		squares[square_index] += char

	print(squares)
	continue
	# print(x)
	# print('\n\n'.join(pattern.replace('/', '\n') for pattern in image))

	for pattern in image:
		output = rules[pattern]



		if output.count('/') == 3:
			# convert 4x4 to 2x2
			rows = output.split('/')
			new_image.append(rows[0][:2] + '/' + rows[1][:2])
			new_image.append(rows[0][2:] + '/' + rows[1][2:])
			new_image.append(rows[2][:2] + '/' + rows[3][:2])
			new_image.append(rows[2][2:] + '/' + rows[3][2:])


			new_matrix = [
				rows[0][:2] + '/' + rows[1][:2],
				rows[0][2:] + '/' + rows[1][2:],
				rows[2][:2] + '/' + rows[3][:2],
				rows[2][2:] + '/' + rows[3][2:],
			]
		else:
			new_image.append(output)

	image = new_image

print(sum(pattern.count('#') for pattern in image))

# 136 too low
