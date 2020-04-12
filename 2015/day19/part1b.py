from collections import defaultdict
from typing import Generator, Set, Dict, List, Tuple


def solve() -> Set[str]:
    replacements, molecule = parse_input()
    return get_new_molecules(replacements, molecule)


def parse_input() -> Tuple[Dict[str, List[str]], str]:
    replacements = defaultdict(lambda: [])
    molecule = ''

    for line in open('input/problem.txt'):
        if '=>' in line:
            from_, to = line.strip().split(' => ')
            replacements[from_].append(to)
        elif line != '\n':
            molecule = line.strip()

    return replacements, molecule


def get_new_molecules(replacements: Dict[str, List[str]], molecule: str) -> Set[str]:
    return set(
        replace_at(molecule, index, len(from_), to)
        for from_ in replacements
        for to in replacements[from_]
        for index in find_all(molecule, from_)
    )


def replace_at(haystack: str, index: int, length: int, replacement: str) -> str:
    return haystack[:index] + replacement + haystack[index + length:]


def find_all(haystack: str, needle: str) -> Generator[int, None, None]:
    index = 0

    while needle in haystack[index:]:
        index = haystack.index(needle, index)
        yield index
        index += 1


print('part1', len(solve()))
