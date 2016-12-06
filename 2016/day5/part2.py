from hashlib import md5

password = {}
i = 0

while len(password.values()) < 8:
	hash = md5(bytes('abbhdwsy' + str(i), 'ascii')).hexdigest()

	if hash.startswith('00000') and hash[5].isdigit() and int(hash[5]) <= 7 and int(hash[5]) not in password:
		password[int(hash[5])] = hash[6]

	i += 1

print(''.join(password.values()))