# This solution is a simple brute force approach. It generates each new row and counts the number of safe tiles as it goes.

# Translate the input from a string to an array of booleans where True is a trap and False is safe.
row = [tile == '^' for tile in '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^']

# Initialize the total to the number of safe spots in the first row
total = row.count(False)

# Because the first row is provided, loop N - 1 times where N is the number of rows specified by the problem (40 for
# part1 and 400000 for part2)
for _ in range(39):
	# Initialize the next row. As a performance optimization, it could be initialized to 100 elements, but it would be a
	# small boost and not very pythonic.
	next_row = []

	# This loops over each tile in the row and calculates the corresponding tile in the next row.
	for i in range(len(row)):
		# The trap rules laid out in the problem statement can actually be reduced down to just this one logic statement.
		# First, note that (i > 0 and row[i - 1]) is checking if the left tile is a trap and (i < len(row) - 1 and row[i + 1])
		# is checking the right. Checkout the following table to see why the center doesn't need to be checked.
		#
		# TRAP CRITERIA TABLE
		# (L C R)
		#  1 1 0
		#  1 0 0
		#  0 1 1
		#  0 0 1
		#
		# Notice that in the first to rows, as long as L = 1 and R = 0, C can be 1 or 0 and the tile is still a trap.
		# Similarly the last two rows show that L = 0 and R = 1 is always a trap. So the center tile doesn't need checking.
		# Further more, if all that's necessary is L = 1 and R = 0 or L = 0 and R = 1, that is the same as checking
		# that L != R which is equivalent to the xor operator.
		is_trap = (i > 0 and row[i - 1]) ^ (i < len(row) - 1 and row[i + 1])

		# Keep a running total of traps. No need to store all the rows if a running total is kept.
		total += not is_trap

		# Add the tile state to the next row being built.
		next_row.append(is_trap)

	# Replace the old row with the new, completed one. Again, due to the running total, there's no need to keep track of
	# anything besides just the last row, which is necessary for creating the next one.
	row = next_row

print(total)