import hashlib
import unicodedata

password = ''
i = 0

while len(password) < 8:
	hash = hashlib.md5(bytes('abbhdwsy' + str(i), 'ascii')).hexdigest()

	if hash.startswith('00000'):
		print("Found character '" + hash[5] + "' " + str(7 - len(password)) + " more to go.")
		password += hash[5]

	i += 1

print("Completed password: " + password)