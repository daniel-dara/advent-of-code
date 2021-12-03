from collections import Counter
from math import prod

numbers = open('example.txt').read().split()
columns = zip(*numbers)
hi_lo_digits = [next(zip(*Counter(row).most_common())) for row in columns]
bit_array = list(zip(*hi_lo_digits))
print(prod(int(''.join(bits), 2) for bits in bit_array))