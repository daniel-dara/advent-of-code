fav_num = 1358
size = 52 # max moves + 2 for starting location (doesn't count as move)

def isWall(x, y):
	return bin(x*x + 3*x + 2*x*y + y + y*y + fav_num).count('1') % 2

grid = [['#' if isWall(x, y) else '.' for x in range(size)] for y in range(size)]
queue = [(1, 1, 0)]
states = 0

while len(queue) > 0:
	x, y, moves = queue.pop(0)

	if moves > 50 or x < 0 or y < 0 or grid[x][y] != '.':
		continue

	if x >= size or y >= size:
		print('ERROR: Size not big enough.')
		exit(1)

	grid[x][y] = 'O'
	states += 1

	for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
		queue.append((x + dx, y + dy, moves + 1))

print('unique states reached:', states)