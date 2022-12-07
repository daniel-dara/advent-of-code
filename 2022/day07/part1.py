sizes = []
total = 0

for line in open('input.txt'):
	if '$ cd' in line:
		if '..' in line:
			dir_size = sizes.pop()
			total += dir_size if dir_size <= 100_000 else 0
			sizes[-1] += dir_size
		else:
			sizes.append(0)
	elif line[0].isdigit():
		sizes[-1] += int(line.split()[0])

# The input is constrained such that the last directory is too big to count,
# so popping what's left in sizes by repeating the 'cd ..' behavior is not necessary.

print(total)
