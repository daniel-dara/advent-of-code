from __future__ import annotations
from typing import NamedTuple, Optional, Dict


class Position(NamedTuple):
    row: int
    column: int

    def apply(self, delta: Position) -> Position:
        return Position(self.row + delta.row, self.column + delta.column)


def path_generator(position: Position, delta: Position) -> Optional[str]:
    while position in diagram:
        if diagram[position].isalpha():
            yield diagram[position]

        if diagram[position] == '+':
            for new_delta in DELTAS:
                if position.apply(new_delta) in diagram and diagram[position.apply(new_delta)] != '*':
                    delta = new_delta

        diagram[position] = '*'
        position = position.apply(delta)


DELTAS = (Position(-1, 0), Position(1, 0), Position(0, 1), Position(0, -1))

diagram: Dict[Position, str] = {
    Position(row, column): character
    for row, line in enumerate(open('input.txt'))
    for column, character in enumerate(line.rstrip())
    if character != ' '
}

print(''.join(path_generator(min(diagram.keys()), Position(1, 0))))
