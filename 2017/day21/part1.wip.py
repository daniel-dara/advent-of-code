import numpy
rules = {a: b for a, b in (line.strip().split(' => ') for line in open('input.txt'))}
image = ['.#./..#/###']

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
	print(i)
	print('\n----\n'.join(pattern.replace('/', '\n') for pattern in image))

	new_image = []

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
		else:
			new_image.append(output)

	image = new_image

print(sum(pattern.count('#') for pattern in image))

# 136 too low
