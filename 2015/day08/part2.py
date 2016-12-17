print(sum([2 + sum([c == '"' or c == '\\' for c in line]) for line in open('input.txt')]))
