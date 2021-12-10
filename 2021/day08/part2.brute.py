import itertools
from collections import defaultdict
from typing import Dict


def decode(pattern: str, mappings_: Dict[str, str]) -> str:
	return ''.join(sorted(mappings_[letter] for letter in pattern))


letters_to_digit = defaultdict(str, {
	'abcefg': '0',
	'cf': '1',
	'acdeg': '2',
	'acdfg': '3',
	'bcdf': '4',
	'abdfg': '5',
	'abdefg': '6',
	'acf': '7',
	'abcdefg': '8',
	'abcdfg': '9',
})

total = 0

for line in open('input.txt'):
	in_, out = map(str.split, line.split('|'))

	for configuration in itertools.permutations('abcdefg'):
		mappings = {key: value for key, value in zip('abcdefg', configuration)}

		if all(
			letters_to_digit[decode(pattern, mappings)]
			for pattern in in_
		):
			total += int(
				''.join(
					letters_to_digit[decode(pattern, mappings)]
					for pattern in out
				)
			)
			break

print(total)
