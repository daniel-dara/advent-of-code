numbers = list(map(int, open('input.txt').readlines()))
i, j = 0, 2

while sum(numbers[i:j]) != 1492208709:
	if sum(numbers[i:j]) < 1492208709:
		j += 1
	elif sum(numbers[i:j]) > 1492208709:
		i += 1

print(min(numbers[i:j]) + max(numbers[i:j]))
