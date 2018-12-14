targetRecipes = int(open('input.txt').read())
elves = [0, 1]
recipes = [3, 7]

while len(recipes) < targetRecipes + 10:
	recipes += list(map(int, list(str(recipes[elves[0]] + recipes[elves[1]]))))

	for i in range(len(elves)):
		elves[i] = (elves[i] + 1 + recipes[elves[i]]) % len(recipes)

print(''.join(map(str, recipes[targetRecipes:targetRecipes + 10])))
