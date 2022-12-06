LENGTH = 4
data = open('input.txt').read()

print(
	next(
		i + LENGTH
		for i in range(len(data))
		if len(set(data[i:i + LENGTH])) == LENGTH
	)
)

# With zipping
print(
	next(
		i + LENGTH
		for i, group in enumerate(
			zip(*[data[i:] for i in range(LENGTH)])
		)
		if len(set(group)) == LENGTH
	)
)
