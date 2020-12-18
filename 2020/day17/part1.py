import itertools

active_cubes = set()

for y, line in enumerate(open('input.txt').readlines()):
	for x, char in enumerate(line.strip()):
		if char == '#':
			active_cubes.add((x, y, 0))

for _ in range(6):
	next_state = set()

	min_x, max_x = min(active_cubes, key=lambda p: p[0])[0] - 1, max(active_cubes, key=lambda p:p[0])[0] + 1
	min_y, max_y = min(active_cubes, key=lambda p: p[1])[1] - 1, max(active_cubes, key=lambda p:p[1])[1] + 1
	min_z, max_z = min(active_cubes, key=lambda p: p[2])[2] - 1, max(active_cubes, key=lambda p:p[2])[2] + 1

	for x in range(min_x, max_x + 1):
		for y in range(min_y, max_y + 1):
			for z in range(min_z, max_z + 1):
				active_neighbors = 0

				for dx, dy, dz in itertools.product([-1, 0, 1], repeat=3):
					if dx != 0 or dy != 0 or dz != 0:
						active_neighbors += int((x + dx, y + dy, z + dz) in active_cubes)

				if (
					(x, y, z) in active_cubes and 2 <= active_neighbors <= 3
					or (x, y, z) not in active_cubes and active_neighbors == 3
				):
					next_state.add((x, y, z))

	active_cubes = next_state

print(len(active_cubes))
