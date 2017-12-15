import re

maxDistance = 0
reindeers = {}

class Reindeer:
	def __init__(self, speed, speedDuration, restDuration):
		self.speed = speed
		self.speedDuration = speedDuration
		self.restDuration = restDuration
		self.score = 0

	def getDistance(self, elapsedSeconds):
		return self.speed * self.speedDuration * (elapsedSeconds // (self.speedDuration + self.restDuration)) + self.speed * min(self.speedDuration, elapsedSeconds % (self.speedDuration + self.restDuration))

for line in open('input.txt'):
	name, speed, speedDuration, restDuration = [line.split(' ')[0]] + list(map(int, re.findall('\d+', line)))
	reindeers[name] = Reindeer(speed, speedDuration, restDuration)

for elapsedSeconds in range(1, 2504):
	maxDistance = 0

	for name, reindeer in reindeers.items():
		distance = reindeer.getDistance(elapsedSeconds)

		if distance >= maxDistance:
			if distance > maxDistance:
				winners = []

			winners.append(name)
			maxDistance = distance

	for name in winners:
		reindeers[name].score += 1

print(max(map(lambda r: r.score, reindeers.values())))
