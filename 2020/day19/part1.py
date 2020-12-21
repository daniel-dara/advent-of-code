import re

rule_input, messages = (lines.split('\n') for lines in open('input.txt').read().split('\n\n'))
rules = {}

for line in rule_input:
	rule, production = line.split(': ')

	if '"' in production:
		rules[rule] = [production.strip('"')]
	else:
		rules[rule] = ['('] + production.split() + [')']

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

print(len(tuple(filter(lambda s: re.fullmatch(''.join(regex), s), messages))))
