color_to_max = {
	'red': 12,
	'green': 13,
	'blue': 14,
}

total = 0

for game in open('input.txt'):
	is_possible = True

	game_id, subsets = game.strip().split(': ')

	for subset in subsets.split('; '):
		for item in subset.split(', '):
			quantity, color = item.split(' ')

			if color_to_max[color] < int(quantity):
				is_possible = False

	if is_possible:
		total += int(game_id.split(' ')[1])

print(total)
