from hashlib import md5
import re

salt   = 'yjdafjpo'
index  = 0
keys   = []
hashes = []

def generateHash(num):
	md5hash = md5(bytes(salt + str(num), 'ascii')).hexdigest()
	quintuples = re.findall(r'(\d|\w)\1\1\1\1', md5hash)

	hashes.append((md5hash, quintuples))

for i in range(1000):
	generateHash(i)

while len(keys) < 64:
	cur_hash = hashes[0][0]

	hashes.pop(0)
	generateHash(index + 1000)

	match = re.search(r'(\d|\w)\1\1', cur_hash)

	if match:
		letter = match.groups()[0]
		found = False

		for item in hashes:
			if letter in item[1]:
				found = True
				break

		if found:
			keys.append((letter, index))
			print('found key', len(keys), 'at index', index)

	index += 1