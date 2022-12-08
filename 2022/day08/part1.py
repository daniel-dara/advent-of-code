import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

total = 0
visible = set()
trees = [list(map(int, line.strip())) for line in open(input_file).readlines()]

for a in range(len(trees)):
	maxes = [-1] * 4

	for b in range(len(trees[0])):
		if trees[a][b] > maxes[0]:
			visible.add((a, b))

		if trees[a][len(trees[a]) - b - 1] > maxes[1]:
			visible.add((a, len(trees[a]) - b - 1))

		if trees[b][a] > maxes[2]:
			visible.add((b, a))

		if trees[len(trees) - b - 1][a] > maxes[3]:
			visible.add((len(trees) - b - 1, a))

		maxes[0] = max(maxes[0], trees[a][b])
		maxes[1] = max(maxes[1], trees[a][len(trees[a]) - b - 1])
		maxes[2] = max(maxes[2], trees[b][a])
		maxes[3] = max(maxes[3], trees[len(trees) - b - 1][a])

print(len(visible))
