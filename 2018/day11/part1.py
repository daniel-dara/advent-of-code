serialNumber = int(open('input.txt').read())

def calculatePointPowerLevel(x, y):
	return ((x + 10) * y + serialNumber) * (x + 10) // 100 % 10 - 5

def calculate3by3PowerLevel(x, y):
	return sum([grid[j - 1][i - 1] for i in range(x, x + 3) for j in range(y, y + 3)])

# 2d array of power levels
grid = [[calculatePointPowerLevel(x, y) for x in range(1, 301)] for y in range(1, 301)]

# 1d array of tuples with x, y, and the total power level of the 3x3 region with that upper left corner.
grid3by3 = [(x, y, calculate3by3PowerLevel(x, y)) for x in range(1, 299) for y in range(1, 299)]

# Grab the max tuple by power level.
x, y, size = max(grid3by3, key=lambda item: item[2])

print(str(x) + ',' + str(y))
