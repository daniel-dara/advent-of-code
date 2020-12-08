from re import findall
from collections import defaultdict
from typing import List, DefaultDict, Tuple

child_map: DefaultDict[str, Tuple[Tuple[int, str]]] = defaultdict(lambda: tuple())

for line in open('input.txt'):
	parent = line.split(' bags contain ')[0]
	children: List[Tuple[str, str]] = findall(r'(\d+) ([\w ]+) bag', line)
	child_map[parent] = tuple((int(a), b) for a, b in children)


def count_children(bag: str) -> int:
	return sum(child_count * (1 + count_children(child)) for child_count, child in child_map[bag])


print(count_children('shiny gold'))
