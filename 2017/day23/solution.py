from collections import defaultdict

instructions = tuple(
    tuple(map(lambda x: x if x.isalpha() else int(x), line.rstrip().split(' ')))
    for line in open('input.txt')
)

registers = defaultdict(lambda: 0)
index, mul_count = 0, 0

while 0 <= index < len(instructions):
    instruction, arg_x, arg_y = instructions[index]
    arg_y = arg_y if type(arg_y) == int else registers[arg_y]

    if instruction == 'set':
        registers[arg_x] = arg_y
    elif instruction == 'sub':
        registers[arg_x] -= arg_y
    elif instruction == 'mul':
        registers[arg_x] *= arg_y
        mul_count += 1
    else:
        index += 1 if (arg_x if type(arg_x) == int else registers[arg_x]) == 0 else arg_y
        continue

    index += 1

print('part 1:', mul_count)
