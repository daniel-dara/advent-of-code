import re

NUM_PATTERN   = re.compile(r'\d+')
ROWS, COLUMNS = 6, 50

pixels = [[0] * COLUMNS for r in range(ROWS)]

def rotateCol(col, rotate_by):
	newCol = [pixels[(i - rotate_by) % ROWS][col] for i in range(ROWS)]

	for i in range(ROWS):
		pixels[i][col] = newCol[i]

def rotateRow(row, rotate_by):
	pixels[row] = [pixels[row][(i - rotate_by) % COLUMNS] for i in range(COLUMNS)]

for line in open('input.txt'):
	a, b = map(int, NUM_PATTERN.findall(line))

	if line.startswith('rect'):
		for c in range(a):
			for r in range(b):
				pixels[r][c] = 1
	elif line.startswith('rotate column'):
		rotateCol(a, b)
	elif line.startswith('rotate row'):
		rotateRow(a, b)

print(sum(map(sum, pixels)))