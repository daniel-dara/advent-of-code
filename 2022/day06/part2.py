LENGTH = 14
data = open('input.txt').read()

print(
	next(
		i + LENGTH
		for i in range(len(data))
		if len(set(data[i:i + LENGTH])) == LENGTH
	)
)
