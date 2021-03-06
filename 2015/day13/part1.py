import re
import itertools

potentials = {}

for line in open('input.txt'):
	personA, effect, value, personB = re.match(r'([^ ]+).*(gain|lose) (\d+).* ([^ ]+).', line).groups()
	potentials[(personA, personB)] = int(value) if effect == 'gain' else -int(value)

maxHappiness = 0
for arrangement in itertools.permutations(set([key[1] for key in potentials.keys()])):
	happiness = 0
	circularArrangement = list(arrangement) + [arrangement[0]]

	for i in range(len(circularArrangement) - 1):
		personA, personB = circularArrangement[i:i + 2]
		happiness += potentials[(personA, personB)] + potentials[(personB, personA)]

	maxHappiness = max(maxHappiness, happiness)

print(maxHappiness)
