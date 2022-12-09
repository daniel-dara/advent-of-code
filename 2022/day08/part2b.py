import math

score = 0
rows = [list(map(int, line.strip())) for line in open('input.txt').readlines()]
columns = list(map(list, zip(*rows)))


def get_view_length(slice, height):
	total = 0

	for tree in slice:
		total += 1

		if tree >= height:
			break

	return total


print(
	max(
		math.prod((
			get_view_length(rows[a][:b][::-1], rows[a][b]),
			get_view_length(rows[a][b + 1:], rows[a][b]),
			get_view_length(columns[b][:a][::-1], columns[b][a]),
			get_view_length(columns[b][a + 1:], columns[b][a]),
		))
		for b in range(len(columns))
		for a in range(len(rows))
	)
)
