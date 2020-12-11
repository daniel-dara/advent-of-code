import itertools
from copy import deepcopy

seats = [list('.' + line.strip() + '.') for line in open('input.txt')]
seats = [['.'] * len(seats[0])] + seats + [['.'] * len(seats[0])]  # Buffer the seats to prevent out of bounds checks.
old_seats = None

while old_seats != seats:
	old_seats = deepcopy(seats)

	for row in range(len(old_seats)):
		for col in range(len(old_seats[0])):
			if old_seats[row][col] == '.':
				continue

			occupied_count = sum(
				old_seats[row + x][col + y] == '#'
				for x, y in itertools.product((-1, 0, 1), repeat=2)
				if (x, y) != (0, 0)
			)

			if occupied_count == 0:
				seats[row][col] = '#'
			elif occupied_count >= 4:
				seats[row][col] = 'L'

print(sum(row.count('#') for row in seats))
