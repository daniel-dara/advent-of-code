import re
from collections import defaultdict

# Maps steps to their requirements
requirements = defaultdict(list)
allSteps = set()

# Parse input.
for line in open('input.txt'):
	requirement, step = re.findall(r'(?:S|s)tep (\w) ', line)
	requirements[step].append(requirement)
	allSteps.add(requirement)

# Any steps that don't have requirements are ready.
readySteps = list(allSteps - set(requirements.keys()))

def timeValue(character):
	return ord(character) - ord('A') + 61

MAX_WORKERS = 5
totalTicks  = 0
workerSteps = [] # Step the worker is working on.
workerTimes = [] # Time left for the step the worker is on.

def finishWorker(i):
	# Remove the worker from the arrays.
	completedStep = workerSteps.pop(i)
	del workerTimes[i]

	# Find which steps have the completed step as a requirement.
	for step, dependencies in requirements.items():
		if completedStep in dependencies:
			# Fulfill the requirement.
			requirements[step].remove(completedStep)

			# Mark the step as ready if all requirements fulfilled.
			if dependencies == []:
				readySteps.append(step)

# Process until all requirements are gone and the workers are empty.
while requirements or workerSteps:
	# Alphabetize steps.
	readySteps.sort()

	# Give the workers worker until there is no more work or no more free workers.
	while readySteps and len(workerTimes) < MAX_WORKERS:
		nextStep = readySteps.pop(0)

		# Remove the in progress step from the map.
		if nextStep in requirements:
			del requirements[nextStep]

		# Give the next available worker the step.
		workerSteps.append(nextStep)
		workerTimes.append(timeValue(nextStep))

	# Pass the time and update work times.
	totalTicks += 1
	workerTimes = [time - 1 for time in workerTimes]

	# Call finishWorker for each finished worker.
	list(map(finishWorker, [i for i, time in enumerate(workerTimes) if time == 0]))

print(totalTicks)
