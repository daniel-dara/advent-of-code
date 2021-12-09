import re

memory, mask = {}, None

for line in open('input.txt'):
	if 'mask' in line:
		mask = line.split('=')[-1].strip()
	else:
		address, value = map(int, re.findall(r'\d+', line))
		value_bitstr = '{0:b}'.format(value).zfill(len(mask))
		value_bitlist = (value_bitstr[i] if mask_bit == 'X' else mask_bit for i, mask_bit in enumerate(mask))
		memory[address] = int(''.join(value_bitlist), 2)

print(sum(memory.values()))
