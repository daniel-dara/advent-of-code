
with open('input.txt') as file:
	earliest = int(file.readline())
	buses = [(index, int(bus)) for index, bus in enumerate(file.readline().split(',')) if bus != 'x']

bus_index = 1
bus1_offset, bus1 = buses[bus_index - 1]
bus2_offset, bus2 = buses[bus_index]
step = bus1
time = 0

while True:
	time += step

	while time % bus2 == bus2 - bus2_offset % bus2:
		step *= bus2

		bus_index += 1

		if bus_index >= len(buses):
			print(time)
			print(time == 1106724616194525)
			exit()

		bus2_offset, bus2 = buses[bus_index]
