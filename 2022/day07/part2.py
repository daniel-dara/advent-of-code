sizes = []
final_sizes = []

for line in open('input.txt'):
	if '$ cd' in line:
		if '..' in line:
			dir_size = sizes.pop()
			final_sizes.append(dir_size)
			sizes[-1] += dir_size
		else:
			sizes.append(0)
	elif line[0].isdigit():
		sizes[-1] += int(line.split()[0])

while sizes:
	final_sizes.append(sizes.pop())

	if sizes:
		sizes[-1] += final_sizes[-1]

final_sizes.sort()

print(next(size for size in final_sizes if 70_000_000 - final_sizes[-1] + size >= 30_000_000))
