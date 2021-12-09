import re
from math import comb, prod

# This solution relies on the fact that there are no 2 jolt differences.
ratings = sorted(map(int, open('input.txt').readlines()))
ratings = [0] + ratings + [ratings[-1] + 3]
differences = (b - a for a, b in zip(ratings, ratings[1:]))
group_lengths = map(len, re.findall(r'(1{2,})', ''.join(map(str, differences))))
print(prod(1 + comb(length - 1, 1) + comb(length - 1, 2) for length in group_lengths))
