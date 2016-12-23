ranges = []

for line in open('input.txt'):
	ranges.append(list(map(int, line.split('-'))))

ranges.sort()

lowest = 0

for rng in ranges:
	if lowest >= rng[0]:
		if lowest < rng[1]:
			lowest = rng[1] + 1
	else:
		break

print(lowest)
