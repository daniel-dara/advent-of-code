from math import prod

total = 0

for game in open('input.txt'):
	color_to_max = {
		'red': 0,
		'green': 0,
		'blue': 0,
	}

	_, subsets = game.strip().split(': ')

	for subset in subsets.split('; '):
		for item in subset.split(', '):
			quantity, color = item.split(' ')
			color_to_max[color] = max(int(quantity), color_to_max[color])

	total += prod(color_to_max.values())

print(total)
