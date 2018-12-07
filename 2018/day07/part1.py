
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
orderedSteps = ''

# Loop until there are no steps left.
while requirements:
	# Alphabetize steps.
	readySteps.sort()

	nextStep = readySteps.pop(0)

	# Complete the step by removing it from the map. 
	if nextStep in requirements:
		del requirements[nextStep]

	# Add it to the final answer.
	orderedSteps += nextStep

	# Find which steps have the completed step as a requirement.
	for step, dependencies in requirements.items():
		if nextStep in dependencies:
			# Fulfill the requirement.
			dependencies.remove(nextStep)

			# Mark the step as ready if all requirements fulfilled.
			if dependencies == []:
				readySteps.append(step)

print(orderedSteps)
