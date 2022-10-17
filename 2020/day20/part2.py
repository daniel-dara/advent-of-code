from collections import defaultdict
from enum import Enum
from typing import Dict, List, Tuple, DefaultDict


class Edge(Enum):
	TOP = 0
	RIGHT = 1
	BOTTOM = 2
	LEFT = 3


class Transposition:
	def __init__(self, tile_id: int, edge: Edge, edge_str: str, is_flipped: bool):
		self.tile_id = tile_id
		self.edge = edge
		self.edge_str = edge_str
		self.is_flipped = is_flipped

	def __repr__(self) -> str:
		return str(self.tile_id)


def main():
	id_to_tile: Dict[int, List[str]] = {}  # Parse from input
	edge_to_transposition: DefaultDict[str, List[Transposition]] = defaultdict(list)  # Populate from id_to_tile

	for string in open('input.txt').read().strip().split('\n\n'):
		id_, tile = int(string.strip('Tile :.#\n')), string.split('\n')[1:]
		id_to_tile[id_] = tile

		for edge, edge_str in {
			Edge.TOP: tile[0],
			Edge.RIGHT: ''.join(row[-1] for row in tile),
			Edge.BOTTOM: tile[-1],
			Edge.LEFT: ''.join(row[0] for row in tile),
		}.items():
			edge_to_transposition[edge_str].append(Transposition(id_, edge, edge_str, False))
			edge_to_transposition[edge_str[::-1]].append(Transposition(id_, edge, edge_str[::-1], True))

	# max in set is 4, I'm guessing palindrome edges
	print(max(len(s) for edge, s in edge_to_transposition.items()))
	print(min(len(s) for edge, s in edge_to_transposition.items()))

	# Iterate id_to_tile, lookup in edge_to_transposition, pop from both
	location_to_tile: Dict[Tuple[int, int], List[str]] = {}


main()
