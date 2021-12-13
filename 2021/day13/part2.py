import re

dots = set(
	(int(x), int(y))
	for x, y in re.findall(r'(\d+),(\d+)', open('input.txt').read())
)

instructions = [
	(axis, int(num))
	for axis, num in re.findall(r'(y|x)=(\d+)', open('input.txt').read())
]

folded_dots = set()

for instruction in instructions:
	for dot in dots:
		if instruction[0] == 'y':
			if dot[1] > instruction[1]:
				folded_dots.add((dot[0], instruction[1] - (dot[1] - instruction[1])))
			else:
				folded_dots.add(dot)
		else:
			if dot[0] > instruction[1]:
				folded_dots.add((instruction[1] - (dot[0] - instruction[1]), dot[1]))
			else:
				folded_dots.add(dot)

	dots = folded_dots
	folded_dots = set()

output = [
	['#' if (x, y) in dots else '.' for x in range(max(x for x, _ in dots) + 1)]
	for y in range(max(y for _, y in dots) + 1)
]

out_string = '\n'.join(''.join(row) for row in output)

print(out_string + '\n')


