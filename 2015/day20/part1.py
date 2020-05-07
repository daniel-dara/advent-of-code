from __future__ import annotations

from typing import NamedTuple, Optional, Dict, Tuple


class Position(NamedTuple):
    row: int
    column: int

    def move(self, delta: Position) -> Tuple[Position, Position]:
        if diagram[self] == '+':
            for new_delta in DELTAS:
                if self.apply(new_delta) in diagram and diagram[self.apply(new_delta)] != '*':
                    delta = new_delta
                    break

        diagram[self] = '*'

        new_position = self.apply(delta)

        return new_position, delta

    def apply(self, delta: Position) -> Position:
        return Position(self.row + delta.row, self.column + delta.column)


diagram: Dict[Position, str] = {
    Position(row, column): character
    for row, line in enumerate(open('input.txt'))
    for column, character in enumerate(line.rstrip())
    if character != ' '
}

DELTAS = (Position(-1, 0), Position(1, 0), Position(0, 1), Position(0, -1))


def path(position: Position, delta: Position) -> Optional[str]:
    while position in diagram:
        if diagram[position].isalpha():
            yield diagram[position]

        position, delta = position.move(delta)


print(''.join(path(min(diagram.keys()), Position(1, 0))))
