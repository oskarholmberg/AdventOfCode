input_file = "../inputs/Day_1.txt"

#Read file
with open(input_file) as f:
    puzzle_input = f.readlines()

#Part 1
changes = [int(n.strip()) for n in puzzle_input]
print(f'Part 1: {sum(changes)}')

#Part 2
from itertools import accumulate, cycle
seen = set()
print(f'Part 2: {next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f))}')
