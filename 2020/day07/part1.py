import re
from collections import defaultdict
from typing import Set, List, DefaultDict

parents: DefaultDict[str, List[str]] = defaultdict(lambda: [])

for line in open('input.txt'):
	parent = line.split(' bags contain ')[0]
	children: List[str] = re.findall(r'\d ([\w ]+) bag', line)

	for child in children:
		parents[child].append(parent)


def find_parents(bag: str) -> Set[str]:
	return set().union(parents[bag], *(find_parents(parent) for parent in parents[bag]))


print(len(find_parents('shiny gold')))
