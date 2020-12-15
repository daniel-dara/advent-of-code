from collections import defaultdict

# nums = [0, 3, 6]
nums = [10, 16, 6, 0, 1, 17]

# history = defaultdict(list, {0: [1], 3: [2], 6: [3]})
history = defaultdict(list, {10: [1], 16: [2], 6: [3], 0: [4], 1: [5], 17: [6]})

for i in range(30_000_000 - len(nums)):
	last_number = nums[-1]

	if len(history[last_number]) <= 1:
		nums.append(0)
		history[0].append(len(nums))
	else:
		last_seen = history[last_number][-1]
		second_last_seen = history[last_number][-2]
		new_num = last_seen - second_last_seen
		nums.append(new_num)
		history[new_num].append(len(nums))

	if i % 1_000_000 == 0:
		print(i)

print(nums[-1])
print(len(nums))
