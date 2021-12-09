import itertools


numbers = list(map(int, open('input.txt').readlines()))
print(next(
	numbers[i] for i in range(25, len(numbers))
	if all(
		a + b != numbers[i]
		for a, b in itertools.combinations(numbers[i - 25:i], 2)
	)
))
