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

	if a <= c and b >= d or c <= a and d >= b:
		v += 1

print(v)
