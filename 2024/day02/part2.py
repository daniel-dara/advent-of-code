total = 0

for line in open('input.txt'):
	levels = list(map(int, line.split()))
	is_possible = False

	for possibility in [levels, *(levels[:i] + levels[i + 1:] for i in range(len(levels)))]:
		prefix = [a - b for a, b in zip(possibility, possibility[1:])]
		is_possible |= all(0 < num <= 3 for num in prefix) or all(-3 <= num < 0 for num in prefix)

	total += is_possible

print(total)
