from math import prod

ratings = sorted(map(int, open('input.txt').readlines()))
ratings = [0] + ratings + [ratings[-1] + 3]

print(prod(map(sum, zip(
	*((b - a == 1, b - a == 3) for a, b in zip(ratings, ratings[1:]))
))))
