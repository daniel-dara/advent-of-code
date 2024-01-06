import itertools


def is_character_adjacent_to_symbol(row, column):
	offsets = [-1, 0, 1]

	for row_offset, column_offset in list(itertools.product(offsets, offsets)):
		if (
			(row_offset != 0 or column_offset != 0)
			and (row + row_offset, column + column_offset) in schematic
			and schematic[row + row_offset, column + column_offset] not in '1234567890.'
		):
			return True

	return False


schematic = {
	(row, column): character
	for row, line in enumerate(open('input.txt').readlines())
	for column, character in enumerate(line.strip() + '.')  # end line with period to avoid number wrapping
}

width, height = max(x[1] for x in schematic.keys()) + 1, max(x[0] for x in schematic.keys()) + 1

is_adjacent_to_symbol = False
num_string = '0'
total = 0

for row in range(height):
	for column in range(width):
		if schematic[row, column].isdigit():
			num_string += schematic[row, column]
			is_adjacent_to_symbol |= is_character_adjacent_to_symbol(row, column)
		else:
			if is_adjacent_to_symbol:
				total += int(num_string)

			is_adjacent_to_symbol = False
			num_string = '0'

print(total)
