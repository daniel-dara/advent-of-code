
print(
	max(
		sum(map(int, elf.split('\n')))
		for elf in open('input.txt').read().split('\n\n')
	)
)
