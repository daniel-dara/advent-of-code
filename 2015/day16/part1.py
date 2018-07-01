import re

sueTraits = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1
}

def isSue(traits):
	for trait in traits:
		name, value = trait.split(': ')

		if sueTraits[name] != int(value):
			return False

	return True

for line in open('input.txt'):
	sue = line.split(':')[0].split(' ')[1]
	traits = re.findall(r'(\w+: \d+)', line)

	if isSue(traits):
		print(sue)
		break
	