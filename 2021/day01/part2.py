
depths = [int(line) for line in open('input.txt')]
windows = [sum(numbers) for numbers in zip(depths, depths[1:], depths[2:])]
print(sum(b > a for a, b in zip(windows, windows[1:])))
