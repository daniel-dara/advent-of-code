import re

rules, _, nearby_tickets = map(
	lambda string: tuple(map(int, re.findall(r'\d+', string))),
	open('input.txt').read().split('\n\n')
)

print(sum(
	0 if any(
		rules[j] <= field <= rules[j + 1] or rules[j + 2] <= field <= rules[j + 3]
		for j in range(0, len(rules), 4)
	) else field
	for field in nearby_tickets
))
