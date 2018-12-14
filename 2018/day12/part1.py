import re

inputLines = open('input.txt').readlines()
state = list(inputLines[0].split(':')[1].strip())
rules = re.findall(r'(.*) => #', '\n'.join(inputLines))

index = 0

for _ in range(20):
	periodsToAdd = (5 - min(5, state.index('#')))
	index -= periodsToAdd

	state = ['.'] * periodsToAdd + state + ['.'] * (5 - (state[-5:][::-1] + ['#']).index('#'))
	newState = ['.', '.']

	for i in range(len(state) - 5):
		newState.append('#' if ''.join(state[i:i + 5]) in rules else '.')

	state = newState

finalState = ''.join(state)
total = 0

for i in range(len(finalState)):
	total += index if finalState[i] == '#' else 0
	index += 1

print(total)
