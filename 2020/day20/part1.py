import math

tiles = {}

for tile in open('input.txt').read().strip().split('\n\n'):
	id_, *image = tile.split('\n')
	tiles[int(id_.strip('Tile :'))] = [
		image[0],
		image[-1],
		''.join(row[0] for row in image),
		''.join(row[-1] for row in image)
	]

for id_, borders in tiles.items():
	for id2, borders2 in tiles.items():
		if id_ != id2:
			for border in borders:
				if border in borders2:
					borders2.remove(border)
					borders.remove(border)
				elif border[::-1] in borders2:
					borders2.remove(border[::-1])
					borders.remove(border)

print(math.prod(id_ for id_, borders in tiles.items() if len(borders) == 2))
