
print(
	sum(
		len(value) in [2, 3, 4, 7]
		for line in open('input.txt')
		for value in line.split('|')[1].split()
	)
)
