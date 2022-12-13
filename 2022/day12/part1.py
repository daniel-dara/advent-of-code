file = open('input.txt')
width = len(file.readline()) - 1
height_map = {(i // width, i % width): ord(c) for i, c in enumerate(file.read().replace('\n', ''))}

start = [k for k in height_map if height_map[k] == ord('S')][0]
end = [k for k in height_map if height_map[k] == ord('E')][0]
height_map[start] = ord('a')
height_map[end] = ord('z')

queue = [(start, 0)]
pos_to_steps = {}

while queue:
	cur, steps = queue.pop()

	if cur not in pos_to_steps or steps < pos_to_steps[cur]:
		pos_to_steps[cur] = steps

		for offset in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			new_pos = cur[0] + offset[0], cur[1] + offset[1]

			if new_pos in height_map and height_map[new_pos] - height_map[cur] <= 1:
				queue.append((new_pos, steps + 1))

print(pos_to_steps[end])
