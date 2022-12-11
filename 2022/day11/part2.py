import re
from math import prod
from typing import List, Callable


class Monkey:
	def __init__(
		self,
		items: List[int],
		operation: Callable[[int], int],
		test: Callable[[int], int],
		test_divisor: int
	):
		self.items = items
		self.operation = operation
		self._test = test
		self.test_divisor = test_divisor
		self.test_count = 0

	def test(self, item):
		self.test_count += 1
		return self._test(item)


monkeys = {}

for i, monkey_str in enumerate(open('input.txt').read().split('\n\n')):
	lines = monkey_str.split('\n')

	monkeys[i] = Monkey(
		list(map(int, re.findall(r'\d+', lines[1]))),
		lambda old, formula=lines[2].split('=')[1]: eval(formula.replace('old', str(old))),
		lambda worry, x=[int(line.split()[-1]) for line in lines[3:6]]: x[2] if worry % x[0] else x[1],
		int(lines[3].split()[-1])
	)

for _ in range(10_000):
	for m in monkeys.values():
		while m.items:
			new_worry = m.operation(m.items.pop(0)) % prod(m.test_divisor for m in monkeys.values())
			new_monkey = m.test(new_worry)
			monkeys[new_monkey].items.append(new_worry)

print(prod(sorted(m.test_count for m in monkeys.values())[-2:]))
