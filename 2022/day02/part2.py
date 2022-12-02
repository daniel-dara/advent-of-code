import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

v = 0
l = []

a1 = 'ABC'
b1 = 'XYZ'

for line in open(input_file):
	a, b = line.strip().split(' ')

	if b == 'X':
		b = b1[(a1.index(a) - 1) % 3]
	elif b == 'Y':
		b = b1[a1.index(a)]
	else:
		b = b1[(a1.index(a) + 1) % 3]

	v += b1.index(b) + 1

	if a1.index(a) == b1.index(b):
		v += 3
	elif (a1.index(a) + 1) % 3 == b1.index(b):
		v += 6

print(v)

# 11386
