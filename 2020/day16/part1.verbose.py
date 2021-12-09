import re

rules, _, nearby_tickets = map(
	lambda string: tuple(map(int, re.findall(r'\d+', string))),
	open('input.txt').read().split('\n\n')
)

errors = 0

for field in nearby_tickets:
	is_valid_field = False

	for j in range(0, len(rules), 4):
		a, b, c, d = rules[j:j + 4]

		if a <= field <= b or c <= field <= d:
			is_valid_field = True
			break

	errors += 0 if is_valid_field else field

print(errors)
