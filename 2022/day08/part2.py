score = 0
trees = [list(map(int, line.strip())) for line in open('input.txt').readlines()]
columns = list(map(list, zip(*trees)))

for a in range(len(trees)):
	for b in range(len(trees[0])):
		score = max(
			score,
			min(b, next(i + 1 for i, v in enumerate(trees[a][:b][::-1] + [9]) if v >= trees[a][b]))
			* min(len(trees[0]) - b - 1, next(i + 1 for i, v in enumerate(trees[a][b + 1:] + [9]) if v >= trees[a][b]))
			* min(a, next(i + 1 for i, v in enumerate(columns[b][:a][::-1] + [9]) if v >= columns[b][a]))
			* min(len(columns[0]) - a - 1, next(i + 1 for i, v in enumerate(columns[b][a + 1:] + [9]) if v >= columns[b][a]))
		)

print(score)
