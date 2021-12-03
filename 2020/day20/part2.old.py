from typing import Tuple, List

import numpy

tiles = {}
edges = {}

for tile in open('input.txt').read().strip().split('\n\n'):
	tile_id, *tile = tile.split('\n')
	tiles[tile_id.strip('Tile :')] = tuple(tuple(row) for row in tile)
	edges[tile_id.strip('Tile :')] = (
		tuple(tile[0]),                  # top
		tuple(row[-1] for row in tile),  # right
		tuple(tile[-1]),                 # bottom
		tuple(row[0] for row in tile),   # left
	)

# Stores tiles at (x, y) coordinates
image = {}


def find_pieces(location: Tuple[int, int], tile_id: str, tile: List[List[str]]) -> None:
	"""Fit and remove the current piece from the pile of remaining pieces. Search for more pieces that fit and recurse
	on them.
	"""
	del edges[tile_id]
	del tiles[tile_id]
	image[location] = tile

	found_pieces = []

	for other_id, other_tile in tiles.items():
		match = set(edges[tile_id]) & set(edges[other_id])

		# TODO Fix matching logic since as the piece rotates twice the edges effectively flip
		if match:
			index = edges[tile_id].index(match)
			original_index = edges[other_id].index(match)
			new_location = (
				(location[0] + 1 if index == 1 else -1 if index == 3 else 0),
				(location[1] + 1 if index == 0 else -1 if index == 2 else 0)
			)
			found_pieces.append((new_location, other_id, numpy.rot90(numpy.ndarray(tile), (index - original_index + 2) % 4)))
			continue

		match = set(image[location]) & set(edge[::-1] for edge in other_tile)

		if match:
			index = other_tile.index(match[::-1])
			new_location = (location[0] + 1 if index == 3 else -1 if index == 2 else 0), (location[1] + 1 if index == 0 else -1 if index == 1 else 0)
			found_pieces.append((new_location, other_id, True))

	for info in found_pieces:
		find_pieces(*info)


find_pieces((0, 0), next(iter(tiles)), False)
