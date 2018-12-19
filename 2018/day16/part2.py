import re
from itertools import zip_longest
from collections import defaultdict

# https://docs.python.org/3/library/itertools.html
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

class Sample:
	def __init__(self, opcode, a, b, c, before, after):
		self.opcode = opcode
		self.a = a
		self.b = b
		self.c = c
		self.before = before
		self.after = after

	def __repr__(self):
		return 'Sample' + str((self.before, (self.opcode, self.a, self.b, self.c), self.after))

def addr(registers, a, b, c):
	registers[c] = registers[a] + registers[b]
	return registers

def addi(registers, a, b, c):
	registers[c] = registers[a] + b
	return registers

def mulr(registers, a, b, c):
	registers[c] = registers[a] * registers[b]
	return registers

def muli(registers, a, b, c):
	registers[c] = registers[a] * b
	return registers

def banr(registers, a, b, c):
	registers[c] = registers[a] & registers[b]
	return registers

def bani(registers, a, b, c):
	registers[c] = registers[a] & b
	return registers

def borr(registers, a, b, c):
	registers[c] = registers[a] | registers[b]
	return registers

def bori(registers, a, b, c):
	registers[c] = registers[a] | b
	return registers

def setr(registers, a, b, c):
	registers[c] = registers[a]
	return registers

def seti(registers, a, b, c):
	registers[c] = a
	return registers

def gtir(registers, a, b, c):
	registers[c] = int(a > registers[b])
	return registers

def gtri(registers, a, b, c):
	registers[c] = int(registers[a] > b)
	return registers

def gtrr(registers, a, b, c):
	registers[c] = int(registers[a] > registers[b])
	return registers

def eqir(registers, a, b, c):
	registers[c] = int(a == registers[b])
	return registers

def eqri(registers, a, b, c):
	registers[c] = int(registers[a] == b)
	return registers

def eqrr(registers, a, b, c):
	registers[c] = int(registers[a] == registers[b])
	return registers

samples = []

for lineGroup in grouper(map(str.strip, open('input.txt').readlines()), 4):
	if lineGroup[0] == '':
		break

	ints = map(int, re.findall(r'(\d+)', ''.join(lineGroup)))
	before, instruction, after = map(list, grouper(ints, 4))
	opcode, a, b, c = instruction

	samples.append(Sample(opcode, a, b, c, before, after))

ops = [
	addr,
	addi,
	mulr,
	muli,
	banr,
	bani,
	borr,
	bori,
	setr,
	seti,
	gtir,
	gtri,
	gtrr,
	eqir,
	eqri,
	eqrr,
]

total = 0
possibilities = defaultdict(list)

for sample in samples:
	for op in ops:
		if sample.after == op(sample.before.copy(), sample.a, sample.b, sample.c):
			possibilities[sample.opcode] += [op]

for opcode in possibilities:
	print(len(possibilities[opcode]), len(set(possibilities[opcode])))
	possibilities[opcode] = set(possibilities[opcode])

print(possibilities)
