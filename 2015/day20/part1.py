
houses = [0] * 2_900_000

for i in range(len(houses)):
	for j in range(i, len(houses), i + 1):
		houses[j] += i + 1

print(next(index + 1 for index, presents in enumerate(houses) if presents >= 2_900_000))
