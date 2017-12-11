

input_file = open("../inputs/first.txt", 'r')

puzzle_input = list(input_file.readline())

total = 0

puzzle_input = [int(digit) for digit in puzzle_input]

for i in range(len(puzzle_input)):
    comp_index = (i+1)%(len(puzzle_input))
    if puzzle_input[i] == puzzle_input[comp_index]:
        total += puzzle_input[i]

print(f"Part 1: {total}")

total = 0

for i in range(len(puzzle_input)):
    comp_index = int((i+len(puzzle_input)/2)%(len(puzzle_input)))
    if puzzle_input[i] == puzzle_input[comp_index]:
        total += puzzle_input[i]

print(f"Part 2: {total}")