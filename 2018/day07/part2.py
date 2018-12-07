import re
from collections import defaultdict

requirements = defaultdict(list)

def timeValue(char):
	return ord(char) - ord('A') + 61

for line in open('input.txt'):
	a, b = re.findall(r'(?:S|s)tep (\w) ', line)
	requirements[b].append(a)

	if a not in requirements:
		requirements[a] = []

workers = []
workerSteps = []
maxWorkers = 5
totalTicks = 0

def finishStep(i):
	global workers, requirements, workerSteps

	del workers[i]
	del requirements[workerSteps[i]]

	for step, dependencies in requirements.items():
		if workerSteps[i] in dependencies:
			requirements[step].remove(workerSteps[i])

	del workerSteps[i]

	print('after delete', workerSteps)

def tick():
	global totalTicks, workers
	print(totalTicks, workers, workerSteps)

	totalTicks += 1

	i = 0
	while i < len(workers):
		workers[i] -= 1

		if workers[i] <= 0:
			print('finishing', workerSteps[i])
			finishStep(i)
		else:
			i += 1

while requirements:
	possibilities = []

	for step, dependencies in requirements.items():
		if dependencies == [] and step not in workerSteps:
			possibilities.append(step)

	possibilities.sort()

	while possibilities and len(workers) < maxWorkers:
		workerSteps.append(possibilities[0])
		workers.append(timeValue(possibilities.pop(0)))

	tick()

print(totalTicks)

# wrong
# 229
# 230
