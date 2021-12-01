
depths = list(map(int, open('input.txt')))
windows = [sum(depths[i:i + 3]) for i in range(len(depths) - 2)]
print(sum(b > a for a, b in zip(windows, windows[1:])))
