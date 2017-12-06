blocks = list(map(int, open('input.txt').read().split('\t')))
states = set()

while str(blocks) not in states:
	states.add(str(blocks))

	theMax = max(blocks)
	indexOfMax = blocks.index(theMax)

	for i in range(len(blocks)):
		leftovers        = theMax % len(blocks)
		rotatedIndex     = abs(i + (len(blocks) - indexOfMax)) % len(blocks)
		includeLeftovers = rotatedIndex != 0 and rotatedIndex <= leftovers

		blocks[i] += theMax // len(blocks) + int(includeLeftovers)

	blocks[indexOfMax] -= theMax

print(len(states))
