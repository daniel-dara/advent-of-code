import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

v = 0
l = []

for line in open(input_file):
	a, b = line[:len(line) // 2], line[len(line) // 2:]
	a = set(list(a))
	b = set(list(b))

	letter = next(iter(a.intersection(b)))

	if letter == letter.lower():
		v += ord(letter) - ord('a') + 1
	else:
		v += ord(letter) - ord('A') + 27

print(v)
