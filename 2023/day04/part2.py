from collections import defaultdict

total = 0
multiplier = 1
card_to_multiplier = defaultdict(int, {0: -1})

for number, line in enumerate(open('example.txt')):
	total += multiplier
	first, second = line.split('|')
	winners = set(map(int, first.split(':')[1].split()))
	numbers = set(map(int, second.split()))
	# assumes numbers are unique and there won't be duplicate winners
	winner_count = len(winners.intersection(numbers))

	if winner_count:
		multiplier += 1
		card_to_multiplier[number + winner_count] = -1

	multiplier += card_to_multiplier[number]

print(total)
