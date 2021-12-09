import itertools
import re

memory, mask = {}, None

for line in open('input.txt'):
	if 'mask' in line:
		mask = line.split('=')[-1].strip()
	else:
		address, value = map(int, re.findall(r'\d+', line))
		address_bitstr = '{0:b}'.format(address).zfill(len(mask))
		masked_bitlist = [address_bitstr[i] if mask_bit == '0' else mask[i] for i, mask_bit in enumerate(mask)]

		for bits in itertools.product('01', repeat=masked_bitlist.count('X')):
			bit_iter = iter(bits)
			address_bitlist = (next(bit_iter) if char == 'X' else char for char in masked_bitlist)
			memory[int(''.join(address_bitlist), 2)] = value

print(sum(memory.values()))
