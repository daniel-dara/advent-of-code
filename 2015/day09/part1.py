import re
import itertools

distances = {}
places = set()

for line in open('input.txt'):
	start, end, distance = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()

	places.add(start)
	places.add(end)

	distances[(start, end)] = int(distance)
	distances[(end, start)] = int(distance)

min_distance = 1000000

for perm in itertools.permutations(places):
	distance = 0

	for i in range(len(perm) - 1):
		distance += distances[(perm[i], perm[i + 1])]

	min_distance = min(min_distance, distance)

print(min_distance)
