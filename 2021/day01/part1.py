
depths = [int(line) for line in open('input.txt')]
print(sum(b > a for a, b in zip(depths, depths[1:])))
