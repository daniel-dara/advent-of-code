from collections import Counter
from math import prod

numbers = open('input.txt').read().split()
columns = zip(*numbers)
hi_lo_paired_digits = [next(zip(*Counter(row).most_common())) for row in columns]
hi_lo_bit_arrays = list(zip(*hi_lo_paired_digits))
print(prod(int(''.join(bit_array), 2) for bit_array in hi_lo_bit_arrays))
