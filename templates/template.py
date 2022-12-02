import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

v = 0
l = []

for line in open(input_file):
	re.findall(r'\d+', line)

print(v)
