# Almost the same as part1. Instead of finding the shortest path, this solution finds the longest path but still uses
# a BFS. Instead of stopping at the first solution found (the shortest) it runs through all pathes to guarantee it finds
# the longest.
#
# Only the differences in this solution have comments so see part1 for a full recap.

from hashlib import md5

passcode = 'pxxbnzuo'
queue = [(0, 0, '')]
destination = (3, 3)

def unlock(path):
	return [not c.isdigit() and c != 'a' for c in md5(bytes(passcode + path, 'ascii')).hexdigest()[:4]]

def findLongestPath():
	while queue:
		x, y, path = queue.pop(0)

		if (x, y) == destination:
			# This is the main difference from part 1. Instead of immediately returning when the first valid path is
			# found, the path is simply stored and the search continues from the next state until all paths are checked.
			# In BFS, the first path found is the shortest and the last path found is the longest. Therefore the paths
			# don't have to be stored just the last one.
			longest_path = path
			continue

		if x < 0 or y < 0 or x >= 4 or y >= 4:
			continue

		unlocked = unlock(path)

		if unlocked[0]:
			queue.append((x, y - 1, path + 'U'))

		if unlocked[1]:
			queue.append((x, y + 1, path + 'D'))

		if unlocked[2]:
			queue.append((x - 1, y, path + 'L'))

		if unlocked[3]:
			queue.append((x + 1, y, path + 'R'))

	# This line could error if no paths were found because longest_path could be undefined. Advent of code problems
	# always have solutions though so that doesn't have to be accounted for in this case.
	return longest_path

# All that's left is to print the length of the longest path returned by the function.
print(len(findLongestPath()))
