# This solution uses a BFS (breadth-first search) to find the shortest path from start to finish.

from hashlib import md5

# Input from problem statement, for use in calculating the hash of the path.
passcode = 'pxxbnzuo'

# A queue to hold the new states to try. Each state is a 3-tuple containing x and y coordinates and the
# path taken so far. The path is represented by a string of U, D, L, R characters where each one represents one move in
# that direction. The starting location is at 0, 0 and the path is empty since no moves have been made.
queue = [(0, 0, '')]

# (x, y) of the destination
destination = (3, 3)

# This function determines which doors are unlocked for a given path. It uses the algorithm in the problem statement.
# 1) Take the hex representation of the md5 hash of passcode + path
# 2) The first four characters of the hash correspond to the doors U, D, L, and R of the current position.
# 3) If a given character is b, c, d, e, or f, then the door is unlocked, otherwise it remains locked.
#
# The return value is a four element array of booleans where the elements represent the doors U, D, L, R of the current
# position and True = unlocked and False = locked.
def unlock(path):
	return [not c.isdigit() and c != 'a' for c in md5(bytes(passcode + path, 'ascii')).hexdigest()[:4]]

# This function performs a breadth-first search of the state space and returns the shortest path to the destination.
def findShortestPath():
	# This condition loops until the queue is empty. Because a BFS is being used to find the shortest path, the only
	# time this condition would be false is if there is NO path at all to the destination. Otherwise, the moment a valid
	# path is found a 'return' is hit and exits the loop on its own.
	while queue:
		# As part of BFS, states (aka nodes) need to be explored first to last. As new states are discovered, they are
		# added to the end of the queue. Therefore the front of the queue is explored first.
		x, y, path = queue.pop(0)

		# If the current path led to the destination, the BFS is done and the path can be returned. Due to the nature
		# of BFS, the first solution found is guaranteed to be the shortest.
		if (x, y) == destination:
			return path

		# Make sure the current path hasn't gone out-of-bounds. For large searches, you typically want to check boundries
		# BEFORE adding a state to the queue to avoid the extra queueing overhead. However the state space for this problem
		# is small enough to where it doesn't matter. And checking the boundries here means it only has to be done once
		# instead of duplicated for each queueing condition.
		if x < 0 or y < 0 or x >= 4 or y >= 4:
			continue

		# Try to unlock doors for the given path.
		# KEY POINT: Doors do not stay unlocked. The problem statement doesn't make this clear but the example solution does.
		# Because doors don't stay locked, the problem is somewhat easier as the door states don't have to be tracked.
		# Simply try all doors again each move.
		unlocked = unlock(path)

		# For each door (U, D, L, R), if it is unlocked, "go through it" by adding a new state to the queue. The new state
		# has an appropriately modified (x, y) and has the new move appended to the path.
		if unlocked[0]:
			queue.append((x, y - 1, path + 'U'))

		if unlocked[1]:
			queue.append((x, y + 1, path + 'D'))

		if unlocked[2]:
			queue.append((x - 1, y, path + 'L'))

		if unlocked[3]:
			queue.append((x + 1, y, path + 'R'))

# All that's left is to print the result of calling our function.
print(findShortestPath())
