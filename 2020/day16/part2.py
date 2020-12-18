import math
import re
from collections import defaultdict

rules, my_ticket, nearby_tickets = open('input.txt').read().split('\n\n')
rules = {match[0]: tuple(map(int, match[1:])) for match in re.findall(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', rules)}
my_ticket = tuple(map(int, re.findall(r'\d+', my_ticket)))
nearby_tickets = [tuple(map(int, ticket)) for ticket in re.findall(','.join([r'(\d+)'] * len(rules)), nearby_tickets)]

# Filter out invalid tickets.
valid_tickets = [
	ticket for ticket in nearby_tickets if all(
		any(a <= field <= b or c <= field <= d for a, b, c, d in rules.values())
		for field in ticket
	)
]

# Determine possible indices for each fields.
possible_field_indices = defaultdict(set)
for name, (a, b, c, d) in rules.items():
	for possible_index in range(len(rules)):
		if all(a <= ticket[possible_index] <= b or c <= ticket[possible_index] <= d for ticket in valid_tickets):
			possible_field_indices[name].add(possible_index)

# Determine exact indices using process of elimination.
field_indices = {}
for field, indices in sorted(possible_field_indices.items(), key=lambda x: len(x[1])):
	field_indices[field] = next(iter(indices - set(field_indices.values())))

print(math.prod(my_ticket[index] for field, index in field_indices.items() if field.startswith('departure')))
