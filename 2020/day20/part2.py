from __future__ import annotations

from collections import defaultdict
from enum import Enum
from typing import Dict, List, Tuple, DefaultDict

Location = Tuple[int, int]


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
	id_to_tile: Dict[int, Tile] = {}
	string_to_edges: DefaultDict[str, List[Edge]] = defaultdict(list)

	# Parse input into id_to_tile and string_to_edges.
	for line in open('input.txt').read().strip().split('\n\n'):
		id_, image = int(line.strip('Tile :.#\n')), line.split('\n')[1:]

		string_to_side = {
			image[0]: Edge.Side.TOP,
			''.join(row[-1] for row in image): Edge.Side.RIGHT,
			image[-1]: Edge.Side.BOTTOM,
			''.join(row[0] for row in image): Edge.Side.LEFT,
		}

		id_to_tile[id_] = Tile(image, string_to_side)

		for string, side in string_to_side.items():
			string_to_edges[string].append(Edge(string, side, False, id_))
			string_to_edges[string[::-1]].append(Edge(string[::-1], side, True, id_))

	# Queue of (location, tile_id) to find matches for.
	queue = [((0, 0), next(iter(id_to_tile)))]

	location_to_tile: Dict[Location, Tile] = {}

	while queue:
		location, id_ = queue.pop(0)
		tile = id_to_tile.pop(id_)

		# Assign the tile to the location map.
		location_to_tile[location] = tile

		# Loop over each side of the tile.
		for string, side in tile.string_to_side:
			# Look for other edges that match.
			matches = [edge for edge in string_to_edges[string] if edge.tile_id != id_]

			if matches:
				matching_edge = matches[0]

				# Add tile to queue
				# todo calculate new location
				new_location = (0, 0)
				queue.append((new_location, matching_edge.tile_id))

				# Remove the matching tile from lists
				matching_tile = id_to_tile.pop(matching_edge.tile_id)

				# todo remove all edges
				string_to_edges[string].remove(matching_edge)

				# todo rotate and flip matching_tile based on the edge, update string_to_side
				# matching_tile.rotate().flip().orient()


main()
