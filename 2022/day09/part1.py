h = t = (0, 0)
visited = {t}

for line in open('input.txt'):
	d = line.split()[0]

	for _ in range(int(line.split()[1])):
		h = h[0] + (d == 'R') - (d == 'L'), h[1] + (d == 'D') - (d == 'U')

		if max(abs(t[0] - h[0]), abs(t[1] - h[1])) == 2:
			t = t[0] + (t[0] < h[0]) - (t[0] > h[0]), t[1] + (t[1] < h[1]) - (t[1] > h[1])

		visited.add(t)

print(len(visited))
