from collections import defaultdict
from enum import Enum
from typing import Dict, List, Tuple, DefaultDict


class Orientation(Enum):
	TOP = 0
	RIGHT = 1
	BOTTOM = 2
	LEFT = 3


class Tile:
	def __init__(self, image: List[str], edge_to_orientation: Dict[str, Orientation]):
		self.image = image
		self.edge_to_orientation = edge_to_orientation


class Transposition:
	def __init__(self, tile_id: int, orientation: Orientation, edge: str, is_flipped: bool):
		self.tile_id = tile_id
		self.orientation = orientation
		self.edge = edge
		self.is_flipped = is_flipped

	def __repr__(self) -> str:
		return (
			'Transposition('
			+ str(self.tile_id)
			+ ', ' + str(self.orientation)
			+ ', ' + self.edge
			+ ', ' + str(self.is_flipped)
			+ ')'
		)


def main():
	id_to_tile: Dict[int, List[str]] = {}  # Parse from input
	edge_to_transposition: DefaultDict[str, List[Transposition]] = defaultdict(list)  # Populate from id_to_tile

	for string in open('input.txt').read().strip().split('\n\n'):
		id_, tile = int(string.strip('Tile :.#\n')), string.split('\n')[1:]
		id_to_tile[id_] = tile

		for orientation, edge in {
			Orientation.TOP:    tile[0],
			Orientation.RIGHT:  ''.join(row[-1] for row in tile),
			Orientation.BOTTOM: tile[-1],
			Orientation.LEFT:   ''.join(row[0] for row in tile),
		}.items():
			edge_to_transposition[edge].append(Transposition(id_, orientation, edge, False))
			edge_to_transposition[edge[::-1]].append(Transposition(id_, orientation, edge[::-1], True))

	# Iterate id_to_tile, lookup in edge_to_transposition, pop from both
	location_to_tile: Dict[Tuple[int, int], List[str]] = {}

	while id_to_tile:
		id_ = next(iter(id_to_tile))
		tile = id_to_tile.pop(id_)

		print(tile)

		for orientation, edge in {
			Orientation.TOP: tile[0],
			Orientation.RIGHT: ''.join(row[-1] for row in tile),
			Orientation.BOTTOM: tile[-1],
			Orientation.LEFT: ''.join(row[0] for row in tile),
		}.items():
			if len(edge_to_transposition[edge]) > 1:
				a, b = edge_to_transposition[edge]
				matching_transposition = b if a.tile_id == id_ else a
				print(orientation, edge, matching_transposition)

			del edge_to_transposition[edge]

		exit()


main()
