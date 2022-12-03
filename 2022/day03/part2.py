import string

lines = open('input.txt').readlines()

print(
	sum(
		(
			letter := (set.intersection(*map(set, lines[i:i + 3])) - {'\n'}).pop(),
			string.ascii_letters.index(letter) + 1
		)[-1]
		for i in range(0, len(lines), 3)
	)
)

