print(sum(abs(a - b) for a, b in zip(*map(sorted, zip(*(map(int, line.split()) for line in open('input.txt')))))))
