
positions = list(map(int, open('input.txt').read().split(',')))

fuel_per_position = []

for i in range(min(positions), max(positions)):
	fuel_per_position.append(sum(abs(position - i) for position in positions))

print(min(fuel_per_position))
