import re

values = {}
rules  = []

for line in open('input.txt'):
	cmd   = (re.findall(r'NOT|AND|OR|LSHIFT|RSHIFT', line) or [None])[0]
	wires = re.findall(r'[a-z]+', line)
	nums  = list(map(int, re.findall(r'\d+', line)))

	if cmd == None and nums:
		values[wires[0]] = nums[0]
	else:
		rules.append((cmd, wires, nums))

while 'a' not in values:
	for rule in rules:
		cmd, wires, nums = rule

		if not sum(wire not in values for wire in wires[:-1]):
			if cmd == 'NOT':
				values[wires[1]] = (~values[wires[0]]) & 2**16 - 1
			elif cmd == 'AND':
				if nums:
					values[wires[1]] = (nums[0] & values[wires[0]]) & 2**16 - 1
				else:
					values[wires[2]] = (values[wires[0]] & values[wires[1]]) & 2**16 - 1
			elif cmd == 'OR':
				values[wires[2]] = (values[wires[0]] | values[wires[1]]) & 2**16 - 1
			elif cmd == 'LSHIFT':
				values[wires[1]] = (values[wires[0]] << nums[0]) & 2**16 - 1
			elif cmd == 'RSHIFT':
				values[wires[1]] = (values[wires[0]] >> nums[0]) & 2**16 - 1
			else:
				values[wires[1]] = values[wires[0]]

		if 'a' in values:
			break;

print(values['a'])