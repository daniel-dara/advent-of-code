ranges = []

for line in open('input.txt'):
	ranges.append(list(map(int, line.split('-'))))

ranges.sort()

total = 0
num = 0
MAX = 4294967295

for rng in ranges:
	if num < rng[0]:
		total += rng[0] - num

	if num <= rng[1]:
		num = rng[1] + 1

total += MAX - num + 1

print(total)
