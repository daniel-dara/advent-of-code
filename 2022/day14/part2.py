import re

# march the perimeter or for each row calculate line segments

X = Y = 4_000_000
no_beacons = set()
sensors = {}
for line in open('input.txt'):
	sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
	sensors[(sx, sy)] = abs(bx - sx) + abs(by - sy)

for x in range(X + 1):
	for y in range(Y + 1):
		is_distress = True

		for s, d in sensors.items():
			if abs(x - s[0]) + abs(y - s[1]) <= d:
				is_distress = False
				break

		if is_distress:
			break

	if is_distress:
		break

print(x, y, x * 4_000_000 + y)
