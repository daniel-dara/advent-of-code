
rules = {a: b for a, b in (line.strip().split(' => ') for line in open('input.txt'))}
image = ['.#./..#/###']

flipped_rules = {}

for input_, output in rules.items():
	# flipped_rules = {}

	if input_.count('/') == 1:
		top, bottom = input_.split('/')
		flipped_rules[bottom[1] + bottom[0] + '/' + top[1] + top[0]] = output
		flipped_rules[bottom[0] + top[0] + '/' + bottom[1] + top[1]] = output
		flipped_rules[top[1] + bottom[1] + '/' + top[0] + bottom[0]] = output

		if bottom[1] + bottom[0] + '/' + top[1] + top[0] in (set(rules) - {input_}):
			exit(1)
		if bottom[0] + top[0] + '/' + bottom[1] + top[1] in (set(rules) - {input_}):
			exit(1)
		if top[1] + bottom[1] + '/' + top[0] + bottom[0] in (set(rules) - {input_}):
			exit(1)
	else:
		og_input = input_

		for _ in range(4):
			input_ = [list(row) for row in input_.split('/')]
			new_pattern = [['.'] * 3 for _ in range(3)]

			for row in range(3):
				for col in range(3):
					new_pattern[col][2 - row] = input_[row][col]

			new_pattern = [''.join(row) for row in new_pattern]
			flipped_rules['/'.join(new_pattern)] = output
			if '/'.join(new_pattern) in (set(rules) - {og_input}):
				exit(1)
			input_ = '/'.join(new_pattern)

			new_pattern[0], new_pattern[2] = new_pattern[2], new_pattern[0]
			flipped_rules['/'.join(new_pattern)] = output
			if '/'.join(new_pattern) in (set(rules) - {og_input}):
				exit(1)

rules = dict(rules.items() | flipped_rules.items())

for x in range(5):
	new_image = []

	print(x, image)
	for pattern in image:
		output = rules[pattern]

		if output.count('/') == 3:
			rows = output.split('/')
			new_image.append(rows[0][:2] + '/' + rows[1][:2])
			new_image.append(rows[0][2:] + '/' + rows[1][2:])
			new_image.append(rows[2][:2] + '/' + rows[3][:2])
			new_image.append(rows[2][2:] + '/' + rows[3][2:])
		else:
			new_image.append(output)

	image = new_image

print(x + 1, image)
print(sum(pattern.count('#') for pattern in image))

# 136 too low
