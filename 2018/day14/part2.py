# Using the implementation from the previous solution took about 4 minutes to run.
# After optimizing" the Python code to avoid the more expensive operations it now runs in about 1m30s.

targetRecipe = list(map(int, list(open('input.txt').read())))
elves = [0, 1]
recipes = [3, 7]

# The second part of this condition ended up not being necessary but ensures that the recipe is found even
# if it is finished by the '1' in the tens column of a sum.
while targetRecipe != recipes[-len(targetRecipe):] and targetRecipe != recipes[-(len(targetRecipe) + 1):-1]:
	score = recipes[elves[0]] + recipes[elves[1]]

	if score >= 10:
		recipes.append(1)
		recipes.append(score - 10)
	else:
		recipes.append(score)

	elves[0] = (elves[0] + 1 + recipes[elves[0]]) % len(recipes)
	elves[1] = (elves[1] + 1 + recipes[elves[1]]) % len(recipes)

print(len(recipes) - int(recipes[-len(targetRecipe):] != targetRecipe) - len(targetRecipe))
