from collections import defaultdict, namedtuple

Position = namedtuple('Position', 'row col')


class Tile:
	def __init__(self, id_, borders, image):
		self.id_ = id_
		self.borders = borders
		self.image = image
		self.position = None


def main():
	tiles = set()

	for tile in open('input.txt').read().strip().split('\n\n'):
		id_, *image = tile.split('\n')
		tiles.add(Tile(
			id_,
			[
				image[0],
				image[-1],
				''.join(row[0] for row in image),
				''.join(row[-1] for row in image)
			],
			image
		))

	first_tile = tiles.pop()
	first_tile.position = Position(0, 0)
	queue = [first_tile]

	while queue:
		tile = queue.pop()

		for index, border in enumerate(tile.borders):
			matching_tile = find_match(index, border, tiles)
		exit()


def find_match(index, border, tiles):
	desired_index = (index + 2) % 4

	for tile in tiles:
		for index2, border2 in enumerate(tile.borders):
			if border == border2:
				return tile

main()
