import re

SPLIT_PATTERN = re.compile(r'[^\[\]]+')
ABA_PATTERN   = re.compile(r'(?=([a-z])(?!\1)([a-z])(\1))')
supported_ips = 0

for line in open('input.txt').readlines():
	aggregate = ['', '']

	for index, piece in enumerate(SPLIT_PATTERN.findall(line)):
		aggregate[index % 2] += piece + '-'

	for match in ABA_PATTERN.finditer(aggregate[0]):
		aba = ''.join(match.groups())
		bab = aba[1] + aba[0] + aba[1]

		if bab in aggregate[1]:
			supported_ips += 1
			break

print(supported_ips)