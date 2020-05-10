infected = {
    (row, column)
    for row, line in enumerate(open('input.txt'))
    for column, character in enumerate(line.rstrip())
    if character == '#'
}

directions = (-1, 0), (0, 1), (1, 0), (0, -1)  # Up, Right, Down, Left
position = len(open('input.txt').readlines()) // 2, len(open('input.txt').readline().rstrip()) // 2
orientation = directions[0]  # Up
infected_bursts = 0

for _ in range(10_000):
    if position in infected:
        infected.remove(position)
        orientation = directions[(directions.index(orientation) + 1) % len(directions)]  # Turn right.
    else:
        infected_bursts += 1
        infected.add(position)
        orientation = directions[(directions.index(orientation) - 1) % len(directions)]  # Turn left.

    position = position[0] + orientation[0], position[1] + orientation[1]

print('part 1:', infected_bursts)
