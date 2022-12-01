from collections import defaultdict
from enum import Enum
from typing import Dict, List, Tuple, DefaultDict


class Edge(Enum):
	TOP = 0
	RIGHT = 1
	BOTTOM = 2
	LEFT = 3


class Tile:
	def __init__(self, image: List[str], str_to_edge: Dict[str, Edge]):
		self.image = image
		self.str_to_edge = str_to_edge


class Transposition:
	def __init__(self, tile_id: int, edge: Edge, edge_str: str, is_flipped: bool):
		self.tile_id = tile_id
		self.edge = edge
		self.edge_str = edge_str
		self.is_flipped = is_flipped

	def __repr__(self) -> str:
		return 'Transition(' + str(self.tile_id) + ', ' + str(self.edge) + ', ' + self.edge_str + ', ' + str(self.is_flipped) + ')'


def main():
	id_to_tile: Dict[int, List[str]] = {}  # Parse from input
	edge_str_to_transposition: DefaultDict[str, List[Transposition]] = defaultdict(list)  # Populate from id_to_tile

	for string in open('input.txt').read().strip().split('\n\n'):
		id_, tile = int(string.strip('Tile :.#\n')), string.split('\n')[1:]
		id_to_tile[id_] = tile

		for edge, edge_str in {
			Edge.TOP: tile[0],
			Edge.RIGHT: ''.join(row[-1] for row in tile),
			Edge.BOTTOM: tile[-1],
			Edge.LEFT: ''.join(row[0] for row in tile),
		}.items():
			edge_str_to_transposition[edge_str].append(Transposition(id_, edge, edge_str, False))
			edge_str_to_transposition[edge_str[::-1]].append(Transposition(id_, edge, edge_str[::-1], True))

	# Iterate id_to_tile, lookup in edge_to_transposition, pop from both
	location_to_tile: Dict[Tuple[int, int], List[str]] = {}

	while id_to_tile:
		id_ = next(iter(id_to_tile))
		tile = id_to_tile.pop(id_)

		print(tile)

		for edge, edge_str in {
			Edge.TOP: tile[0],
			Edge.RIGHT: ''.join(row[-1] for row in tile),
			Edge.BOTTOM: tile[-1],
			Edge.LEFT: ''.join(row[0] for row in tile),
		}.items():
			if len(edge_str_to_transposition[edge_str]) > 1:
				a, b = edge_str_to_transposition[edge_str]
				matching_transposition = b if a.tile_id == id_ else a
				print(edge, edge_str, matching_transposition)

			del edge_str_to_transposition[edge_str]

		exit()


main()
