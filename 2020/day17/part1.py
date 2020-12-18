import itertools
import operator

active_cubes = set(
	(x, y, 0)
	for y, line in enumerate(open('input.txt').readlines())
	for x, char in enumerate(line.strip())
	if char == '#'
)

for _ in range(6):
	next_state = set()
	mins = [min(active_cubes, key=operator.itemgetter(i))[i] - 1 for i in range(3)]
	maxs = [max(active_cubes, key=operator.itemgetter(i))[i] + 1 for i in range(3)]

	for x in range(mins[0], maxs[0] + 1):
		for y in range(mins[1], maxs[1] + 1):
			for z in range(mins[2], maxs[2] + 1):
				active_neighbors = sum(
					int((x + dx, y + dy, z + dz) in active_cubes)
					for dx, dy, dz in itertools.product([-1, 0, 1], repeat=3)
					if (dx != 0 or dy != 0 or dz != 0)
				)

				if (
					(x, y, z) in active_cubes and 2 <= active_neighbors <= 3
					or (x, y, z) not in active_cubes and active_neighbors == 3
				):
					next_state.add((x, y, z))

	active_cubes = next_state

print(len(active_cubes))
