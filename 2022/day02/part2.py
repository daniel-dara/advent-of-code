import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

for line in open(input_file):
	re.findall(r'\d+', line)
