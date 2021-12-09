from typing import Set
from math import prod

packages = set(map(int, open('input.txt').read().split('\n')))
sub_sum = sum(packages) / 3
states = set()
best_subset = packages


def find_smaller_subset(remaining: Set[int], chosen: Set[int]):
	global states
	global best_subset

	if (len(chosen), prod(chosen)) in states:
		return

	states.add((len(chosen), prod(chosen)))

	if sum(chosen) == sub_sum:
		if prod(chosen) < prod(best_subset):
			best_subset = chosen
			yield chosen
	elif sum(chosen) < sub_sum:
		if len(chosen) < len(best_subset):
			for number in list(remaining)[::-1]:  # Optimization: Reverse the list to find the smaller subsets first.
				yield from find_smaller_subset(remaining - {number}, chosen | {number})


print(prod(list(find_smaller_subset(packages, set()))[-1]))
