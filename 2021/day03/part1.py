from math import prod

binary_numbers = open('input.txt').read().split()
digit_columns = zip(*binary_numbers)
hi_lo_paired_digits = [('1', '0') if digits.count('1') > len(digits) / 2 else ('0', '1') for digits in digit_columns]
hi_lo_bit_arrays = list(zip(*hi_lo_paired_digits))
print(prod(int(''.join(bit_array), 2) for bit_array in hi_lo_bit_arrays))
