from functools import reduce
from binascii import unhexlify

def rotateLeft(l, n):
	return l[n:] + l[:n]

def hexToBitString(hexString):
	return ''.join(['{0:08b}'.format(bytearray(unhexlify(hexString))[i]) for i in range(len(hexString) // 2)])

def getKnotHash(input):
	nums = [i for i in range(256)]
	index = 0
	skip = 0
	lengths = list(map(ord, input)) + [17, 31, 73, 47, 23]

	for _ in range(64):
		for length in lengths:
			nums = nums[0:length][::-1] + nums[length:]
			index += length + skip
			nums = rotateLeft(nums, (length + skip) % len(nums))
			skip += 1

	nums = rotateLeft(nums, -index % len(nums))

	denseHash = []
	for block in [nums[i:i + 16] for i in range(0, len(nums), 16)]:
		denseHash.append(reduce(lambda a, b: a ^ b, block))

	return ''.join(map("{0:02x}".format, denseHash))

grid = set()

for row in range(128):
	for col, val in enumerate(hexToBitString(getKnotHash('ljoxqyyw-' + str(row)))):
		if val == '1':
			grid.add((row, col))

def removeRegion(x, y):
	if (x, y) in grid:
		grid.remove((x, y))
		removeRegion(x - 1, y)
		removeRegion(x + 1, y)
		removeRegion(x, y - 1)
		removeRegion(x, y + 1)

regionCount = 0

while grid:
	removeRegion(*next(iter(grid)))
	regionCount += 1

print(regionCount)
