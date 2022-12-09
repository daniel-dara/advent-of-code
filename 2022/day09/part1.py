h = t = (0, 0)
visited = {t}

for line in open('input.txt'):
	for _ in range(int(line.split()[1])):
		match line.split()[0]:
			case 'R':
				h = h[0] + 1, h[1]
			case 'L':
				h = h[0] - 1, h[1]
			case 'U':
				h = h[0], h[1] - 1
			case 'D':
				h = h[0], h[1] + 1

		if max(abs(t[0] - h[0]), abs(t[1] - h[1])) == 2:
			t = t[0] + int(t[0] < h[0]) - int(t[0] > h[0]), t[1] + int(t[1] < h[1]) - int(t[1] > h[1])

		visited.add(t)

print(len(visited))
