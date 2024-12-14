total = 0

for line in open('input.txt'):
	first, second = line.split('|')
	winners = set(map(int, first.split(':')[1].split()))
	numbers = set(map(int, second.split()))
	# assumes numbers are unique and there won't be duplicate winners
	total += int(2 ** (len(winners.intersection(numbers)) - 1))

print(total)
