from typing import Dict
from importlib import import_module

# from .part1b import parse_input, get_new_molecules
part1b = import_module('2015.day19.part1b')


def solve() -> int:
    replacements, target_molecule = part1b.parse_input()

    states: Dict[str, int] = {}
    queue = [('e', 0)]

    while queue and target_molecule not in states:
        molecule, steps = queue.pop()

        if molecule in states and steps > states[molecule]:
            continue

        print(steps, len(molecule) - len(target_molecule), len(queue), molecule)

        states[molecule] = steps

        for new_molecule in part1b.get_new_molecules(replacements, molecule):
            if len(new_molecule) <= len(target_molecule):
                queue.append((new_molecule, steps + 1))

    return states[target_molecule]


print('part2', solve())
