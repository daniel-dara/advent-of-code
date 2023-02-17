import re

Y = 2_000_000
no_beacons = set()

for line in open('input.txt'):
	sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
	distance = abs(bx - sx) + abs(by - sy)

	for x in range(sx - distance + abs(sy - Y), sx + distance + 1 - abs(sy - Y)):
		if abs(sx - x) + abs(sy - Y) <= distance and (x, Y) != (bx, by):
			no_beacons.add((x, Y))

print(len(no_beacons) == 5525847)
