lines = open('input.txt').readlines()

print(
	sum(
		(
			letter := (set.intersection(*map(set, lines[i:i + 3])) - set('\n')).pop(),
			ord(letter) - (ord('a') - 1 if letter.islower() else ord('A') - 27)
		)[-1]
		for i in range(0, len(lines), 3)
	)
)
