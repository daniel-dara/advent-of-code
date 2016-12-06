import hashlib
import unicodedata

password = {}
i = 0

while len(password.values()) < 8:
	hash = hashlib.md5(bytes('abbhdwsy' + str(i), 'ascii')).hexdigest()

	if hash.startswith('00000') and hash[5].isdigit() and int(hash[5]) <= 7 and int(hash[5]) not in password:
		print("Found character '" + hash[6] + "' for position " + hash[5] + ", " + str(8 - len(password.values())) + " more to go.")
		password[int(hash[5])] = hash[6]

	i += 1

print(''.join(password.values()))