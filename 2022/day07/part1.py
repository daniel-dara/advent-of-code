
MAX = 100_000
sizes = []
folders = {}
total = 0

for line in open('input.txt'):
	if line.startswith('$ cd'):
		if '..' in line:
			size = sizes.pop()

			if size <= MAX:
				total += size

			if sizes:
				sizes[-1] += size
		else:
			sizes.append(0)
	elif line[0].isdigit():
		sizes[-1] += int(line.split()[0])

while sizes:
	size = sizes.pop()

	if size <= MAX:
		total += size

	if sizes:
		sizes[-1] += size

print(total == 1792222)
