from collections import defaultdict

components = defaultdict(lambda: [])

for component in open('input.txt'):
	a, b = map(int, component.split('/'))
	components[a].append(b)
	components[b].append(a)


def find_longest(connector: int = 0, length: int = 0, strength: int = 0) -> int:
	attributes = []

	for index in range(len(components[connector])):
		next_connector = components[connector][index]

		components[connector].remove(next_connector)
		components[next_connector].remove(connector)

		attributes.append(find_longest(next_connector, length + 1, strength + connector + next_connector))

		components[connector].insert(index, next_connector)
		components[next_connector].insert(index, connector)

	return max(attributes) if attributes else (length, strength)


print(find_longest()[1])
