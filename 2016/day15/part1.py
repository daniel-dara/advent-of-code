discs = ((7,  0), (13, 0), (3,  2), (5,  2), (17, 0), (19, 7))

for start_time in range(0, 10000000):
	time = start_time
	level = 0

	while level < len(discs):
		time += 1

		if (discs[level][1] + time) % discs[level][0] != 0:
			break

		level += 1

	if level == len(discs):
		print(start_time)
		break
