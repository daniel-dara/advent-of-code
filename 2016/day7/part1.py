import re

SPLIT_PATTERN = re.compile(r'[^\[\]]+')
ABBA_PATTERN  = re.compile(r'([a-z])(?!\1)([a-z])\2\1')
supported_ips = 0

for line in open('input.txt').readlines():
	aggregate = ['', '']

	for index, piece in enumerate(SPLIT_PATTERN.findall(line)):
		aggregate[index % 2] += piece + '-'

	if ABBA_PATTERN.search(aggregate[0]) and not ABBA_PATTERN.search(aggregate[1]):
		supported_ips += 1

print(supported_ips)