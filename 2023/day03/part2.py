import itertools
from collections import defaultdict
from math import prod


def get_adjacent_gear_coordinates(row, column):
	offsets = [-1, 0, 1]

	return set(
		(row + row_offset, column + column_offset)
		for row_offset, column_offset in list(itertools.product(offsets, offsets))
		if (
			(row_offset != 0 or column_offset != 0)
			and (row + row_offset, column + column_offset) in schematic
			and schematic[row + row_offset, column + column_offset] == '*'
		)
	)


schematic = {
	(row, column): character
	for row, line in enumerate(open('input.txt').readlines())
	for column, character in enumerate(line.strip() + '.')  # end line with period to avoid number wrapping
}

width, height = max(x[1] for x in schematic.keys()) + 1, max(x[0] for x in schematic.keys()) + 1

adjacent_gear_coordinates = set()
num_string = '0'
total = 0

gear_coordinates_to_part_numbers = defaultdict(list)

for row in range(height):
	for column in range(width):
		if schematic[row, column].isdigit():
			num_string += schematic[row, column]
			adjacent_gear_coordinates |= get_adjacent_gear_coordinates(row, column)
		else:
			if adjacent_gear_coordinates:
				for row_, column_ in adjacent_gear_coordinates:
					gear_coordinates_to_part_numbers[row_, column_].append(int(num_string))

			adjacent_gear_coordinates = set()
			num_string = '0'

print(sum(prod(numbers) for numbers in gear_coordinates_to_part_numbers.values() if len(numbers) > 1))
