from sys import stdin
from collections import Counter

counters = [Counter() for _ in range(8)]

for word in open('input.txt').readlines():
	for i in range(8):
		counters[i][word[i]] += 1

answer = ''

for c in counters:
	answer += c.most_common(1)[0][0]

print(answer)