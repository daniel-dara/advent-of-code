import operator
from numbers import Number
from typing import List, Callable


def get_rating(binary_numbers: List[str], op: Callable[[Number, Number], bool], index: int = 0, criteria: str = '') -> int:
	if len(binary_numbers) == 1:
		return int(binary_numbers[0], 2)

	digit_columns = list(zip(*binary_numbers))
	criteria += '1' if op(digit_columns[index].count('1'), len(binary_numbers) / 2) else '0'
	binary_numbers = list(filter(lambda number: number.startswith(criteria), binary_numbers))
	return get_rating(binary_numbers, op, index + 1, criteria)


def get_o2_rating(binary_numbers: List[str]) -> int:
	return get_rating(binary_numbers, operator.ge)


def get_co2_rating(binary_numbers: List[str]) -> int:
	return get_rating(binary_numbers, operator.lt)


def main():
	binary_numbers = open('input.txt').read().split()
	print(get_o2_rating(binary_numbers) * get_co2_rating(binary_numbers))


main()
