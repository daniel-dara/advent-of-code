snake = [(0, 0)] * 10
visited = {snake[-1]}

for line in open('input.txt'):
	for _ in range(int(line.split()[1])):
		h = snake[0]

		match line.split()[0]:
			case 'R':
				h = h[0] + 1, h[1]
			case 'L':
				h = h[0] - 1, h[1]
			case 'U':
				h = h[0], h[1] - 1
			case 'D':
				h = h[0], h[1] + 1

		snake[0] = h

		for i in range(1, 10):
			h = snake[i - 1]
			t = snake[i]

			if max(abs(t[0] - h[0]), abs(t[1] - h[1])) == 2:
				t = t[0] + int(t[0] < h[0]) - int(t[0] > h[0]), t[1] + int(t[1] < h[1]) - int(t[1] > h[1])

			snake[i - 1] = h
			snake[i] = t

		visited.add(snake[-1])

print(len(visited))
