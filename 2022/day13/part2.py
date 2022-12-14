from functools import cmp_to_key


def is_ordered(A, B):
	for a, b in zip(A, B):
		if type(a) is int and type(b) is int:
			if a != b:
				return b - a
		else:
			x = is_ordered([a] if type(a) is int else a, [b] if type(b) is int else b)

			if x < 0:
				return -1
			elif x > 0:
				return 1

	return len(B) - len(A)


packets = list(map(eval, open('input.txt').read().split())) + [[[2]]] + [[[6]]]
packets = sorted(packets, key=cmp_to_key(is_ordered), reverse=True)

d1 = packets.index([[2]]) + 1
d2 = packets.index([[6]]) + 1
print(d1 * d2)
