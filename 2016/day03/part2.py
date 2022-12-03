
sides = list(map(int, open('input.txt').read().split()))

total = 0
for i in range(len(sides) // 3):
	j = 9 * (i // 3) + i % 3
	a, b, c = sides[j], sides[j + 3], sides[j + 6]
	total += a + b > c and b + c > a and a + c > b

print(total)
