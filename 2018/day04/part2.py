import re
from collections import defaultdict
import datetime

guards = defaultdict(list)
totalSleep = defaultdict(int)
lastGuard = None

for line in sorted(open('input.txt').read().split('\n')):
	year, month, day, hour, minute, *guard = map(int, re.findall('\d+', line))

	if guard:
		lastGuard = guard[0]
	elif 'asleep' in line:
		sleepTime = datetime.datetime(year, month, day, hour, minute)
	elif 'wake' in line:
		wakeTime = datetime.datetime(year, month, day, hour, minute)

		guards[lastGuard].append((sleepTime, wakeTime))
		totalSleep[lastGuard] += (wakeTime - sleepTime).seconds // 60

bestMinutes = {}

for guard, timeRanges in guards.items():
	minutes = defaultdict(int)

	for timeRange in timeRanges:
		sleepTime, wakeTime = timeRange

		for minute in range((wakeTime - sleepTime).seconds // 60):
			minutes[(sleepTime.minute + minute) % 60] += 1

	mostCommonMinute = max(minutes, key=lambda guard: minutes[guard])

	bestMinutes[guard] = (mostCommonMinute, minutes[mostCommonMinute])

bestGuard = max(bestMinutes, key=lambda guard: bestMinutes[guard][1])
print(bestGuard * bestMinutes[bestGuard][0])
