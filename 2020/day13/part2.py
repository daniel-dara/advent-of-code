
with open('input.txt') as file:
	earliest = int(file.readline())
	buses = [(index, int(bus)) for index, bus in enumerate(file.readline().split(',')) if bus != 'x']

time, step = 0, 1

for offset, bus in buses:
	while time % bus != (bus - offset) % bus:
		time += step

	step *= bus

print(time)
