
# clean
total_score = 0
file = open('input.txt').read()
strategy_guide = file.translate(file.maketrans('ABCXYZ', '012012'))

for line in strategy_guide.split('\n'):
	a, b = map(int, line.split())

	total_score += b + 1

	if a == b:
		total_score += 3
	elif (a + 1) % 3 == b:
		total_score += 6

print(total_score)

# golf
print(sum((i:=ord(l[0])-65,j:=ord(l[2])-88,(j-i+1)%3*3+j+1)[2]for l in open('input.txt')))
