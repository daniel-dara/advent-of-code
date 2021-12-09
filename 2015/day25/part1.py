from itertools import count

previous_value = 20151125
row, col = 1, 1
for _ in count():
	row -= 1
	col += 1
	if row < 1:
		row = col
		col = 1

	current_value = (previous_value * 252533) % 33554393

	if row == 2981 and col == 3075:
		print(current_value)
		exit()
	# print(row, col, current_value)
	previous_value = current_value
