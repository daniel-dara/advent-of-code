from collections import defaultdict

components = defaultdict(lambda: [])

for component in open('input.txt'):
	a, b = map(int, component.split('/'))
	components[a].append(b)
	components[b].append(a)


def find_strongest(connector: int = 0, strength: int = 0) -> int:
	strengths = []

	for index in range(len(components[connector])):
		next_connector = components[connector][index]

		components[connector].remove(next_connector)
		components[next_connector].remove(connector)

		strengths.append(find_strongest(next_connector, strength + connector + next_connector))

		components[connector].insert(index, next_connector)
		components[next_connector].insert(index, connector)

	return max(strengths) if strengths else strength


print(find_strongest())
