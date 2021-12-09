import re

rule_input, messages = (lines.split('\n') for lines in open('input.txt').read().split('\n\n'))
rules = {line.split(': ')[0]: ['(?:'] + line.split(': ')[1].strip('"').split() + [')'] for line in rule_input}

# Only a single 42 is needed for 8 as the remaining 42s can be considered part of rule 11.
# Then any number of 42s can be "given back" if there are more 42s than 31s in 11.
rules['8'] = '(?: 42 )'.split()
rules['11'] = '( (?: 42 ) + ) ( (?: 31 ) + )'.split()
regex = ['0']

while any(part in rules for part in regex):
	regex = sum((rules[part] if part in rules else [part] for part in regex), start=[])

regex_matches = (re.fullmatch(''.join(regex), message) for message in messages)
print(sum(1 for match in regex_matches if match and len(match.group(1)) >= len(match.group(2))))
