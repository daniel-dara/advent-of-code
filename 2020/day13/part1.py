import math

with open('input.txt') as file:
	earliest = int(file.readline())
	buses = [int(bus) for bus in file.readline().split(',') if bus != 'x']

print(math.prod(min((bus - earliest % bus, bus) for bus in buses)))
