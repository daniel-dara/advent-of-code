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
		tuple(tile[-1][::-1]),                 # bottom
		tuple(row[0] for row in tile[::-1]),   # left
	)

# Stores tiles at (x, y) coordinates
image = {}

# tile = '..#.\n#...\n...#\n.#..'.split('\n')

tile = tiles.pop()

while tiles:
