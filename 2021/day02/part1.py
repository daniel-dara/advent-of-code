
horizontal = 0
depth = 0

for line in open('input.txt'):
	direction, num = line.split(' ')
	num = int(num)

	if direction == 'forward':
		horizontal += num
	elif direction == 'down':
		depth += num
	elif direction == 'up':
		depth -= num

print(horizontal * depth)
