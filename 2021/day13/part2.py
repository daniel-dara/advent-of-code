
dots = set()

for line in open('input.txt'):
	if ',' in line:
		dots.add(tuple(map(int, line.split(','))))
	elif '=' in line:
		axis = 'y' in line
		value = int(line.split('=')[1])
		folded_dots = set()

		for dot in dots:
			if dot[axis] < value:
				folded_dots.add(dot)
			else:
				new_dot = dot[not axis], 2 * value - dot[axis]
				folded_dots.add(new_dot if axis else new_dot[::-1])

		dots = folded_dots

print(
	'\n'.join(
		''.join(
			'#' if (x, y) in dots else '.'
			for x in range(max(x for x, _ in dots) + 1)
		)
		for y in range(max(y for _, y in dots) + 1)
	)
)
