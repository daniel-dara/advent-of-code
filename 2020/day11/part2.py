import itertools
from copy import deepcopy

seats = [list('X' + line.strip() + 'X') for line in open('input.txt')]
seats = [['X'] * len(seats[0])] + seats + [['X'] * len(seats[0])]  # Buffer the seats to prevent out of bounds checks.
old_seats = None

while old_seats != seats:
	old_seats = deepcopy(seats)

	for row in range(len(old_seats)):
		for col in range(len(old_seats[0])):
			if old_seats[row][col] in '.X':
				continue

			total = 0
			for x, y in itertools.product((-1, 0, 1), repeat=2):
				if (x, y) == (0, 0):
					continue

				for scale in itertools.count(1):
					seat = old_seats[row + scale * x][col + scale * y]

					if seat != '.':
						total += (seat == '#')
						break

			if total == 0:
				seats[row][col] = '#'
			elif total >= 5:
				seats[row][col] = 'L'

print(sum(row.count('#') for row in seats))
