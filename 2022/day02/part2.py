
# clean
total_score = 0
file = open('input.txt').read()
strategy_guide = file.translate(file.maketrans('ABCXYZ', '012012'))

for line in strategy_guide.split('\n'):
	a, b = map(int, line.split())

	if b == 0:
		# loss
		total_score += 0 + ((a - 1) % 3) + 1
	elif b == 1:
		# draw
		total_score += 3 + (a % 3) + 1
	else:
		# win
		total_score += 6 + ((a + 1) % 3) + 1

print(total_score)

# golf
print(sum((i:=ord(l[0])-65,j:=ord(l[2])-88,j*3+(i+j+2)%3+1)[2]for l in open('input.txt')))
