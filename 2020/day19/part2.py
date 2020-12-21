import re

rule_input, messages = (lines.split('\n') for lines in open('input.txt').read().split('\n\n'))
rules = {}

for line in rule_input:
	rule, production = line.split(': ')

	if '"' in production:
		rules[rule] = [production.strip('"')]
	else:
		rules[rule] = ['(?:'] + production.split() + [')']

# Only a single 42 is needed for 8 as the remaining 42s can be considered part of rule 11.
# Then any number of 42s can be "given back" if there are more 42s than 31s in 11.
rules['8'] = '(?: 42 )'.split()
rules['11'] = '( (?: 42 ) + ) ( (?: 31 ) + )'.split()

regex = []
next_expansion = ['0']

while regex != next_expansion:
	regex = next_expansion
	next_expansion = []

	for part in regex:
		if part in rules:
			next_expansion += rules[part]
		else:
			next_expansion += part

matches = 0
for message in messages:
	match = re.fullmatch(''.join(regex), message)

	if match and len(match.group(1)) >= len(match.group(2)):
		matches += 1

print(matches)
