total = 0

for line in open('input.txt'):
	levels = list(map(int, line.split()))
	prefix = [a - b for a, b in zip(levels, levels[1:])]
	total += all(0 < num <= 3 for num in prefix) or all(-3 <= num < 0 for num in prefix)

print(total)
