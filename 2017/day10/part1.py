nums = [i for i in range(256)]
index = 0
skip = 0

def rotateLeft(l, n):
	return l[n:] + l[:n]

for length in map(int, open('input.txt').read().split(',')):
	nums = nums[0:length][::-1] + nums[length:]
	index += length + skip
	nums = rotateLeft(nums, (length + skip) % len(nums))
	skip += 1

nums = rotateLeft(nums, -index % len(nums)) # rotate right
print(nums[0] * nums[1])
