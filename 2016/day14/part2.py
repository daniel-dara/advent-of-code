from hashlib import md5
import re


def generate_hash(num):
	md5hash = 'yjdafjpo' + str(num)

	for i in range(2017):
		md5hash = md5(bytes(md5hash, 'ascii')).hexdigest()

	quintuples = re.findall(r'(\d|\w)\1\1\1\1', md5hash)

	return md5hash, quintuples


def find_64th_key(hashes):
	index = 0
	keys = 0

	while keys < 64:
		cur_hash = hashes.pop(0)[0]
		hashes.append(generate_hash(index + 1000))

		match = re.search(r'(\d|\w)\1\1', cur_hash)

		if match:
			letter = match.groups()[0]

			for item in hashes:
				if letter in item[1]:
					keys += 1
					break

		index += 1

	return index - 1


hashes = [generate_hash(i) for i in range(1000)]
print(find_64th_key(hashes))
