severity = 0

for line in open('input.txt'):
	layer, scanRange = map(int, line.rstrip().split(': '))

	if layer > 0 and layer % (2 * (scanRange - 1)) == 0:
		severity += layer * scanRange

print(severity)