
dots = set()
folds = []

for line in open('input.txt'):
	if ',' in line:
		dots.add(tuple(map(int, line.split(','))))
	elif '=' in line:
		folds.append(('y' in line, int(line.split('=')[1])))

for axis, value in folds:
	folded_dots = set()
	# axis = axis == 'y'

	for dot in dots:
		if dot[axis] < value:
			folded_dots.add(dot)
		else:
			a = dot[not axis], 2 * value - dot[axis]
			folded_dots.add(a if axis else a[::-1])

	dots = folded_dots

output = '\n'.join(
	''.join(
		'#' if (x, y) in dots else '.'
		for x in range(max(x for x, _ in dots) + 1)
	)
	for y in range(max(y for _, y in dots) + 1)
)

print(output == '.##....##..##..#..#.###...##..###..###.\n#..#....#.#..#.#.#..#..#.#..#.#..#.#..#\n#.......#.#....##...###..#..#.#..#.###.\n#.......#.#....#.#..#..#.####.###..#..#\n#..#.#..#.#..#.#.#..#..#.#..#.#....#..#\n.##...##...##..#..#.###..#..#.#....###.')
print(output)
