# TODO: Cleanup this disgusting solution

import numpy
rules = {a: b for a, b in (line.strip().split(' => ') for line in open('input.txt'))}
image = '.#./..#/###'
# image = '#..#/..../..../#..#'
# image = '##.##./#..#../....../##.##./#..#../......'

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
image_matrix = numpy.array([list(row) for row in image.split('/')])

# Properly split matrix: https://stackoverflow.com/a/11105569/1313439
# transform, then put back together
for i in range(5):

	if len(image_matrix) % 2:
		chunk_size = 3
	else:
		chunk_size = 2

	size = len(image_matrix)
	chunk_count = (size // chunk_size) ** 2
	matrices = []

	for i in range(chunk_count):
		loc = i // (size // chunk_size) * chunk_size, (i * chunk_size) % size
		matrices.append(image_matrix[loc[0]:loc[0] + chunk_size, loc[1]:loc[1] + chunk_size])

	# [print(matrix) for matrix in matrices]

	for i in range(len(matrices)):
		string = '/'.join(''.join(row) for row in matrices[i])
		new_string = rules[string]
		new_matrix = [list(row) for row in new_string.split('/')]
		matrices[i] = new_matrix

	# [print(matrix) for matrix in matrices]
	# image = '/'.join(''.join(row) for row in matrices[0])
	# print(image)

	new_image = [[] for row in range(size + size // chunk_size)]
	main_row = 0
	for i in range(chunk_count):
		main_row = i // (size // chunk_size) * (chunk_size + 1)
		for j, row in enumerate(matrices[i]):
			new_image[main_row + j] += row

	image_matrix = numpy.array(new_image)

print(sum(row.tolist().count('#') for row in image_matrix))
print(sum(row.tolist().count('#') for row in image_matrix) == 176)
