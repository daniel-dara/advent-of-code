from hashlib import md5

password = ''
i = 0

while len(password) < 8:
	hash = md5(bytes('abbhdwsy' + str(i), 'ascii')).hexdigest()

	if hash.startswith('00000'):
		password += hash[5]

	i += 1

print(password)