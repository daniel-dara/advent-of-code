containers = list(map(int, open('input.txt').read().split('\n')))
maxLiters = 150
combos = set()
fullComboCount = 0

def fill(currentCombo, currentLiters):
	global fullComboCount

	if currentLiters > maxLiters or currentCombo in combos:
		return

	if currentLiters == maxLiters:
		fullComboCount += 1
		return

	combos.add(currentCombo)

	lastContainerIndex = -1 if currentCombo == () else currentCombo[-1]

	for i in range(lastContainerIndex + 1, len(containers)):
		fill(currentCombo + (i,), currentLiters + containers[i])

fill((), 0)

print(fullComboCount)
