
deltas = eval(open('input.txt').read().replace('\n', ','))

total = 0
previousTotals = set()
i = 0

while total not in previousTotals:
	previousTotals.add(total)

	total += deltas[i]

	i = (i + 1) % len(deltas)

print(total)
