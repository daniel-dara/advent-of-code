visible = set()
trees = [list(map(int, line.strip())) for line in open('input.txt').readlines()]

for a in range(len(trees)):
	maxes = [-1] * 4

	for b in range(len(trees[0])):
		for i, (A, B) in enumerate((
			(a, b),
			(a, len(trees[a]) - b - 1),
			(b, a),
			(len(trees) - b - 1, a)
		)):
			if trees[A][B] > maxes[i]:
				visible.add((A, B))
				maxes[i] = trees[A][B]

print(len(visible))
