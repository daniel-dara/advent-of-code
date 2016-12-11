import re

VOWEL_PATTERN  = re.compile(r'a|e|i|o|u')
DOUBLE_PATTERN = re.compile(r'(\w)\1')
AVOID_PATTERN  = re.compile(r'ab|cd|pq|xy')

print(sum(int(len(VOWEL_PATTERN.findall(line)) >= 3 and
	              DOUBLE_PATTERN.search(line) != None and
	              AVOID_PATTERN.search(line) == None)
		  for line in open('input.txt')))
