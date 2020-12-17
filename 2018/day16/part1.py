import operator
import re
from copy import deepcopy
from typing import List

opnames = (
	'addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
	'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr'
)

opmap = {
	'ad': operator.add,
	'mu': operator.mul,
	'ba': operator.and_,
	'bo': operator.or_,
	'se': lambda a, _: a,
	'gt': operator.gt,
	'eq': operator.eq,
}


def execute(regs: List[int], opname: str, a: int, b: int, c: int) -> List[int]:
	a = a if opname[2] == 'i' or opname == 'seti' else regs[a]
	b = b if opname[3] == 'i' else regs[b]
	regs[c] = int(opmap[opname[:2]](a, b))
	return regs


numbers = list(map(int, re.findall(r'\d+', open('input.txt').read().split('\n\n\n')[0])))
samples = []

for i in range(0, len(numbers), 12):
	regs_in = numbers[i:i + 4]
	opcode, A, B, C = numbers[i + 4:i + 8]
	regs_out = numbers[i + 8:i + 12]

	possible_opnames = [opname for opname in opnames if execute(deepcopy(regs_in), opname, A, B, C) == regs_out]
	samples.append(possible_opnames)

print(sum(1 for sample in samples if len(sample) >= 3))
