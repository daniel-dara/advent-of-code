
print(
	max(
		sum(map(int, elf.split()))
		for elf in open('input.txt').read().split('\n\n')
	)
)

# golf
print(max(eval(open('input.txt').read().replace('\n\n',',').replace('\n','+'))))
