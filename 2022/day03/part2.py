
lines = open('input.txt').readlines()

print(
	sum(
		(
			a := lines[i].strip(),
			b := lines[i + 1],
			c := lines[i + 2],
			letter := (set(a) & set(b) & set(c)).pop(),
			ord(letter) - (ord('a') - 1 if letter.islower() else ord('A') - 27)
		)[-1]
		for i in range(0, len(lines), 3)
	)
)
