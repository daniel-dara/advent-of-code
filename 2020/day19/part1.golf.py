import re

rule_input, messages = (lines.split('\n') for lines in open('input.txt').read().split('\n\n'))
rules = {line.split(': ')[0]: ['('] + line.split(': ')[1].strip('"').split() + [')'] for line in rule_input}
regex = ['0']

while any(part in rules for part in regex):
	regex = sum((rules[part] if part in rules else [part] for part in regex), start=[])

print(len(tuple(filter(lambda s: re.fullmatch(''.join(regex), s), messages))))
