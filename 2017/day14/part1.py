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

print(sum([hexToBitString(getKnotHash('ljoxqyyw-' + str(row))).count('1') for row in range(128)]))
