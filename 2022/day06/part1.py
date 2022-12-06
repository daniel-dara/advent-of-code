import re
import itertools
import collections
import math

# input_file = 'example.txt'
input_file = 'input.txt'

v = 0
l = []

seen = set()
file = open(input_file).read()

for i in range(len(file)):
	if len(set(file[i:i + 4])) == 4:
		print(i + 4)
		exit()

print(v)
