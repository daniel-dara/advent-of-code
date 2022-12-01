
total = 0

for line in open('input.txt').readlines():
	l, w, h = map(int, line.split('x'))
	total += 2 * (w * l + h * l + h * w) + l * w * h // max(l, w, h)

print(total)
