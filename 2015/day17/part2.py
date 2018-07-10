from collections import defaultdict

containers = list(map(int, open('input.txt').read().split('\n')))
maxLiters = 150
combos = set()
fullComboLengths = defaultdict(lambda: 0)

def fill(currentCombo, currentLiters):
	if currentLiters > maxLiters or currentCombo in combos:
		return

	combos.add(currentCombo)

	if currentLiters == maxLiters:
		fullComboLengths[len(currentCombo)] += 1
		return

	lastContainerIndex = -1 if currentCombo == () else currentCombo[-1]

	for i in range(lastContainerIndex + 1, len(containers)):
		fill(currentCombo + (i,), currentLiters + containers[i])

fill((), 0)

print(fullComboLengths[min(fullComboLengths.keys())])
