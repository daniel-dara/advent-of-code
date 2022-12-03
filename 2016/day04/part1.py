import collections
import re

total = 0

for line in open('input.txt'):
	name, sector, checksum = re.findall(r'(.*)-(\d+)\[(.*)]', line)[0]
	counts = collections.Counter(name.replace('-', '')).most_common()
	top5 = sorted(counts, key=lambda x: (-x[1], x[0]))[:5]

	if next(zip(*top5)) == tuple(checksum):
		total += int(sector)

print(total)
