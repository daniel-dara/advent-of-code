from collections import Counter

polymer = open('input.txt').readlines()[0].strip()

rules = {
	a: b for a, b in
	[line.strip().split(' -> ') for line in open('input.txt').readlines()[2:]]
}

for _ in range(10):
	polymer = polymer[0] + ''.join(rules[a + b] + b for a, b in zip(polymer, polymer[1:]))

most_common = Counter(polymer).most_common()
print(most_common[0][1] - most_common[-1][1])
