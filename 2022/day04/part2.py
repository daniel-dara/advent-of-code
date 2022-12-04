import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

v = 0
l = []

for line in open(input_file):
	a, b, c, d = map(int, re.findall('\d+', line))

	if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
		print(a, b, c, d, v)
		v += 1

print(v)
