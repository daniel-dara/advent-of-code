from collections import Counter, defaultdict

rules = {
	a: b for a, b in
	[line.strip().split(' -> ') for line in open('input.txt').readlines()[2:]]
}

polymer = open('input.txt').readlines()[0].strip()
counts = {key: polymer.count(key) for key in rules}

for _ in range(40):
	new_counts = defaultdict(int)

	for pair, count in counts.items():
		char = rules[pair]
		new_counts[pair[0] + char] += count
		new_counts[char + pair[1]] += count

	counts = new_counts

element_counts = defaultdict(int, {polymer[0]: 1})

for pair, count in counts.items():
	element_counts[pair[1]] += count

most_common = Counter(element_counts).most_common()
print(most_common[0][1] - most_common[-1][1])
