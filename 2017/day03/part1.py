import math

num = int(open('input.txt').read())
nearest_root = math.ceil(math.sqrt(num))
nearest_odd_root = nearest_root + (nearest_root + 1) % 2

diff_from_root = nearest_odd_root ** 2 - num

side = nearest_odd_root
arm_index = diff_from_root % (side - 1)

smaller_index = min(arm_index, (side - 1) - arm_index)
dist_from_middle = (side // 2) - smaller_index

print(nearest_odd_root // 2 + dist_from_middle)
