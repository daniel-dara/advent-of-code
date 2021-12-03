import itertools
from collections import defaultdict
from enum import Enum, auto
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


class Border(Enum):
	TOP = auto()
	RIGHT = auto()
	BOTTOM = auto()
	LEFT = auto()


class Puzzle:
	def fit(self, a: Tile, b: Tile) -> bool:
		pass


def main() -> None:
	puzzle = Puzzle()
	new_tiles = set(get_tiles())

	borders_to_tiles = defaultdict(int)

#
	# edge = string, border, is_reversed but matches as long as string is same
	edges_to_tiles = []
	for tile in new_tiles:
		for edge, orientation in tile.edges():
			if edge in borders_to_tiles:
				other_tile = borders_to_tiles[edge]
				tile.orient_to(other_tile)
			else:
				edges_to_tiles[edge] = tile

#

	for tile in new_tiles:
		borders_to_tiles[''.join(tile.top())] += 1
		borders_to_tiles[''.join(tile.right())] += 1
		borders_to_tiles[''.join(tile.bottom())] += 1
		borders_to_tiles[''.join(tile.left())] += 1

		borders_to_tiles[''.join(tile.top())[::-1]] += 1
		borders_to_tiles[''.join(tile.right())[::-1]] += 1
		borders_to_tiles[''.join(tile.bottom())[::-1]] += 1
		borders_to_tiles[''.join(tile.left())[::-1]] += 1

	tile = new_tiles.pop()


main()
