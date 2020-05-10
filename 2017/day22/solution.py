from __future__ import annotations

from copy import copy
from typing import NamedTuple, Set


class Position(NamedTuple):
    row: int
    column: int

    def add(self, direction: Direction) -> Position:
        return Position(self.row + direction.row, self.column + direction.column)


class Direction(Position):
    values = None

    def turn_clockwise(self) -> Direction:
        return self.turn(1)

    def turn_counter_clockwise(self) -> Direction:
        return self.turn(-1)

    def turn(self, index_delta: int) -> Direction:
        return self.values[(self.values.index(self) + index_delta) % len(self.values)]


Direction.UP = Direction(-1, 0)
Direction.RIGHT = Direction(0, 1)
Direction.DOWN = Direction(1, 0)
Direction.LEFT = Direction(0, -1)
Direction.values = (Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT)

initial_infected = {
    Position(row, column)
    for row, line in enumerate(open('input.txt'))
    for column, character in enumerate(line.rstrip())
    if character == '#'
}

initial_position = Position(len(open('input.txt').readlines()) // 2, len(open('input.txt').readline().rstrip()) // 2)
initial_direction: Direction = Direction.UP


def part1(infected: Set[Position], position: Position, direction: Direction) -> int:
    infected_bursts = 0

    for _ in range(10_000):
        if position in infected:
            direction = direction.turn_clockwise()
            infected.remove(position)
        else:
            direction = direction.turn_counter_clockwise()
            infected.add(position)
            infected_bursts += 1

        position = position.add(direction)

    return infected_bursts


def part2(infected: Set[Position], position: Position, direction: Direction) -> int:
    infected_bursts = 0

    weakened = set()
    flagged = set()

    for _ in range(10_000_000):
        if position in infected:
            direction = direction.turn_clockwise()
            infected.remove(position)
            flagged.add(position)
        elif position in flagged:
            direction = direction.turn_clockwise().turn_clockwise()
            flagged.remove(position)
        elif position in weakened:
            weakened.remove(position)
            infected.add(position)
            infected_bursts += 1
        else:
            direction = direction.turn_counter_clockwise()
            weakened.add(position)

        position = position.add(direction)

    return infected_bursts


print('part 1:', part1(copy(initial_infected), initial_position, initial_direction))
print('part 2:', part2(copy(initial_infected), initial_position, initial_direction))
