import re

VOWEL_PATTERN  = re.compile(r'(\w\w).*\1')
REPEAT_PATTERN = re.compile(r'(\w)\w\1')

print(sum(int(VOWEL_PATTERN.search(line) != None and
	          REPEAT_PATTERN.search(line) != None)
		  for line in open('input.txt')))
