import re

for line in open('input.txt'):
	name, sector = re.findall(r'(.*)-(\d+)', line)[0]
	shifted = [chr(ord('a') + (ord(c) - ord('a') + int(sector)) % 26) for c in name if c != '-']

	if 'northpole' in ''.join(shifted):
		print(sector)
		break
