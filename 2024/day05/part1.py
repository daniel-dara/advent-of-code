import re
import itertools
import collections
import math
from collections import defaultdict

rules_string, updates_string = open('input.txt').read().split('\n\n')
rules = defaultdict(set)

for line in rules_string.split('\n'):
	a, b = map(int, line.split('|'))
	rules[a].add(b)

updates = [list(map(int, line.split(','))) for line in updates_string.split('\n')]

total = 0
for update in updates:
	is_valid = True

	for i in range(len(update)):
		for successor in rules[update[i]]:
			if successor in update[:i]:
				is_valid = False

	if is_valid:
		total += update[len(update) // 2]

print(total)
