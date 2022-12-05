from __future__ import annotations

from collections import defaultdict
from enum import Enum
from typing import Dict, List, Tuple, DefaultDict


class Tile:
	def __init__(self, image: List[str], string_to_side: Dict[str, Edge.Side]):
		self.image = image
		self.string_to_side = string_to_side


class Edge:
	class Side(Enum):
		TOP = 0
		RIGHT = 1
		BOTTOM = 2
		LEFT = 3

		def __repr__(self):
			return self.name

	def __init__(self, string: str, side: Edge.Side, is_flipped: bool, tile_id: int):
		self.string = string
		self.side = side
		self.is_flipped = is_flipped
		self.tile_id = tile_id

	def __repr__(self) -> str:
		return self.__class__.__name__ + '(' + ', '.join((map(str, self.__dict__.values()))) + ')'


def main():
	id_to_tile: Dict[int, List[str]] = {}
	str_to_edge: DefaultDict[str, List[Edge]] = defaultdict(list)

	# Parse input into id_to_tile and str_to_edge
	for line in open('input.txt').read().strip().split('\n\n'):
		id_, tile = int(line.strip('Tile :.#\n')), line.split('\n')[1:]
		id_to_tile[id_] = tile

		for orientation, string in {
			Edge.Side.TOP:    tile[0],
			Edge.Side.RIGHT:  ''.join(row[-1] for row in tile),
			Edge.Side.BOTTOM: tile[-1],
			Edge.Side.LEFT:   ''.join(row[0] for row in tile),
		}.items():
			str_to_edge[string].append(Edge(string, orientation, False, id_))
			str_to_edge[string[::-1]].append(Edge(string[::-1], orientation, True, id_))

	location_to_tile: Dict[Tuple[int, int], List[str]] = {}

	# For each tile in id_to_tile, lookup each edge in str_to_edge, match and place tile, then pop from both.
	while id_to_tile:
		id_ = next(iter(id_to_tile))
		tile = id_to_tile.pop(id_)

		print(tile)

		for orientation, string in {
			Edge.Side.TOP: tile[0],
			Edge.Side.RIGHT: ''.join(row[-1] for row in tile),
			Edge.Side.BOTTOM: tile[-1],
			Edge.Side.LEFT: ''.join(row[0] for row in tile),
		}.items():
			if len(str_to_edge[string]) > 1:
				a, b = str_to_edge[string]
				matching_transposition = b if a.tile_id == id_ else a
				print(orientation, string, matching_transposition)

			del str_to_edge[string]

		exit()


main()
