from collections import defaultdict

left = []
right_occurrences = defaultdict(int)

for line in open('input.txt'):
	a, b = map(int, line.split())
	left.append(a)
	right_occurrences[b] += 1

print(sum(right_occurrences[num] * num for num in left))
