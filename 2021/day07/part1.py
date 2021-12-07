from statistics import median

positions = list(map(int, open('input.txt').read().split(',')))
print(int(sum(abs(p - median(positions)) for p in positions)))
