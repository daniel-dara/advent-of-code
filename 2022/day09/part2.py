snake = [(0, 0)] * 10
visited = {snake[-1]}

for line in open('input.txt'):
	d = line.split()[0]

	for _ in range(int(line.split()[1])):
		snake[0] = snake[0][0] + (d == 'R') - (d == 'L'), snake[0][1] + (d == 'D') - (d == 'U')

		for i in range(1, 10):
			h = snake[i - 1]
			t = snake[i]

			if max(abs(t[0] - h[0]), abs(t[1] - h[1])) == 2:
				t = t[0] + (t[0] < h[0]) - (t[0] > h[0]), t[1] + (t[1] < h[1]) - (t[1] > h[1])

			snake[i - 1] = h
			snake[i] = t

		visited.add(snake[-1])

print(len(visited))
