import re
import string

# runtime: 6s

polymer = open('input.txt').read()

def react(polymer):
	previousLength = 0

	while previousLength != len(polymer):
		previousLength = len(polymer)
		polymer = re.sub(r'(\w)(?!\1)(?i:\1)', '', polymer)

	return polymer

reducedPolymer = react(polymer)

print(min(len(react(reducedPolymer.replace(char, '').replace(char.upper(), ''))) for char in string.ascii_lowercase))
