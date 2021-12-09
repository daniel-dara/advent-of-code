import re
from collections import defaultdict
from typing import Iterable


def get_range(a1: int, a2: int, b1: int, b2: int) -> Iterable:
	if a1 == a2:
		a_range = (abs(b2 - b1) + 1) * [a1]
	else:
		a_step = 1 if a2 > a1 else -1
		a_range = range(a1, a2 + a_step, a_step)

	return a_range


graph = defaultdict(int)

for line in open('input.txt'):
	x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))

	for a, b in zip(get_range(x1, x2, y1, y2), get_range(y1, y2, x1, x2)):
		graph[(a, b)] += 1

print(sum(value >= 2 for value in graph.values()))
