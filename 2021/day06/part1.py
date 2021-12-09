timers = list(map(int, open('input.txt').read().split(',')))

for _ in range(80):
	i = 0

	while i < len(timers):
		if timers[i] == 0:
			timers[i] = 6
			timers.append(9)
		else:
			timers[i] -= 1

		i += 1

print(len(timers))
