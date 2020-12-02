import re
from collections import Counter

valid_count = 0

for line in open('input.txt'):
    minimum, maximum, letter, word = re.search('(\\d+)-(\\d+) (\\w): (\\w+)', line).groups()

    if int(minimum) <= Counter(word)[letter] <= int(maximum):
        valid_count += 1

print(valid_count)
