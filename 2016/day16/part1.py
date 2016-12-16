
def dragCurve(data):
	return data + '0' + data[::-1].replace('1', '2').replace('0', '1').replace('2', '0')

def checkSum(data):
	while len(data) % 2 == 0:
		checksum = ''

		for i in range(0, len(data), 2):
			checksum += str(int(data[i] == data[i + 1]))

		data = checksum

	return checksum

data = '11100010111110100'
size = 272

while len(data) < size:
	data = dragCurve(data)

print(checkSum(data[:size]))
