import re
import copy

size = (35, 25)
# size = (3, 3)
sizes = [[0 for _ in range(size[0])] for _ in range(size[1])]
usages = [[0 for _ in range(size[0])] for _ in range(size[1])]
free_spot = None
source_loc = (24, 0)
# source_loc = (2, 0)
source_usage = 69
# source_usage = 6

for line in list(open('input.txt'))[2:]:
	x, y, size, used, avail, use = map(int, re.findall(r'\d+', line))

	sizes[y][x] = size
	usages[y][x] = str(used) + ('*' if y == source_loc[1] and x == source_loc[0] else '')

	if used == 0:
		free_spot = (y, x)

def getHash(usages):
	return ':'.join(['-'.join(row) for row in usages])

def printUsages(usage):
	for row in usages:
		for col in row:
			print(col + ', ', end='')
		print()
	print()

states = {}
# Hash, Moves, Last-State
queue = [(usages, free_spot, 0, None)]

while queue:
	# print(queue[0][1:3])
	usages, free_spot, moves, last_move = queue.pop(0)

	if len(queue) % 1000 == 0 and len(queue) > 0:
		print(len(queue))

	usage_hash = getHash(usages)

	if usage_hash in states:
		continue

	states[usage_hash] = (moves, last_move)

	if usages[0][0] == str(source_usage) + '*':
		print('Found solution in steps:', moves)
		exit()

	row, col = free_spot
	# printUsages(usages)
	# print(free_spot)
	for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
		if (row + dy >= 0 and row + dy < len(usages) and
				col + dx >= 0 and col + dx < len(usages[0]) and
				int(usages[row + dy][col + dx].rstrip('*')) <= sizes[row][col]):
			new_usages = copy.deepcopy(usages)
			new_usages[row][col] = new_usages[row + dy][col + dx]
			new_usages[row + dy][col + dx] = '0'
			queue.append((new_usages, (row + dy, col + dx), moves + 1, usage_hash))

print('no solution found')