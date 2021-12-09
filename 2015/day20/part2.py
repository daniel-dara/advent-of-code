houses = [0] * 2_900_000

for i in range(1, len(houses) + 1):
	for j in range(i - 1, min(50 * i, len(houses)), i):
		houses[j] += i * 11

print(next(index + 1 for index, presents in enumerate(houses) if presents >= 29_000_000))
