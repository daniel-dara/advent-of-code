blocks = list(map(int, open('input.txt').read().split('\t')))
states = {}

while str(blocks) not in states:
	states[str(blocks)] = len(states)

	theMax = max(blocks)
	indexOfMax = blocks.index(theMax)

	for i in range(len(blocks)):
		leftovers        = theMax % len(blocks)
		rotatedIndex     = abs(i + (len(blocks) - indexOfMax)) % len(blocks)
		includeLeftovers = rotatedIndex != 0 and rotatedIndex <= leftovers

		blocks[i] += theMax // len(blocks) + int(includeLeftovers)

	blocks[indexOfMax] -= theMax

print(len(states) - states[str(blocks)])
