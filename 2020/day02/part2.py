import re

valid_count = 0

for line in open('input.txt'):
    position1, position2, letter, word = re.search(r'(\d+)-(\d+) (\w): (\w+)', line).groups()

    if (word[int(position1) - 1] == letter) ^ (word[int(position2) - 1] == letter):
        valid_count += 1

print(valid_count)
