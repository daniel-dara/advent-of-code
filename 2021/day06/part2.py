fish_times = open('input.txt').read().split(',')
fish_by_day = [fish_times.count(str(i)) for i in range(9)]

for _ in range(256):
	new_fish = fish_by_day.pop(0)  # fish at 0 will create new fish
	fish_by_day[6] += new_fish  # fish at 0 also get revived at 6 days
	fish_by_day.append(new_fish)  # new fish start at 8 days which is the end of the day range

print(sum(fish_by_day))
