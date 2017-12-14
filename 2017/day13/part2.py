firewall = {}

for line in open('input.txt'):
	layer, scanRange = map(int, line.rstrip().split(': '))
	firewall[layer] = scanRange

def willGetCaught(delay):
	for layer, scanRange in firewall.items():
		layer += delay

		if layer == 0 or layer % (2 * (scanRange - 1)) == 0:
			return True

	return False

delay = 0

while willGetCaught(delay):
	delay += 1

print(delay)