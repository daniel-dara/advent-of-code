from hashlib import md5

i = 1
while not md5(bytes('bgvyzdsv' + str(i), 'ascii')).hexdigest().startswith('000000'):
	i += 1

print(i)