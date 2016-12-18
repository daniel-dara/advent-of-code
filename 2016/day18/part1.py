row = [tile == '^' for tile in '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^']
total = row.count(False)

for _ in range(40 - 1):
	next_row = []

	for i in range(len(row)):
		is_trap = (i > 0 and row[i - 1]) ^ (i < len(row) - 1 and row[i + 1])
		total += not is_trap
		next_row.append(is_trap)

	row = next_row

print(total)