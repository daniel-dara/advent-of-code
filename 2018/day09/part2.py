import re
from collections import deque

# Parse input.
players, marbles = map(int, re.findall(r'(\d+)', open('input.txt').read()))

# Increase marbles per problem statement.
marbles *= 100

scores = [0] * players
circle = deque([0])
currentPlayer = 0
currentMarble = 1

# This solution uses a deque for faster operations at the ends of the queue. Thus the current marble
# is kept at the front of the queue using rotations so pop/appendleft are O(1).
while currentMarble <= marbles:
	if currentMarble % 23 == 0:
		# Remove and score the marble 7 marbles to the left of the current one. Popping this marble
		# bumps the marble to its right into the current index so modifying index a second time is not
		# necessary.
		circle.rotate(6)
		scores[currentPlayer] += currentMarble + circle.pop()
	else:
		# Insert new marble between the 1st and 2nd marbles to the right of the current one.
		circle.rotate(-2)
		circle.appendleft(currentMarble)

	currentMarble += 1
	currentPlayer = (currentPlayer + 1) % players

print(max(scores))
