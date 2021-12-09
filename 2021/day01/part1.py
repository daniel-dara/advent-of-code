
depths = list(map(int, open('input.txt')))
print(sum(b > a for a, b in zip(depths, depths[1:])))
