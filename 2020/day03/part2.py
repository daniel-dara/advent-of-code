import math
from collections import namedtuple

Slope = namedtuple('Slope', ['x', 'y'])
world = [line.strip() for line in open('input.txt')]


def count_trees(slope: Slope) -> int:
    x, y = 0, 0
    tree_count = 0

    while y < len(world):
        if world[y][x % len(world[0])] == '#':
            tree_count += 1

        x += slope.x
        y += slope.y

    return tree_count


print(math.prod(count_trees(Slope(x, y)) for x, y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))
