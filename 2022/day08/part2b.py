import math

score = 0
rows = [list(map(int, line.strip())) for line in open('input.txt').readlines()]
columns = list(map(list, zip(*rows)))


def get_view_length(slice):
	total = 0

	for tree in slice[1:]:
		total += 1

		if tree >= slice[0]:
			break

	return total


print(
	max(
		math.prod((
			get_view_length(rows[a][:b + 1][::-1]),
			get_view_length(rows[a][b:]),
			get_view_length(columns[b][:a + 1][::-1]),
			get_view_length(columns[b][a:]),
		))
		for b in range(len(columns))
		for a in range(len(rows))
	) == 590824
)
