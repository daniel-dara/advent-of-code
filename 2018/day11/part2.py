serialNumber = int(open('input.txt').read())

def calculatePointPowerLevel(x, y):
	return ((x + 10) * y + serialNumber) * (x + 10) // 100 % 10 - 5

def calculate3by3PowerLevel(x, y):
	return sum([grid[j - 1][i - 1] for i in range(x, x + 3) for j in range(y, y + 3)])

# 2d array of power levels
grid = [[calculatePointPowerLevel(x, y) for x in range(1, 301)] for y in range(1, 301)]

# Initialize the size of the 2d prefix array of power levels
prefixGrid = [[0 for x in range(len(grid))] for y in range(len(grid))]

# A safe way to retrieve an element from the prefix grid. Returns 0 if the indices are out of bounds.
def getPrefixGrid(row, col):
	return prefixGrid[row][col] if row >= 0 and col >= 0 else 0

# Populate the prefix matrix by summing elements starting in the upper left and slowly expanding.
for length in range(len(grid)):
	for i in range(length + 1):
		prefixGrid[length][i] = grid[length][i] + getPrefixGrid(length - 1, i) + getPrefixGrid(length, i - 1) - getPrefixGrid(length - 1, i - 1)
		prefixGrid[i][length] = grid[i][length] + getPrefixGrid(i, length - 1) + getPrefixGrid(i - 1, length) - getPrefixGrid(i - 1, length - 1)

# Calculates the sum of a square of the matrix given the upper left and lower right points.
def sumSquare(row, col, row2, col2):
	return getPrefixGrid(row2, col2) - getPrefixGrid(row2, col - 1) - getPrefixGrid(row - 1, col2) + getPrefixGrid(row - 1, col - 1)

maxSquare = (0, 0, 0, 0)

# Loop over every possible upper left point for a square.
for row in range(len(grid)):
	for col in range(len(grid)):
		# Loop over every possible square size starting from row, col and going down right.
		for size in range(min(len(grid) - row - 1, len(grid) - col - 1)):
			currentSum = sumSquare(row, col, row + size, col + size)

			if currentSum > maxSquare[3]:
				maxSquare = (col + 1, row + 1, size + 1, currentSum)

print(str(maxSquare[0]) + ',' + str(maxSquare[1]) + ',' + str(maxSquare[2]))