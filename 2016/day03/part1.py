
print(
	sum(
		a + b > c and b + c > a and a + c > b
		for a, b, c in [
			map(int, line.split()) for line in open('input.txt').read().split('\n')
		]
	)
)
