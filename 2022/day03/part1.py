import string
print(
	sum(
		(
			mid := len(line) // 2,
			letter := (set(line[:mid]) & (set(line[mid:]))).pop(),
			string.ascii_letters.index(letter) + 1
		)[-1]
		for line in open('input.txt')
	)
)
