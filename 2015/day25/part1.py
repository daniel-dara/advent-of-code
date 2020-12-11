
code = 20151125
row, col = 1, 1

while not (row == 2981 and col == 3075):
	row, col = (row - 1, col + 1) if row > 1 else (col + 1, 1)
	code = (code * 252533) % 33554393

print(code)
