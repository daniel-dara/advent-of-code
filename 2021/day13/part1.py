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

for dot in dots:
	if instructions[0][0] == 'y':
		if dot[1] > instructions[0][1]:
			folded_dots.add((dot[0], instructions[0][1] - (dot[1] - instructions[0][1])))
		else:
			folded_dots.add(dot)
	else:
		if dot[0] > instructions[0][1]:
			folded_dots.add((instructions[0][1] - (dot[0] - instructions[0][1]), dot[1]))
		else:
			folded_dots.add(dot)

print(len(folded_dots))
