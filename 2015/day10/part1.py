import re

repeated_digits = re.compile(r'((\d)\2*)')
sequence = open('input.txt').read()

for _ in range(40):
	sequence = ''.join([(str(len(repeats)) + digit) for repeats, digit in re.findall(repeated_digits, sequence)])

print(len(sequence))