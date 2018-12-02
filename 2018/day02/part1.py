from collections import Counter

twos = 0
threes = 0

for line in open('input.txt'):
	occurences = list(map(lambda x: x[1], Counter(line).most_common()))

	twos += 2 in occurences
	threes += 3 in occurences

print(twos * threes)
