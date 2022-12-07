import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

NEED = 30_000_000
sizes = []
folders = {}

final_sizes = []

for line in open(input_file):
	if line.startswith('$ cd'):
		if '..' in line:
			size = sizes.pop()

			final_sizes.append(size)

			if sizes:
				sizes[-1] += size
		else:
			sizes.append(0)
	elif line.startswith('$ ls'):
		pass
	elif line.startswith('dir '):
		pass
	else:
		# file size
		sizes[-1] += int(line.split()[0])

size = 0
while sizes:
	sizes[-1] += size
	size = sizes.pop()
	final_sizes.append(size)

final_sizes.sort()

used = final_sizes[-1]

for size in final_sizes:
	if 30_000_000 <= 70_000_000 - used + size:
		print(size)
		exit()

# 14733871 too high?
