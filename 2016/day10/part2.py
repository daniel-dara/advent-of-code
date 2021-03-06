#
# This solution makes the following assumption (which is true for the given input):
#
# Instructions are not order dependent. When multiple bots have two chips, the order in which they run doesn't change
# the outcome.
#    i.e. A bot will never have more than two chips
#
# Note that part1 of the problem doesn't require keeping track of output.
#
# This solution first populates bots with their initial values and instruction set and then executes instructions
# for each bot with two chips all the way until no bot has two chips. It could technically end when output 0, 1, and 2
# are found but it's just as easy to run to completion for the given input. Then it simply prints their product.
#

import re

VALUE_PATTERN = re.compile(r'value (\d+) goes to bot (\d+)')
GIVE_PATTERN = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')

bots = [{'chips': [], 'instruction': []} for i in range(1000)]

instructions = []
full_bots = []
output = {}

for line in open('input.txt'):
	groups = (VALUE_PATTERN.match(line) or GIVE_PATTERN.match(line)).groups()

	if len(groups) == 2:
		val, bot = map(int, groups)
		bots[bot]['chips'].append(val)

		if len(bots[bot]['chips']) == 2:
			full_bots.append(bot)
	else:
		bots[int(groups[0])]['instruction'] = groups

find_comparison = [17, 61]

while full_bots:
	giver, type1, taker1, type2, taker2 = [int(x) if x.isdigit() else x for x in bots[full_bots[-1]]['instruction']]

	if type1 == 'bot':
		bots[taker1]['chips'].append(min(bots[giver]['chips']))
	else:
		output[taker1] = min(bots[giver]['chips'])

	if type2 == 'bot':
		bots[taker2]['chips'].append(max(bots[giver]['chips']))
	else:
		output[taker2] = max(bots[giver]['chips'])

	bots[giver]['chips'] = []

	full_bots.pop()

	if len(bots[taker1]['chips']) > 1:
		full_bots += [taker1]

	if len(bots[taker2]['chips']) > 1:
		full_bots += [taker2]

print(output[0] * output[1] * output[2])