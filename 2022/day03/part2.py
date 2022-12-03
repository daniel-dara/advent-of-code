import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

v = 0
l = []

lines = list(map(str.strip, open(input_file).readlines()))

for i in range(len(lines) // 3):
	a = set(lines[3 * i])
	b = set(lines[3 * i + 1])
	c = set(lines[3 * i + 2])

	letter = next(iter(a.intersection(b).intersection(c)))

	if letter == letter.lower():
		v += ord(letter) - ord('a') + 1
	else:
		v += ord(letter) - ord('A') + 27

print(v)
