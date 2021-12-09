import operator

op_map = {'+': operator.add, '*': operator.mul, '(': None}
equations = [equation.strip().replace('(', '( ').replace(')', ' )').split(' ') for equation in open('input.txt')]
values = []

for equation in equations:
	op_stack = []
	value_stack = []

	for part in equation:
		if part in op_map:
			op_stack.append(part)
		else:
			if part == ')':
				op_stack.pop()
			else:
				value_stack.append(int(part))

			while len(value_stack) >= 2 and op_stack[-1] != '(':
				a, b, op = value_stack.pop(), value_stack.pop(), op_map[op_stack.pop()]
				value_stack.append(op(b, a))

	values.append(value_stack[0])

print(sum(values))
