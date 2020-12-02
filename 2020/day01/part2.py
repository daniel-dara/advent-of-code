import itertools
from math import prod

expenses = [int(line) for line in open('input.txt')]

for subset in itertools.combinations(expenses, 3):
    if sum(subset) == 2020:
        print(prod(subset))
        break
