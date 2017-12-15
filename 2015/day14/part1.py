import re

elapsedSeconds = 2503
maxDistance = 0

for line in open('input.txt'):
	reindeer, speed, speedDuration, restDuration = [line.split(' ')[0]] + list(map(int, re.findall('\d+', line)))
	distance = speed * speedDuration * (elapsedSeconds // (speedDuration + restDuration)) + speed * min(speedDuration, elapsedSeconds % (speedDuration + restDuration))
	maxDistance = max(maxDistance, distance)

print(maxDistance)
