
nums = [0, 3, 6]
nums = [10,16,6,0,1,17]

for _ in range(2020 - len(nums)):
	if nums[-1] not in nums[:-1]:
		nums.append(0)
	else:
		last_seen = len(nums) - 1 - nums[::-1].index(nums[-1])
		second_last_seen = len(nums[:last_seen]) - 1 - nums[:last_seen][::-1].index(nums[-1])
		nums.append(last_seen - second_last_seen)

	print(nums[-1])

print(nums[-1])
print(len(nums))
