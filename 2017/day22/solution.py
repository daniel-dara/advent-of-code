position = tuple(map(lambda x: len(x) // 2, [open('input.txt').readlines(), open('input.txt').readline().rstrip()]))

infected = set()

for row, line in enumerate(open('input.txt')):
    for column, character in enumerate(line.rstrip()):
        if character == '#':
            infected.add((row, column))

directions = (-1, 0), (0, 1), (1, 0), (0, -1)
orientation = directions[0]

infected_bursts = 0

for _ in range(10_000):
    if position in infected:
        orientation = directions[(directions.index(orientation) + 1) % len(directions)]
        infected.remove(position)
    else:
        infected_bursts += 1
        infected.add(position)
        orientation = directions[(directions.index(orientation) - 1) % len(directions)]

    position = position[0] + orientation[0], position[1] + orientation[1]

print('part 1:', infected_bursts)
