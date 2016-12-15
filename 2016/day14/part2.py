from hashlib import md5
import re

index  = 0
keys   = []
hashes = []

def generateHash(num):
	md5hash = 'yjdafjpo' + str(num)

	for i in range(2017):
		md5hash = md5(bytes(md5hash, 'ascii')).hexdigest()

	quintuples = re.findall(r'(\d|\w)\1\1\1\1', md5hash)

	hashes.append((md5hash, quintuples))

for i in range(1000):
	generateHash(i)

while len(keys) < 64:
	cur_hash = hashes.pop(0)[0]
	generateHash(index + 1000)

	match = re.search(r'(\d|\w)\1\1', cur_hash)

	if match:
		letter = match.groups()[0]

		for item in hashes:
			if letter in item[1]:
				keys.append((letter, index))
				print('found key', len(keys), 'at index', index)
				break

	index += 1