sequence = open('input.txt').read()
total = 0

for i in range(len(sequence)):
	if sequence[i] == sequence[(i + (len(sequence) // 2)) % len(sequence)]:
		total += int(sequence[i])

print(total)
