
print(
	max(
		sum(map(int, elf.split()))
		for elf in open('input.txt').read().split('\n\n')
	)
)
