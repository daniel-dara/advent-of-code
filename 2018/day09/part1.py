import re

# Parse input.
players, marbles = map(int, re.findall(r'(\d+)', open('input.txt').read()))

scores = [0] * players
circle = [0]
currentIndex = 0
currentPlayer = 0
currentMarble = 1

# This solution uses list manipulation and tracks the index of the current marble.
while currentMarble <= marbles:
	if currentMarble % 23 == 0:
		# Remove and score the marble 7 marbles to the left of the current one. Popping this marble
		# bumps the marble to its right into the current index so modifying index a second time is not
		# necessary.
		nextIndex = (currentIndex - 7) % len(circle)
		scores[currentPlayer] += currentMarble + circle.pop(nextIndex)
	else:
		# Insert new marble between the 1st and 2nd marbles to the right of the current one.
		nextIndex = ((currentIndex + 1) % len(circle)) + 1
		circle.insert(nextIndex, currentMarble)

	currentIndex = nextIndex
	currentMarble += 1
	currentPlayer = (currentPlayer + 1) % players

print(max(scores))
