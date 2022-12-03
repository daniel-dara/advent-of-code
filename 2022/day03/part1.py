print(
	sum(
		(
			mid := len(line) // 2,
			letter := (set(line[:mid]) & (set(line[mid:]))).pop(),
			ord(letter) - (ord('a') - 1 if letter.islower() else ord('A') - 27)
		)[-1]
		for line in open('input.txt')
	)
)
