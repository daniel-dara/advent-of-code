import itertools
from typing import List, Iterable

import numpy as np


# human-ish way of solving
# place a piece, check it against all other pieces and place all matches (adding to a queue)
# repeat for entire queue until all pieces placed (assigned coordinates, then translate to 2d array)

# more optimized way
# dictionary of all possible edges
# place a piece, quickly find all matches, when placing matches, must reorient to match already placed piece
# remove placed pieces from dictionary of edges
# dictionary value could contain either:
# 	1) the fully oriented tile, ready for use. but this would require a dictionary per edge on the anchor tile
#   2) the original tile with metadata for how to reorient
# metadata approach:
#	put all 4 sides in dictionary with integer for orientatin/rotation (0 = top, 1 = right, 2 = bottom, 3 = left)
#   left to right vs right to left order of characters in edges will be important here
#		matching a bottom to a top means reading them both the same, ex: left to right
#		same for sides, ex: top to bottom
#		matching a top to a left though is a bit different: left to right should match top to bottom
#		top to right gets weird: left to right BUT bottom to top since opposite
#   flips indicated by 0 or 1 as they are along that single edge axis


class Tile:
	def __init__(self, id_: int, image: List[str]):
		self.id = id_
		self.image = np.array([list(row) for row in image])
		self.row, self.column = None, None
		self.matches = [None] * 4

	def top(self):
		return self.image[0]

	def bottom(self):
		return self.image[-1]

	def left(self):
		return self.image[:, 0]

	def right(self):
		return self.image[:, -1]

	def is_solved(self):
		return all(self.matches)

	def orient_and_match(self, other):
		# for each side of self
			# for each side of other
				# for each flip of other
					# if sides match
		pass


def get_tiles() -> Iterable[Tile]:
	for tile_string in open('input.txt').read().strip().split('\n\n'):
		id_, *image = tile_string.split('\n')
		yield Tile(int(id_.strip('Tile :')), image)



class Puzzle:
	def fit(self, a: Tile, b: Tile) -> bool:
		pass


def main() -> None:
	puzzle = Puzzle()
	new_tiles = set(get_tiles())

	first_tile = new_tiles.pop()
	first_tile.row, first_tile.column = 0, 0
	placed_tile_queue = [first_tile]

	while new_tiles:
		if not placed_tile_queue:
			raise Exception('The puzzle pieces do not all fit together.')

		placed_tile = placed_tile_queue.pop(0)

		# for each orientation of new_tile (all rotations, flip + rotations)
		# for each side of placed_tile
		# if placed_tile.side matches new_tile.corresponding_side
		# place new_tile (set coordinates)

		for new_tile in new_tiles:
			if placed_tile.right() == new_tile.left():
				new_tiles.remove(new_tile)
				new_tile.row = placed_tile.row
				new_tile.column = placed_tile.column + 1
				placed_tile_queue.append(new_tile)
				break
			elif placed_tile.left() == new_tile.right():
				new_tiles.remove(new_tile)
				new_tile.row = placed_tile.row
				new_tile.column = placed_tile.column + 1
				placed_tile_queue.append(new_tile)
				break
			
			# repeat for top to bottom, bottom to top, and left to right

	

	# for every pairing of tiles
	# skip if either tile has 4 matches already
	# for every edge on tile a
	# compare to every edge on tile b (flip b and repeat)
	# if a match is found, record the match in each tile
	# continue to next tile pair

	# the 4 tiles with only 2 matches are the corners


main()
