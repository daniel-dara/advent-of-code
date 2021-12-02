
horizontal = 0
depth = 0
aim = 0

for line in open('input.txt'):
	direction, num = line.split(' ')
	num = int(num)

	if direction == 'forward':
		horizontal += num
		depth += aim * num
	elif direction == 'down':
		aim += num
	elif direction == 'up':
		aim -= num

print (horizontal * depth)
