
total = 0

for line in open('input.txt').readlines():
	l, w, h = map(int, line.split('x'))
	total += 2 * (l + w + h - max(l, w, h)) + l * w * h

print(total)
