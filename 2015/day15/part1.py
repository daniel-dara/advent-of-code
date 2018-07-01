import re

ingredients = []

for line in open('input.txt'):
	ingredients.append(list(map(int, re.findall(r'-?\d', line))))

def getScore(amounts):
	score = 1;

	for i in range(len(ingredients[0]) - 1):
		subScore = 0

		for j in range(len(ingredients)):
			subScore += amounts[j] * ingredients[j][i]

		if subScore < 0:
			return 0

		score *= subScore

	return score

def getAllAmounts(amounts):
	if len(amounts) == len(ingredients):
		yield amounts
	elif len(amounts) == len(ingredients) - 1:
		yield amounts + [100 - sum(amounts)]
	else:
		for amount in range(101 - sum(amounts)):
			yield from getAllAmounts(amounts + [amount])

bestScore = 0

for amounts in getAllAmounts([]):
	bestScore = max(bestScore, getScore(amounts))

print(bestScore)
