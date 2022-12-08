score = 0
rows = [list(map(int, line.strip())) for line in open('input.txt').readlines()]
columns = list(map(list, zip(*rows)))

print(
	max(
		min(b, next(i + 1 for i, v in enumerate(rows[a][:b][::-1] + [9]) if v >= rows[a][b]))
		* min(len(rows[0]) - b - 1, next(i + 1 for i, v in enumerate(rows[a][b + 1:] + [9]) if v >= rows[a][b]))
		* min(a, next(i + 1 for i, v in enumerate(columns[b][:a][::-1] + [9]) if v >= columns[b][a]))
		* min(len(columns[0]) - a - 1, next(i + 1 for i, v in enumerate(columns[b][a + 1:] + [9]) if v >= columns[b][a]))
		for b in range(len(columns))
		for a in range(len(rows))
	)
)
